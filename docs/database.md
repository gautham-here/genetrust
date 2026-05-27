# Database Architecture

# GeneTrust Biological Metadata Infrastructure

---

# Purpose

GeneTrust separates:

1. Biological payload storage
2. Metadata persistence
3. Security monitoring data
4. Governance data
5. Audit information

This separation ensures that sensitive biological information remains protected while still enabling efficient analytics and monitoring.

---

# Core Database Philosophy

GeneTrust follows:

```text
Sensitive Biological Data
        ↓
Encrypted Storage Layer

Metadata
        ↓
Database Layer
```

Raw biological data and metadata are intentionally separated.

---

# Current Database Stack

| Layer              |                    Technology |
| ------------------ | ----------------------------: |
| Database           |           Supabase PostgreSQL |
| Authentication     |                 Supabase Auth |
| Storage References |      Supabase Metadata Tables |
| Security           |            AES-256 Encryption |
| API Access         |                       FastAPI |
| ORM Layer          | Lightweight query abstraction |

---

# Current Storage Architecture

```text
Genome Upload
        ↓
Parse Genome File
        ↓
Extract Features
        ↓
Encrypt Raw Genome
        ↓
Store Encrypted File
        ↓
Store Metadata in Supabase
```

---

# Persistence Flow

Current backend flow:

```text
upload.py
        ↓

storage_service.py
        ↓

encrypt_and_store()
        ↓

register_genome()
        ↓

database/queries.py
        ↓

Supabase
```

---

# Current Genome Storage Model

Raw files are stored locally:

```text
backend/uploads/
```

Encrypted versions:

```text
backend/encrypted_storage/
```

Example:

```text
GTX-45F213.enc
GTX-895A82.enc
GTX-B60A51.enc
```

---

# Why Raw Genome Files Are Not Stored Directly in Database

Biological payloads are large and highly sensitive.

Storing entire genomic payloads inside relational databases creates:

* performance issues
* storage inefficiency
* larger attack surfaces
* difficult access control management

Instead:

```text
Database
      ↓
Stores metadata only

Encrypted storage
      ↓
Stores biological payload
```

---

# Current Genome Metadata Schema

Current logical schema:

```sql
CREATE TABLE genomes (

    id UUID PRIMARY KEY,

    genome_id TEXT UNIQUE,

    filename TEXT,

    genome_length INTEGER,

    gc_content FLOAT,

    risk_level TEXT,

    risk_score INTEGER,

    encrypted_path TEXT,

    owner TEXT,

    created_at TIMESTAMP

);
```

---

# Column Descriptions

| Column         | Description                     |
| -------------- | ------------------------------- |
| id             | Internal unique identifier      |
| genome_id      | Human-readable genome reference |
| filename       | Uploaded file name              |
| genome_length  | Total sequence length           |
| gc_content     | GC percentage                   |
| risk_level     | low / medium / high             |
| risk_score     | Heuristic score                 |
| encrypted_path | Encrypted payload location      |
| owner          | Upload owner                    |
| created_at     | Upload timestamp                |

---

# Example Record

```json
{
   "id":"6fa47d89",

   "genome_id":"GTX-45F213",

   "filename":"sample.fasta",

   "genome_length":102,

   "gc_content":50.98,

   "risk_level":"medium",

   "risk_score":49,

   "encrypted_path":
   "encrypted_storage/GTX-45F213.enc",

   "owner":"researcher",

   "created_at":
   "2026-05-27T14:23:47"
}
```

---

# Audit Schema

GeneTrust stores audit events separately.

Suggested schema:

```sql
CREATE TABLE audit_logs (

    id UUID PRIMARY KEY,

    action TEXT,

    user_id TEXT,

    genome_id TEXT,

    severity TEXT,

    status TEXT,

    metadata JSONB,

    created_at TIMESTAMP

);
```

---

# Example Audit Record

```json
{
   "action":"Genome Upload",

   "user_id":"upload_pipeline",

   "genome_id":"GTX-45F213",

   "severity":"Medium",

   "status":"success",

   "metadata":{
      "risk_score":49
   }
}
```

---

# Threat Monitoring Schema

Threat events should remain independent.

Suggested schema:

```sql
CREATE TABLE threats (

    id UUID PRIMARY KEY,

    genome_id TEXT,

    severity TEXT,

    title TEXT,

    message TEXT,

    status TEXT,

    created_at TIMESTAMP
);
```

---

# Example Threat Event

```json
{
   "genome_id":"GTX-45F213",

   "severity":"medium",

   "title":"Entropy Anomaly",

   "message":"Elevated entropy pattern detected.",

   "status":"active"
}
```

---

# Organization Schema

Future organizational isolation:

```sql
CREATE TABLE organizations (

    id UUID PRIMARY KEY,

    organization_name TEXT,

    organization_type TEXT,

    created_at TIMESTAMP
);
```

---

# User Schema

Authentication support:

```sql
CREATE TABLE users (

    id UUID PRIMARY KEY,

    email TEXT,

    role TEXT,

    organization_id UUID,

    created_at TIMESTAMP
);
```

---

# Current Security Controls

Current database protections:

✓ JWT authentication

✓ RBAC authorization

✓ encrypted genome payloads

✓ audit logging

✓ threat monitoring

✓ metadata isolation

---

# Database Access Flow

```text
User Request
      ↓

JWT Authentication
      ↓

RBAC Validation
      ↓

API Endpoint
      ↓

Database Query
      ↓

Metadata Response
```

---

# Current Runtime Behavior

Observed upload behavior:

```text
Upload
    ↓

Genome encrypted

↓

Metadata persisted

↓

Threat evaluated

↓

Audit logged
```

Example runtime:

```text
HTTP POST /genomes

201 Created

Genome registered:
GTX-45F213
```

---

# Future Database Enhancements

Potential additions:

---

## Vector Databases

Current folders:

```text
backend/vector_db/

├── chroma
└── faiss
```

Future use:

* semantic search
* genomic embeddings
* AI retrieval systems
* similarity detection

---

## Blockchain Audit Layer

Potential uses:

* immutable biological records
* tamper verification
* genomic consent tracking

---

## Graph Database

Potential:

```text
Genome
    ↓
Patient
    ↓
Organization
    ↓
Research Study
```

Useful for:

* lineage tracking
* biological relationship mapping
* governance analysis

---

## Distributed Storage

Potential:

* IPFS
* object storage
* hybrid cloud storage

---

# Conclusion

GeneTrust uses a metadata-centric architecture where:

✓ genomic payloads remain encrypted

✓ metadata remains searchable

✓ audit records remain independent

✓ threat monitoring remains isolated

✓ future scaling remains possible

This architecture minimizes exposure while preserving analytical capability.
