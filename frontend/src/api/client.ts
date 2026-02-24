import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export interface IngestPayload {
  source_type: string;
  title: string;
  content: string;
  occurred_at?: string | null;
}

export interface SourceDocResponse {
  id: number;
  source_type: string;
  title: string;
  content: string;
  occurred_at: string | null;
  created_at: string;
}

export interface WorkItem {
  id: number;
  category: string;
  problem: string;
  action: string;
  result: string;
  impact_score: number | null;
  evidence_json: Record<string, unknown>;
  created_at: string;
}

export interface ExtractResponse {
  created_count: number;
  task_queued: boolean;
}

const client = axios.create({
  baseURL,
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function ingestText(payload: IngestPayload): Promise<SourceDocResponse> {
  const { data } = await client.post<SourceDocResponse>("/ingest/text", payload);
  return data;
}

export async function listWorkItems(): Promise<WorkItem[]> {
  const { data } = await client.get<WorkItem[]>("/work-items");
  return data;
}

export async function extractWorkItems(): Promise<ExtractResponse> {
  const { data } = await client.post<ExtractResponse>("/work-items/extract");
  return data;
}

export default client;
