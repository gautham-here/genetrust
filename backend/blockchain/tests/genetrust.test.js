const { expect }  = require("chai");
const { ethers }  = require("hardhat");

describe("GeneTrust Contracts", function () {
  let registry, policy, ledger;
  let owner, lab, patient, stranger;

  // Deterministic test genome hash (mimics SHA-256 output)
  const GENOME_HASH = ethers.keccak256(ethers.toUtf8Bytes("ATCGATCG...sample"));
  const SAMPLE_ID   = "SAMPLE-001";

  beforeEach(async function () {
    [owner, lab, patient, stranger] = await ethers.getSigners();

    registry = await (await ethers.getContractFactory("GenomicRegistry")).deploy();
    policy   = await (await ethers.getContractFactory("AccessPolicy")).deploy();
    ledger   = await (await ethers.getContractFactory("AuditLedger")).deploy();
  });

  // ── GenomicRegistry ────────────────────────────────────────────────────────
  describe("GenomicRegistry", function () {
    it("registers a genome and emits event", async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      const event = receipt.logs.find(
        (l) => l.fragment?.name === "GenomeRegistered"
      );
      expect(event).to.not.be.undefined;
    });

    it("returns correct record after registration", async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      const recordId = receipt.logs[0].args[0];

      const [gh, submitter, ts, sid, revoked] = await registry.getRecord(recordId);
      expect(gh).to.equal(GENOME_HASH);
      expect(submitter).to.equal(lab.address);
      expect(sid).to.equal(SAMPLE_ID);
      expect(revoked).to.be.false;
    });

    it("verifies hash correctly", async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      const recordId = receipt.logs[0].args[0];

      const [valid] = await registry.verifyGenome(recordId, GENOME_HASH);
      expect(valid).to.be.true;

      const [invalid] = await registry.verifyGenome(recordId, ethers.ZeroHash);
      expect(invalid).to.be.false;
    });

    it("only owner can revoke", async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      const recordId = receipt.logs[0].args[0];

      await expect(
        registry.connect(stranger).revokeGenome(recordId)
      ).to.be.revertedWith("GenomicRegistry: not owner");

      await registry.connect(lab).revokeGenome(recordId);
      const [valid] = await registry.verifyGenome(recordId, GENOME_HASH);
      expect(valid).to.be.false;
    });
  });

  // ── AccessPolicy ───────────────────────────────────────────────────────────
  describe("AccessPolicy", function () {
    let recordId;

    beforeEach(async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      recordId = receipt.logs[0].args[0];
      await policy.connect(lab).createPolicy(recordId, patient.address);
    });

    it("consent is false by default", async function () {
      const [, consent] = await policy.getPolicyInfo(recordId);
      expect(consent).to.be.false;
    });

    it("patient can give and withdraw consent", async function () {
      await policy.connect(patient).setConsent(recordId, true);
      const [, consent] = await policy.getPolicyInfo(recordId);
      expect(consent).to.be.true;

      await policy.connect(patient).setConsent(recordId, false);
      const [, noConsent] = await policy.getPolicyInfo(recordId);
      expect(noConsent).to.be.false;
    });

    it("lab is unauthorised without consent", async function () {
      await policy.connect(patient).grantRole(recordId, lab.address, 2 /* LAB */);
      const auth = await policy.isAuthorised(recordId, lab.address, 2);
      expect(auth).to.be.false; // consent not given yet
    });

    it("lab is authorised after consent", async function () {
      await policy.connect(patient).setConsent(recordId, true);
      await policy.connect(patient).grantRole(recordId, lab.address, 2);
      const auth = await policy.isAuthorised(recordId, lab.address, 2);
      expect(auth).to.be.true;
    });

    it("stranger has no access even with consent", async function () {
      await policy.connect(patient).setConsent(recordId, true);
      const auth = await policy.isAuthorised(recordId, stranger.address, 1);
      expect(auth).to.be.false;
    });
  });

  // ── AuditLedger ────────────────────────────────────────────────────────────
  describe("AuditLedger", function () {
    let recordId;
    const DATA_HASH = ethers.keccak256(ethers.toUtf8Bytes('{"event":"upload","ts":1234567890}'));

    beforeEach(async function () {
      const tx = await registry.connect(lab).registerGenome(GENOME_HASH, SAMPLE_ID);
      const receipt = await tx.wait();
      recordId = receipt.logs[0].args[0];
    });

    it("logs an audit entry and increments counter", async function () {
      await ledger.connect(lab).log(recordId, 1 /* EVT_UPLOAD */, DATA_HASH, "Genome uploaded");
      expect(await ledger.totalEntries()).to.equal(1n);
    });

    it("retrieves the correct entry", async function () {
      await ledger.connect(lab).log(recordId, 1, DATA_HASH, "Genome uploaded");
      const [rid, actor, evtType, dh, , desc] = await ledger.getEntry(0);
      expect(rid).to.equal(recordId);
      expect(actor).to.equal(lab.address);
      expect(evtType).to.equal(1);
      expect(dh).to.equal(DATA_HASH);
      expect(desc).to.equal("Genome uploaded");
    });

    it("verifies entry hash correctly", async function () {
      await ledger.connect(lab).log(recordId, 1, DATA_HASH, "Genome uploaded");
      expect(await ledger.verifyEntry(0, DATA_HASH)).to.be.true;
      expect(await ledger.verifyEntry(0, ethers.ZeroHash)).to.be.false;
    });

    it("indexes entries by recordId", async function () {
      await ledger.connect(lab).log(recordId, 1, DATA_HASH, "Upload");
      await ledger.connect(lab).log(recordId, 3, DATA_HASH, "AI analysis");
      const indices = await ledger.getEntriesForRecord(recordId);
      expect(indices.length).to.equal(2);
    });
  });
});