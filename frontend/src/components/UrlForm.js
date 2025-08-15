import React, { useState } from "react";

function UrlForm({ onAnalyze, onDownloadPDF }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url) onAnalyze(url);
  };

  const handleDownload = () => {
    if (url) onDownloadPDF(url);
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <input
        type="text"
        placeholder="Enter website URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ padding: "8px", width: "300px" }}
      />
      <button type="submit" style={{ marginLeft: "10px" }}>Analyze</button>
      <button type="button" style={{ marginLeft: "10px" }} onClick={handleDownload}>
        Download PDF
      </button>
    </form>
  );
}

export default UrlForm;
