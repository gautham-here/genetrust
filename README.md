<div align="center">

```
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗███████╗████████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██████╔╝██║   ██║███████╗   ██║   
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██║   ██║╚════██║   ██║   
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝███████║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝  
```

**The Trust Layer for Biological Intelligence Systems**

AI-Native · Blockchain-Anchored · Privacy-Preserving · Enterprise-Grade

*"Biology is becoming digital. Biological identity cannot be reset.*
*GeneTrust is the infrastructure that protects it."*

</div>

---

## The Problem We're Solving

Every year, millions of genomic sequences are uploaded to cloud platforms, shared across research networks, and processed by AI models — **with almost no privacy infrastructure in place.**

Unlike a password or a credit card number:

| Data Type | If Leaked… | Recovery |
|---|---|---|
| Password | Change it | ✅ Recoverable |
| Credit Card | Cancel it | ✅ Recoverable |
| Genomic Sequence | Reveals ancestry, disease risk, family lineage, biological identity | ❌ **Permanent. Irreversible.** |

Genomic data is the most sensitive category of personal information that has ever existed. Yet today:

- Labs upload raw FASTA files over unsecured channels
- AI models process unencrypted sequences
- There is no tamper-proof audit trail for genomic access
- Re-identification attacks on "anonymized" genomic data succeed routinely
- No on-chain consent or governance mechanism exists

**GeneTrust fixes this.** End to end.

---

## What Is GeneTrust?

GeneTrust is a full-stack **CyberBioSecurity infrastructure platform** that secures the entire lifecycle of genomic data — from the moment a lab sequences a sample, through AI analysis, to final clinical reporting — using:

- 🤖 **Real GenAI** (Gemini 1.5 Flash + Ollama local fallback) for privacy risk analysis
- ⛓️ **Blockchain** (Polygon / EVM smart contracts) for immutable audit trails and consent enforcement
- 🔐 **AES-256 encryption** for every genomic file at rest
- 🧬 **BioPython** genomic parsing with entropy, GC content, and mutation signature detection
- 🏥 **A real lab-to-clinic workflow** modeled on how genomics actually works in healthcare

This is not a demo. Every AI call hits a real model. Every audit event is anchored to a real blockchain.

---

## Live Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       REAL-WORLD LAB SCENARIO                        │
│   Patient Sample → DNA Extraction → NGS Sequencing → FASTA Output   │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         SECURE INGEST LAYER                          │
│   AES-256 Encrypted Upload  →  BioPython Parser  →  SHA-256 Anon.   │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
┌────────────────────────┐   ┌──────────────────────────────────────┐
│   HEURISTIC RISK       │   │           GENAI PIPELINE              │
│   ENGINE               │   │                                       │
│   • GC content         │   │   Gemini 1.5 Flash (primary)         │
│   • Entropy score      │──▶│   Mistral / Llama / Phi (fallback)   │
│   • Mutation signals   │   │   Anonymized features only           │
│   • Marker density     │   │   No raw sequences ever sent to AI   │
│   • CG islands         │   │                                       │
└────────────────────────┘   └─────────────────┬────────────────────┘
                                                │
                                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      BLOCKCHAIN GOVERNANCE LAYER                     │
│                                                                      │
│   GenomeRegistry.sol    →   SHA-256 genome hash anchored on-chain   │
│   AuditLog.sol          →   Every access event, tamper-proof        │
│   GenomicAccessControl  →   RBAC + consent policy on smart contract │
│                                                                      │
│   Network: Polygon Mumbai Testnet (free, fast, EVM-compatible)      │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        GOVERNANCE & OUTPUT                           │
│   Clinician PDF Report  │  Research API  │  GDPR/HIPAA Export       │
│   Real-time Threat Feed │  Webhook Alerts│  Compliance Dashboard    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Real-World Use Case: The Hospital Genomics Lab

> **Scenario:** A patient at a hospital submits a saliva sample for cancer predisposition screening. The sample goes to the lab, gets sequenced, and produces a FASTA file. What happens next is where GeneTrust operates.

**Without GeneTrust:**
The FASTA file is emailed to a researcher, uploaded to an unsecured S3 bucket, run through a public AI API that logs all inputs, and stored in a spreadsheet. No audit trail. No encryption. No consent record.

**With GeneTrust:**

| Step | What Happens |
|---|---|
| **1. Lab Upload** | Lab technician uploads FASTA via encrypted endpoint. File is AES-256 encrypted on arrival. |
| **2. Genome Parsing** | BioPython extracts GC content, sequence length, entropy, mutation signatures. |
| **3. Anonymization** | Raw sequence is SHA-256 hashed. No identifiable data leaves the system. |
| **4. AI Risk Analysis** | Anonymized features sent to Gemini 1.5. Returns: risk level, re-identification probability, compliance warnings, GDPR flags. |
| **5. Blockchain Anchor** | Genome hash + risk score written to `GenomeRegistry.sol` on Polygon. Immutable. Timestamped. |
| **6. Audit Trail** | Every access event written to `AuditLog.sol`. Chain of custody verified cryptographically. |
| **7. Consent Enforcement** | Patient's research / clinical / third-party consent flags enforced via `GenomicAccessControl.sol`. |
| **8. Clinical Report** | Clinician receives structured risk report. No raw genomic data in the report. |
| **9. Compliance Export** | GDPR / HIPAA / GINA-ready audit export available on demand. |

**The patient's biological identity is protected at every step.**

---

## Smart Contracts

Three production-grade Solidity contracts, deployed on Polygon (EVM-compatible, low gas, free testnet):

### `GenomeRegistry.sol`
```
Stores → SHA-256 hash of encrypted genome blob (never raw sequence)
         Risk level, score, GC content, sequence length
         Registrant wallet address + block timestamp
         Per-genome consent flags: research | clinical | third-party

Access control → grantAccess() / revokeAccess() per address
                 expiry timestamps on every grant

Events → GenomeRegistered, AccessGranted, AccessRevoked, ConsentUpdated
```

### `AuditLog.sol`
```
Stores → Every access event: upload, AI analysis, export, login
         Actor wallet, action string, severity, status
         previousHash linkage → cryptographic chain of custody

Verification → verifyChainIntegrity() checks every previousHash link
               Returns false if any entry has been tampered with

Events → AuditEntryCreated (indexed by genomeHash + actor)
```

### `GenomicAccessControl.sol`
```
Roles → ADMIN | RESEARCHER | CLINICIAN | LAB_OPERATOR | PATIENT

Per-genome policy → requiresConsent
                    requiresMultiPartyApproval
                    allowsExternalSharing
                    allowsAIAnalysis
                    dataClassification: public | restricted | confidential | top_secret

Events → RoleGranted, RoleRevoked, AccessPolicySet, AccessRequestLogged
```

---

## AI Pipeline

GeneTrust uses a **privacy-first, tiered AI architecture**. Raw genomic sequences never leave the system.

```
Raw FASTA
    │
    ▼
BioPython Parser ──► Feature Extractor ──► Anonymizer
                                               │
                           SHA-256 genome reference
                           GC content, AT content
                           Entropy score (Shannon H)
                           Mutation count
                           Marker density
                           CG island density
                                               │
                                               ▼
                                  ┌────────────────────┐
                                  │  Gemini 1.5 Flash   │  ◄── Primary
                                  │  (Cloud, FREE)      │
                                  └──────────┬──────────┘
                                             │ fails?
                                             ▼
                                  ┌────────────────────┐
                                  │   Ollama Local      │  ◄── Fallback
                                  │  Mistral / Llama    │       (offline)
                                  └──────────┬──────────┘
                                             │
                                             ▼
                              Structured AI Analysis Output:
                              • Risk level + score (0-100)
                              • Threat indicators
                              • Privacy concerns
                              • Re-identification pathways
                              • GDPR / HIPAA / GINA warnings
                              • Security recommendations
```

**The AI never sees a nucleotide sequence.** It only sees anonymized statistical features. This is privacy-preserving AI by design.

---

## Feature Breakdown

### 🧬 Genomic Processing Engine

| Feature | Description |
|---|---|
| FASTA / FASTQ Parser | BioPython-powered, handles multi-record files |
| GC Content | Standard genomic compositional metric |
| Shannon Entropy | Sequence complexity / identifiability score |
| Mutation Signatures | Repeat pattern detection (AAA, GGGG, ATATAT…) |
| CG Island Analysis | Methylation signature and density scoring |
| Homopolymer Runs | Structural anomaly detection |
| Marker Density | Re-identification exposure estimation |

### 🤖 AI Risk Analysis

| Feature | Description |
|---|---|
| Heuristic Scorer | Weighted multi-feature risk score (0–100) |
| Gemini 1.5 Flash | Full structured risk report from real LLM |
| Offline Fallback | Mistral / Llama / Phi3 via Ollama |
| Privacy-First | Anonymized features only — no raw sequence ever sent |
| Structured Output | Risk level, threats, privacy concerns, compliance flags |

### ⛓️ Blockchain Layer

| Feature | Description |
|---|---|
| GenomeRegistry | On-chain genome hash + consent registry |
| AuditLog | Tamper-proof chain-of-custody event log |
| AccessControl | RBAC + per-genome data policies on-chain |
| Chain Integrity Check | Cryptographic verification of audit trail |
| Polygon Network | EVM-compatible, low gas, free Mumbai testnet |
| Explorer Links | Every tx links to Polygonscan |

### 🔐 Security

| Feature | Description |
|---|---|
| AES-256 Encryption | Every genome encrypted at rest (Fernet/PBKDF2) |
| JWT Auth | Access token with role + expiry |
| RBAC | Admin / Researcher / Clinician / Lab Operator / Patient |
| Rate Limiting | Per-IP request throttling |
| CORS | Configurable origin whitelist |
| Input Validation | Pydantic schemas on every endpoint |

---

## Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Next.js 16 + TailwindCSS | Security dashboard UI |
| **Backend** | FastAPI + Python 3.11 | API server + pipeline orchestration |
| **Bioinformatics** | BioPython | FASTA/FASTQ parsing + feature extraction |
| **AI (Cloud)** | Google Gemini 1.5 Flash | Genomic risk analysis LLM |
| **AI (Local)** | Ollama (Mistral / Llama / Phi3) | Offline AI fallback |
| **Blockchain** | Solidity 0.8.20 + Web3.py | Smart contracts + on-chain audit |
| **Network** | Polygon Mumbai (EVM) | Low-gas, free testnet deployment |
| **Encryption** | AES-256 (Fernet + PBKDF2) | Genomic file encryption at rest |
| **Auth** | JWT + RBAC | Role-based access control |
| **Database** | Supabase (optional) | Persistent storage layer |
| **Contracts** | Hardhat-compatible Solidity | GenomeRegistry, AuditLog, AccessControl |

---

## Repository Structure

```
genetrust/
│
├── contracts/                          # Solidity Smart Contracts
│   ├── GenomeRegistry.sol              # On-chain genome hash registry + consent
│   ├── AuditLog.sol                    # Immutable chain-of-custody audit trail
│   └── GenomicAccessControl.sol        # RBAC + per-genome data policy enforcement
│
├── backend/
│   ├── app/
│   │   ├── main.py                     # FastAPI entrypoint + CORS + middleware
│   │   ├── ai/                         # AI pipeline layer
│   │   │   ├── gemini_client.py        # Google Gemini 1.5 integration
│   │   │   ├── ollama_client.py        # Ollama local model bridge
│   │   │   ├── model_selector.py       # AI backend routing + fallback logic
│   │   │   └── prompt_templates.py     # Structured genomic analysis prompts
│   │   ├── api/                        # API route handlers
│   │   │   ├── upload.py               # Genome upload + full pipeline trigger
│   │   │   ├── genomes.py              # Genome registry endpoints
│   │   │   ├── ai.py                   # Direct AI analysis endpoints
│   │   │   ├── audit.py                # Audit log retrieval
│   │   │   ├── threats.py              # Threat intelligence feed
│   │   │   ├── blockchain.py           # Blockchain status + chain audit logs
│   │   │   └── auth.py                 # JWT login + registration
│   │   ├── blockchain/
│   │   │   └── chain_service.py        # Web3.py contract integration layer
│   │   ├── genomic/
│   │   │   ├── parser.py               # BioPython FASTA/FASTQ parser
│   │   │   ├── feature_extractor.py    # GC, entropy, mutation, marker density
│   │   │   ├── mutation_detector.py    # Repeat patterns, CG islands, homopolymers
│   │   │   └── anonymizer.py           # SHA-256 anonymization before AI
│   │   ├── services/
│   │   │   ├── risk_engine.py          # Heuristic risk scorer (0–100)
│   │   │   ├── ai_gateway.py           # AI orchestration + response parser
│   │   │   ├── audit_service.py        # Off-chain + blockchain audit bridge
│   │   │   ├── threat_engine.py        # Real-time threat detection + alerting
│   │   │   ├── storage_service.py      # Encrypted genome persistence
│   │   │   └── auth_service.py         # User management + JWT issuance
│   │   ├── security/
│   │   │   ├── jwt_handler.py          # Token creation + verification
│   │   │   ├── rbac.py                 # Role-permission matrix
│   │   │   ├── access_control.py       # FastAPI auth dependency
│   │   │   └── policy_engine.py        # Upload + access policy evaluation
│   │   └── utils/
│   │       ├── encryption.py           # AES-256 Fernet encryption
│   │       ├── logger.py               # Structured logging
│   │       └── validators.py           # Pydantic input schemas
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── app/
│   │   ├── dashboard/page.tsx          # Main security operations dashboard
│   │   ├── upload/page.tsx             # Genome upload + live AI results
│   │   ├── audit/page.tsx              # Audit log with chain anchoring status
│   │   ├── risk-analysis/page.tsx      # Risk scoring + AI findings
│   │   ├── blockchain/page.tsx         # On-chain registry + integrity checker
│   │   └── lab/page.tsx                # Lab workflow simulator
│   ├── components/
│   │   ├── Sidebar.tsx                 # Navigation with blockchain status
│   │   ├── Topbar.tsx                  # Live chain connection indicator
│   │   ├── GenomeTable.tsx             # Registry with Polygonscan links
│   │   ├── ThreatPanel.tsx             # Real-time threat feed
│   │   └── ActivityTimeline.tsx        # Audit timeline with chain anchoring
│   └── services/                       # Typed API client layer
│
└── README.md
```

---

## Quickstart

### Prerequisites

- Python 3.11+
- Node.js 18+
- A free [Google AI Studio](https://aistudio.google.com) key (Gemini 1.5 Flash is free)
- MetaMask wallet + free [Polygon Mumbai MATIC](https://faucet.polygon.technology) (for blockchain features)

### 1. Clone

```bash
git clone https://github.com/gautham-here/genetrust.git
cd genetrust
```

### 2. Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env — minimum required:
#   GEMINI_API_KEY=your_key_here
#   AI_BACKEND=gemini

uvicorn app.main:app --reload --port 8000
```

API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000

npm run dev
```

Dashboard: [http://localhost:3000/dashboard](http://localhost:3000/dashboard)

### 4. Blockchain (Optional — enables on-chain anchoring)

```bash
# Deploy contracts to Polygon Mumbai (free testnet)
# Using Remix IDE: paste contracts from /contracts/, compile, deploy
# Or with Hardhat:
npm install --save-dev hardhat
npx hardhat run scripts/deploy.js --network mumbai

# Add to backend/.env:
BLOCKCHAIN_ENABLED=true
WEB3_PROVIDER_URL=https://rpc-mumbai.maticvigil.com
CONTRACT_DEPLOYER_PRIVATE_KEY=your_wallet_key
GENOME_REGISTRY_CONTRACT_ADDRESS=0x...
AUDIT_LOG_CONTRACT_ADDRESS=0x...
```

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload-genome` | Upload FASTA → full AI + blockchain pipeline |
| `GET` | `/genomes` | List all registered genomes |
| `GET` | `/genomes/{id}` | Get genome by ID |
| `POST` | `/ai/analyze` | Direct AI analysis on features |
| `GET` | `/audit/logs` | Retrieve off-chain audit log |
| `GET` | `/threats` | Live threat intelligence feed |
| `GET` | `/blockchain/status` | Blockchain connection health |
| `GET` | `/blockchain/audit-logs` | On-chain audit entries |
| `GET` | `/blockchain/verify-integrity` | Cryptographic chain integrity check |
| `POST` | `/auth/login` | JWT authentication |
| `GET` | `/health` | Full system health including blockchain |

---

## Environment Variables

```bash
# AI
AI_BACKEND=gemini                    # gemini | ollama | local
GEMINI_API_KEY=your_key_here         # Free at aistudio.google.com
GEMINI_MODEL=gemini-1.5-flash

# Blockchain
BLOCKCHAIN_ENABLED=true
WEB3_PROVIDER_URL=https://rpc-mumbai.maticvigil.com
CONTRACT_DEPLOYER_PRIVATE_KEY=...
GENOME_REGISTRY_CONTRACT_ADDRESS=...
AUDIT_LOG_CONTRACT_ADDRESS=...

# Security
JWT_SECRET_KEY=your_64_char_secret
GENOME_ENCRYPTION_KEY=your_32_char_key

# CORS
ALLOWED_ORIGINS=http://localhost:3000
```

---

## Security Model

```
┌─────────────────────────────────────────────────────────┐
│                    PRIVACY GUARANTEE                     │
│                                                          │
│  Raw genomic sequence                                    │
│       │                                                  │
│       ▼                                                  │
│  [AES-256 encrypted] ──► stored in encrypted vault      │
│       │                                                  │
│       ▼                                                  │
│  [SHA-256 anonymized] ──► only hash leaves the system   │
│       │                                                  │
│       ▼                                                  │
│  [Statistical features] ──► sent to AI (no sequence)    │
│       │                                                  │
│       ▼                                                  │
│  [Genome hash] ──► anchored to blockchain                │
│                                                          │
│  Raw sequence NEVER: sent to AI · stored in DB ·        │
│                       written to blockchain              │
└─────────────────────────────────────────────────────────┘
```

**Compliance scope:** GDPR Article 9 (special category biometric data) · HIPAA PHI · GINA (Genetic Information Non-discrimination Act)

---

## Roadmap

```
Phase 1 ✅  Secure Genomic Infrastructure
            AES-256 vault · BioPython parser · RBAC · JWT · Encrypted storage

Phase 2 ✅  AI-Safe Biological Processing
            Gemini integration · Privacy-first pipeline · Offline Ollama fallback
            Heuristic risk engine · Mutation signature detection

Phase 3 ✅  Blockchain Governance
            GenomeRegistry.sol · AuditLog.sol · GenomicAccessControl.sol
            Polygon deployment · Chain integrity verification

Phase 4 🔜  Cross-Organization Trust
            Multi-org genome sharing · Federated consent · DAO governance

Phase 5 🔜  BioCryptographic Systems
            Zero-knowledge genomic proofs · Homomorphic analysis
            Secure multi-party genomic computation
```

---

## What Makes This Different

| Capability | GeneTrust | Traditional Genomic Platform |
|---|---|---|
| AI analysis | Real LLM (Gemini 1.5) | Rule-based or none |
| AI privacy | Anonymized features only | Raw sequence to API |
| Audit trail | Immutable blockchain | Database log (mutable) |
| Consent | Smart contract enforced | Policy document |
| Encryption | AES-256 at rest | S3 bucket (varies) |
| Offline AI | Ollama local fallback | Cloud only |
| Chain integrity | Cryptographic verification | None |
| GDPR compliance | Automated flag detection | Manual |

---

## Team Double Trouble

<div align="center">

| | |
|:---:|:---:|
| **Gautham R** | **Shobhana S** |
| Frontend · UX · System Design | Backend · AI · Blockchain |
| [LinkedIn](https://www.linkedin.com/in/gautham-r2005/) | [LinkedIn](https://www.linkedin.com/in/shobhana-shankar-b28026289/) |

</div>

---

<div align="center">

**Built for the hackathon. Built to last.**

*GeneTrust — Because biological identity deserves the strongest protection ever engineered.*

MIT License

</div>
