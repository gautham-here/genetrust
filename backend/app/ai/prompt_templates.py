def build_risk_prompt(data: dict) -> str:
    return f"""You are GeneTrust — an expert AI genomic cybersecurity analyst specializing in privacy risk assessment and biological data governance.

Analyze the following anonymized genomic metadata (NO raw sequences are present):

Genomic Metadata:
{data}

Provide a structured analysis with the following sections:

1. RISK ASSESSMENT
   - Overall genomic privacy risk level (low/medium/high/critical)
   - Numeric risk score (0-100)
   - Primary risk drivers

2. THREAT INDICATORS
   - Specific genomic privacy threats detected
   - Re-identification exposure pathways
   - Data linkage vulnerabilities

3. PRIVACY CONCERNS
   - Ancestry exposure probability
   - Disease predisposition inference risk
   - Biological identity linkage risk

4. SECURITY RECOMMENDATIONS
   - Immediate mitigation actions
   - Governance controls required
   - Encryption and access policies

5. COMPLIANCE WARNINGS
   - GDPR/HIPAA/GINA considerations
   - Data sharing restrictions
   - Retention policy recommendations

Be precise, technical, and actionable. Focus on genomic security infrastructure, not medical diagnosis.
"""


def build_summary_prompt(genome_features: dict, risk_result: dict) -> str:
    return f"""You are a genomic security AI summarizer for GeneTrust.

Given the following genomic analysis results, produce a concise executive summary (3-5 sentences) for a security dashboard.

Genomic Features:
{genome_features}

Risk Analysis:
{risk_result}

Executive Summary:
"""


def build_threat_prompt(access_patterns: dict) -> str:
    return f"""You are a CyberBioSecurity threat intelligence analyst for GeneTrust.

Analyze these genomic access patterns for anomalous behavior:

Access Patterns:
{access_patterns}

Identify:
1. Suspicious access behaviors
2. Potential data exfiltration indicators
3. Brute-force or enumeration attempts
4. Compliance violations

Output format: JSON with keys: threat_level, indicators (list), recommended_actions (list)
"""