"""
chain_service.py
────────────────
Python / web3.py integration layer for the three GeneTrust smart contracts.

Responsibilities:
  • Hash & sign genome data before it hits the chain (Chain lane: "Hash & sign")
  • Write genome registrations to GenomicRegistry
  • Create / update AccessPolicy records
  • Append to AuditLedger for every significant platform event

Environment variables required (add to backend/.env):
  WEB3_PROVIDER_URL       – e.g. http://127.0.0.1:8545  (local) or Alchemy/Infura URL
  DEPLOYER_PRIVATE_KEY    – hex private key of the backend hot wallet
  CHAIN_ID                – 31337 (local hardhat) or 80002 (Polygon Amoy)

ABIs are loaded from deployed_addresses.json written by scripts/deploy.js.
"""

import hashlib
import json
import os
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent.parent / ".env")
from web3 import Web3
#from web3.middleware import ExtraDataToPOAMiddleware  # needed for Polygon

logger = logging.getLogger(__name__)

# ── Load deployed addresses & ABIs ────────────────────────────────────────────

_BASE = Path(__file__).parent

def _load_addresses() -> dict:
    path = _BASE / "deployed_addresses.json"
    if not path.exists():
        raise FileNotFoundError(
            "deployed_addresses.json not found. Run `npm run deploy:local` first."
        )
    return json.loads(path.read_text())

def _load_abi(contract_name: str) -> list:
    """
    Hardhat writes compiled artifacts to blockchain/artifacts/contracts/<Name>.sol/<Name>.json.
    We ship the ABI alongside this file for convenience; update it after recompiling.
    """
    abi_path = _BASE / "abis" / f"{contract_name}.json"
    if not abi_path.exists():
        raise FileNotFoundError(
            f"ABI file not found: {abi_path}. "
            "Copy it from blockchain/artifacts/contracts/<Name>.sol/<Name>.json"
        )
    return json.loads(abi_path.read_text())["abi"]


# ── ChainService ──────────────────────────────────────────────────────────────

class ChainService:
    """
    Singleton-like service for all on-chain interactions.
    Instantiate once at application startup (e.g. in FastAPI lifespan).
    """

    def __init__(self):
        provider_url = os.getenv("WEB3_PROVIDER_URL", "http://127.0.0.1:8545")
        private_key  = os.getenv("DEPLOYER_PRIVATE_KEY")
        self.chain_id = int(os.getenv("CHAIN_ID", "31337"))

        if not private_key:
            raise EnvironmentError("DEPLOYER_PRIVATE_KEY is not set")

        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        # Polygon (and most PoA chains) require this middleware
        if self.chain_id != 31337:
            self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

        if not self.w3.is_connected():
            raise ConnectionError(f"Cannot connect to Web3 provider at {provider_url}")

        self.account = self.w3.eth.account.from_key(private_key)
        logger.info("ChainService: connected as %s on chain %d", self.account.address, self.chain_id)

        addrs = _load_addresses()
        self.registry = self.w3.eth.contract(
            address=Web3.to_checksum_address(addrs["GenomicRegistry"]),
            abi=_load_abi("GenomicRegistry"),
        )
        self.access_policy = self.w3.eth.contract(
            address=Web3.to_checksum_address(addrs["AccessPolicy"]),
            abi=_load_abi("AccessPolicy"),
        )
        self.audit_ledger = self.w3.eth.contract(
            address=Web3.to_checksum_address(addrs["AuditLedger"]),
            abi=_load_abi("AuditLedger"),
        )

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _send(self, fn) -> dict:
        """Build, sign, and broadcast a transaction. Returns receipt dict."""
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        tx = fn.build_transaction({
            "from":     self.account.address,
            "nonce":    nonce,
            "chainId":  self.chain_id,
            "gas":      500_000,
            "gasPrice": self.w3.eth.gas_price,
        })
        signed = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

    @staticmethod
    def hash_genome(anonymized_sequence: str) -> bytes:
        """
        Compute SHA-256 of the anonymized genomic sequence.
        Returns raw 32 bytes (bytes32-compatible).
        """
        return hashlib.sha256(anonymized_sequence.encode()).digest()

    @staticmethod
    def hash_event_payload(payload: dict) -> bytes:
        """Hash an audit event payload dict → bytes32."""
        serialised = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(serialised.encode()).digest()

    # ── GenomicRegistry ───────────────────────────────────────────────────────

    def register_genome(self, anonymized_sequence: str, sample_id: str) -> dict:
        """
        Hash the sequence and register it on GenomicRegistry.
        Returns {"tx_hash", "record_id", "genome_hash"}.
        """
        genome_hash_bytes = self.hash_genome(anonymized_sequence)
        receipt = self._send(
            self.registry.functions.registerGenome(genome_hash_bytes, sample_id)
        )

        # Parse GenomeRegistered event to extract recordId
        events = self.registry.events.GenomeRegistered().process_receipt(receipt)
        record_id = events[0]["args"]["recordId"].hex() if events else None

        logger.info("Genome registered: recordId=%s sampleId=%s", record_id, sample_id)
        return {
            "tx_hash":     receipt["transactionHash"].hex(),
            "record_id":   record_id,
            "genome_hash": genome_hash_bytes.hex(),
            "block":       receipt["blockNumber"],
        }

    def verify_genome(self, record_id_hex: str, anonymized_sequence: str) -> dict:
        """
        Re-hash the sequence and call verifyGenome on-chain.
        Returns {"valid", "timestamp"}.
        """
        record_id = bytes.fromhex(record_id_hex)
        genome_hash = self.hash_genome(anonymized_sequence)
        valid, timestamp = self.registry.functions.verifyGenome(record_id, genome_hash).call()
        return {"valid": valid, "timestamp": timestamp}

    def revoke_genome(self, record_id_hex: str) -> dict:
        record_id = bytes.fromhex(record_id_hex)
        receipt = self._send(self.registry.functions.revokeGenome(record_id))
        return {"tx_hash": receipt["transactionHash"].hex()}

    # ── AccessPolicy ──────────────────────────────────────────────────────────

    ROLE_MAP = {"patient": 1, "lab": 2, "admin": 3}

    def create_policy(self, record_id_hex: str, patient_address: str) -> dict:
        """Create on-chain access policy after genome registration."""
        record_id      = bytes.fromhex(record_id_hex)
        patient_cs     = Web3.to_checksum_address(patient_address)
        receipt = self._send(
            self.access_policy.functions.createPolicy(record_id, patient_cs)
        )
        return {"tx_hash": receipt["transactionHash"].hex()}

    def set_consent(self, record_id_hex: str, consent: bool, caller_key: Optional[str] = None) -> dict:
        """
        Patient (or their proxy) gives / withdraws consent.
        Pass caller_key to override the default backend wallet (for patient-initiated calls).
        """
        record_id = bytes.fromhex(record_id_hex)
        # Allow patient to call with their own key via caller_key
        if caller_key:
            acct = self.w3.eth.account.from_key(caller_key)
            nonce = self.w3.eth.get_transaction_count(acct.address)
            tx = self.access_policy.functions.setConsent(record_id, consent).build_transaction({
                "from": acct.address, "nonce": nonce,
                "chainId": self.chain_id, "gas": 200_000,
                "gasPrice": self.w3.eth.gas_price,
            })
            signed  = acct.sign_transaction(tx)
            tx_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        else:
            receipt = self._send(
                self.access_policy.functions.setConsent(record_id, consent)
            )
        return {"tx_hash": receipt["transactionHash"].hex(), "consent": consent}

    def grant_role(self, record_id_hex: str, grantee_address: str, role: str) -> dict:
        record_id   = bytes.fromhex(record_id_hex)
        grantee_cs  = Web3.to_checksum_address(grantee_address)
        role_int    = self.ROLE_MAP.get(role.lower(), 1)
        receipt = self._send(
            self.access_policy.functions.grantRole(record_id, grantee_cs, role_int)
        )
        return {"tx_hash": receipt["transactionHash"].hex(), "role": role}

    def is_authorised(self, record_id_hex: str, caller_address: str, min_role: str = "patient") -> bool:
        record_id  = bytes.fromhex(record_id_hex)
        caller_cs  = Web3.to_checksum_address(caller_address)
        min_int    = self.ROLE_MAP.get(min_role.lower(), 1)
        return self.access_policy.functions.isAuthorised(record_id, caller_cs, min_int).call()

    # ── AuditLedger ───────────────────────────────────────────────────────────

    EVENT_TYPES = {
        "upload":      1,
        "access":      2,
        "ai_analysis": 3,
        "consent":     4,
        "revocation":  5,
        "role_change": 6,
        "anomaly":     7,
        "export":      8,
    }

    def log_event(
        self,
        event_type: str,
        payload: dict,
        description: str,
        record_id_hex: Optional[str] = None,
    ) -> dict:
        """
        Append an audit entry to AuditLedger.
        payload is hashed before being stored — raw data stays off-chain.
        """
        record_id_bytes = bytes.fromhex(record_id_hex) if record_id_hex else b"\x00" * 32
        data_hash       = self.hash_event_payload(payload)
        evt_int         = self.EVENT_TYPES.get(event_type.lower(), 2)

        receipt = self._send(
            self.audit_ledger.functions.log(
                record_id_bytes, evt_int, data_hash, description
            )
        )
        events = self.audit_ledger.events.AuditLogged().process_receipt(receipt)
        idx = events[0]["args"]["entryIndex"] if events else None

        logger.info("Audit logged: type=%s idx=%s desc=%s", event_type, idx, description)
        return {
            "tx_hash":   receipt["transactionHash"].hex(),
            "entry_index": idx,
            "data_hash": data_hash.hex(),
        }

    def get_audit_trail(self, record_id_hex: str) -> list[dict]:
        """Return all on-chain audit entries for a genome record."""
        record_id = bytes.fromhex(record_id_hex)
        indices   = self.audit_ledger.functions.getEntriesForRecord(record_id).call()
        entries   = []
        for i in indices:
            rid, actor, evt_type, dh, ts, desc = self.audit_ledger.functions.getEntry(i).call()
            entries.append({
                "index":       i,
                "record_id":   rid.hex(),
                "actor":       actor,
                "event_type":  evt_type,
                "data_hash":   dh.hex(),
                "timestamp":   ts,
                "description": desc,
            })
        return entries


# ── Module-level singleton ────────────────────────────────────────────────────
# Instantiated lazily so tests can mock it before import.
_service: Optional[ChainService] = None

def get_chain_service() -> ChainService:
    global _service
    if _service is None:
        _service = ChainService()
    return _service


