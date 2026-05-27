const { ethers } = require("hardhat");
const fs = require("fs");
const path = require("path");

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying GeneTrust contracts with:", deployer.address);
  console.log(
    "Balance:",
    ethers.formatEther(await deployer.provider.getBalance(deployer.address)),
    "MATIC"
  );

  // 1. GenomicRegistry
  const Registry = await ethers.getContractFactory("GenomicRegistry");
  const registry = await Registry.deploy();
  await registry.waitForDeployment();
  console.log("GenomicRegistry deployed to:", await registry.getAddress());

  // 2. AccessPolicy
  const Policy = await ethers.getContractFactory("AccessPolicy");
  const policy = await Policy.deploy();
  await policy.waitForDeployment();
  console.log("AccessPolicy    deployed to:", await policy.getAddress());

  // 3. AuditLedger
  const Ledger = await ethers.getContractFactory("AuditLedger");
  const ledger = await Ledger.deploy();
  await ledger.waitForDeployment();
  console.log("AuditLedger     deployed to:", await ledger.getAddress());

  // ── Persist addresses for the Python backend ──────────────────────────────
  const addresses = {
    network:          (await ethers.provider.getNetwork()).name,
    chainId:          Number((await ethers.provider.getNetwork()).chainId),
    deployedAt:       new Date().toISOString(),
    GenomicRegistry:  await registry.getAddress(),
    AccessPolicy:     await policy.getAddress(),
    AuditLedger:      await ledger.getAddress(),
  };

  const outPath = path.resolve(__dirname, "../deployed_addresses.json");
  fs.writeFileSync(outPath, JSON.stringify(addresses, null, 2));
  console.log("\nAddresses saved to", outPath);

  // Also copy into backend for easy import
  const backendPath = path.resolve(
    __dirname,
    "../../backend/app/blockchain/deployed_addresses.json"
  );
  fs.mkdirSync(path.dirname(backendPath), { recursive: true });
  fs.writeFileSync(backendPath, JSON.stringify(addresses, null, 2));
  console.log("Addresses also copied to", backendPath);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});