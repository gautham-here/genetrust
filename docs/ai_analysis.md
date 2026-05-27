# AI Analysis Architecture

# GeneTrust Hybrid AI Intelligence Layer

---

# Purpose

GeneTrust uses artificial intelligence as an augmentation layer rather than a dependency layer.

The heuristic engine remains the primary risk computation system.

AI provides:

* contextual interpretation
* human-readable summaries
* threat explanation
* recommendation enhancement
* governance assistance

AI does not replace deterministic risk computation.

---

# Core Design Philosophy

Traditional AI-driven genomic systems often follow:

```text
Raw Genome
      ↓
AI Model
      ↓
Risk Prediction
```

GeneTrust instead follows:

```text
Raw Genome
      ↓
Feature Extraction
      ↓
Heuristic Risk Engine
      ↓
AI Interpretation Layer
      ↓
Threat Intelligence Output
```

Advantages:

* explainable outputs
* deterministic risk generation
* reduced AI hallucination
* privacy preservation
* operational reliability

---

# Current AI Workflow

```text
Genome Upload
      ↓
Sequence Parsing
      ↓
Feature Extraction
      ↓
Mutation Signature Analysis
      ↓
Risk Engine
      ↓
Threat Engine
      ↓
AI Gateway
      ↓
AI Summary Generation
```

---

# AI Components in GeneTrust

Current implementation location:

```text
backend/app/ai/
```

Current modules:

```text
ai_router.py

gemini_client.py

llama_client.py

mistral_client.py

local_inference.py

model_selector.py

ollama_client.py

phi_client.py

prompt_templates.py
```

---

# AI Routing System

GeneTrust implements dynamic model routing.

Location:

```text
backend/app/ai/model_selector.py
```

Workflow:

```text
Request
     ↓
Select Preferred Model
     ↓

If available:
     Execute

Else:
     Fallback
```

Current behavior:

```text
Gemini
    ↓

Mistral via Ollama
    ↓

Llama
    ↓

Phi
    ↓

Heuristic fallback
```

---

# Current Cloud AI Layer

Primary model:

```text
Google Gemini
```

Current uses:

* summarize genomic findings
* generate explanations
* generate security observations
* generate recommendations

Example:

Input:

```json
{
 "risk_score":49,
 "entropy":1.92,
 "mutation_count":5
}
```

Output:

```text
Medium privacy exposure risk identified.

Elevated entropy may indicate increased biological complexity.

Recommendation:
Restrict external genomic sharing.
```

---

# Current Offline AI Layer

Supported local models:

```text
Mistral

Llama

Phi
```

Purpose:

* air-gapped deployments
* hospitals
* research labs
* privacy-sensitive environments
* offline execution

Current path:

```text
backend/local_models/
```

---

# Ollama Integration

GeneTrust uses Ollama for local inference.

Workflow:

```text
GeneTrust
      ↓
Ollama API
      ↓
Local Model
      ↓
Generated Output
```

Current endpoint:

```text
http://localhost:11434/api/generate
```

Example runtime logs:

```text
Gemini unavailable

↓

Fallback to Mistral

↓

Local inference executed
```

---

# Prompt Engineering Strategy

Location:

```text
backend/app/ai/prompt_templates.py
```

Prompt templates include:

* biological context
* privacy constraints
* security focus
* governance focus

Example:

```text
Analyze the following genomic feature profile:

Risk Score:49

Entropy:1.92

Mutation Count:5

Provide:

• risk interpretation
• privacy concerns
• recommendations
```

---

# AI Output Structure

Current output object:

```json
{
   "ai_risk_level":"medium",

   "ai_risk_score":49,

   "ai_summary":"...",

   "threat_indicators":[],

   "privacy_concerns":[],

   "security_recommendations":[],

   "compliance_warnings":[],

   "raw_response":""
}
```

---

# AI Failure Handling

AI services are treated as optional.

Current logic:

```text
AI request
      ↓

Cloud model available?

YES → execute

NO ↓

Local model available?

YES → execute

NO ↓

Fallback heuristic response
```

---

# Current Fallback Example

Observed runtime:

```text
Gemini API error:
GEMINI_API_KEY not set

↓

Ollama unavailable

↓

Fallback response generated
```

Fallback output:

```json
{
   "ai_summary":
   "AI analysis unavailable. Using heuristic risk assessment.",

   "ai_backend_used":"fallback",

   "ai_fallback_used":true
}
```

---

# Why AI Is Not the Primary Decision Layer

AI systems may produce:

* hallucinations
* inconsistent outputs
* probabilistic behavior
* difficult-to-audit decisions

GeneTrust therefore keeps:

```text
Risk computation
     =
Deterministic
```

while:

```text
AI
     =
Interpretation layer
```

---

# Privacy Protection Strategy

GeneTrust never sends complete genomic files directly to AI systems.

Current pipeline:

```text
Raw Genome
      ↓
Feature Extraction
      ↓
Anonymization
      ↓
AI Input
```

AI receives:

✓ entropy

✓ mutation count

✓ marker density

✓ risk scores

AI does not receive:

✗ raw DNA sequence

✗ complete FASTA payload

✗ patient identifiers

---

# Advantages of Hybrid AI Architecture

---

## Reliability

System remains operational even when:

* internet unavailable
* API unavailable
* AI models unavailable

---

## Privacy

Sensitive biological data remains local.

---

## Explainability

Risk scores remain deterministic.

---

## Flexibility

Supports:

* cloud deployment
* local deployment
* air-gapped deployment

---

## Scalability

Additional models can be integrated without changing core architecture.

Examples:

* Gemma
* TinyLlama
* Claude
* GPT
* BioBERT
* MedPaLM

---

# Current Limitations

Current MVP:

* AI explanations are general
* no fine-tuned biological model
* no genomic transformer model
* no population-scale learning
* no federated learning

---

# Future Directions

Future AI capabilities may include:

* explainable AI
* genomic foundation models
* federated learning
* biological graph networks
* privacy-preserving inference
* retrieval-augmented biological intelligence
* BioLLM systems

---

# Conclusion

GeneTrust uses AI as a secure interpretation layer rather than a decision layer.

This architecture ensures:

✓ explainability

✓ privacy preservation

✓ reliability

✓ offline capability

✓ deterministic risk computation

AI enhances biological understanding while the heuristic engine remains the trusted computational foundation.
