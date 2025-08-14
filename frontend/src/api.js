const API_BASE = process.env.REACT_APP_API_BASE;

export async function generateReport(url) {
  const res = await fetch(`${API_BASE}/generate-report`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });
  return await res.json();
}
