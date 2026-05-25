def build_risk_prompt(data: dict):

    return f'''
You are an AI genomic cybersecurity analyst.

Analyze the uploaded genomic metadata.

Data:
{data}

Generate:
1. Risk Level
2. Threat Indicators
3. Privacy Concerns
4. Security Recommendations
5. Compliance Warnings
'''