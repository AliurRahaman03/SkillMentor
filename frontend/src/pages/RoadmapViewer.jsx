import { useState } from "react";
import api from "../api/api";

export default function RoadmapViewer() {
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    setError(null);
    if (!role || role.trim() === "") {
      setError("Please enter a target role before generating.");
      return;
    }

    setLoading(true);
    setResult(null);
    try {
      const profile = { target_role: role, skills: ["Python", "Flask"] };
      console.debug("Sending generate request", { profile });
      const res = await api.post("/ai/generate-roadmap", { user_id: 1, profile });
      console.debug("Generate response", res);

      // Prefer res.data.metadata if present, otherwise fallback to data
      const data = res?.data ?? null;
      if (!data) {
        throw new Error("Empty response from server");
      }

      setResult(data.metadata ?? data);
    } catch (err) {
      console.error("Error generating roadmap:", err);
      const message = err?.response?.data?.message || err.message || "Unknown error";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>AI Roadmap Generator</h2>
      <input
        placeholder="Target Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />
      <button type="button" onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button>

      {error && (
        <div style={{ color: "#b00020", marginTop: "0.5rem" }}>
          Error: {error}
        </div>
      )}

      {result && (
        <pre
          style={{ textAlign: "left", background: "#f4f4f4", padding: "1rem", marginTop: "1rem" }}
        >
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
