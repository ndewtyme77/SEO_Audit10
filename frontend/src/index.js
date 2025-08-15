import React, { useState } from "react";
import UrlForm from "./components/UrlForm";
import Charts from "./components/Charts";
import api from "./services/api";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (url) => {
    setLoading(true);
    try {
      const res = await api.get("/analyze", { params: { url } });
      setData(res.data);
    } catch (err) {
      console.error(err);
      alert("Failed to fetch SEO data.");
    }
    setLoading(false);
  };

  const handleDownloadPDF = async (url) => {
    try {
      const res = await api.get("/report/pdf", {
        params: { url },
        responseType: "blob"
      });
      const blob = new Blob([res.data], { type: "application/pdf" });
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = "seo_report.pdf";
      link.click();
    } catch (err) {
      console.error(err);
      alert("Failed to download PDF.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>SEO Audit Tool</h1>
      <UrlForm onAnalyze={handleAnalyze} onDownloadPDF={handleDownloadPDF} />
      {loading && <p>Analyzing...</p>}
      {data && <Charts data={data} />}
    </div>
  );
}

export default App;
