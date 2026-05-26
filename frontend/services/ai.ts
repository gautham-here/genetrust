import { apiFetch } from "./api";

export type AiAnalysis = {
  ai_risk_level?: string;
  ai_risk_score?: number;
  ai_summary?: string;
  threat_indicators?: string[];
  privacy_concerns?: string[];
  security_recommendations?: string[];
  compliance_warnings?: string[];
  raw_response?: string;
  ai_backend_used?: string;
  ai_fallback_used?: boolean;
};

export type RiskAnalysis = {
  risk_level?: string;
  risk_score?: number;
  findings?: string[];
  recommendations?: string[];
  ai_analysis?: AiAnalysis;
};

export type ParsedGenome = {
  sequence_length?: number;
  gc_content?: number;
  sequence_preview?: string;
};

export type UploadGenomeResponse = {
  genome_id: string;
  filename: string;
  status: string;
  parsed_data: ParsedGenome[];
  risk_analysis: RiskAnalysis[];
};

export type AnalyzePayload = {
  genome_id?: string;
  features?: Record<string, unknown>;
  context?: string;
};

export type AnalyzeResponse = {
  success: boolean;
  data: {
    analysis: string;
    genome_id?: string;
    ai_backend_used: string;
    fallback_used: boolean;
  };
  message: string;
};

export function uploadGenomeForAi(file: File): Promise<UploadGenomeResponse> {
  const formData = new FormData();
  formData.append("file", file);

  return apiFetch<UploadGenomeResponse>("/upload-genome", {
    method: "POST",
    body: formData,
  });
}

export function analyzeWithAi(payload: AnalyzePayload): Promise<AnalyzeResponse> {
  return apiFetch<AnalyzeResponse>("/ai/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
}
