import React, { useRef } from "react";
import ChartBlock from "./ChartBlock";
import html2pdf from "html2pdf.js";

export default function ReportViewer({ report }) {
  const reportRef = useRef();

  const downloadPDF = () => {
    html2pdf().from(reportRef.current).save("seo_report.pdf");
  };

  return (
    <div ref={reportRef}>
      <h2>SEO Report</h2>
      <ChartBlock
        title="Scores"
        labels={["Performance", "SEO", "Accessibility"]}
        values={[
          report.performance.performance_score * 100,
          report.performance.seo_score * 100,
          report.performance.accessibility_score * 100
        ]}
      />
      <button onClick={downloadPDF}>Download PDF</button>
    </div>
  );
}
