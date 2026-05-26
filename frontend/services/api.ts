export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function apiFetch<T>(
  path: string,
  init?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, init);
  const data = await response.json().catch(() => null);

  if (!response.ok) {
    const message =
      data?.detail || data?.message || `Request failed with ${response.status}`;
    throw new Error(message);
  }

  return data as T;
}
