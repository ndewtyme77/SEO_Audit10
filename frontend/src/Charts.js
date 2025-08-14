import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function Charts({ data }) {
  const chartData = {
    labels: ["Performance", "PageRank", "SEO Issues", "Lighthouse Categories"],
    datasets: [
      {
        label: "SEO Metrics",
        data: [
          data.pagespeed?.lighthouseResult?.categories?.performance?.score * 100 || 0,
          data.pagerank?.response?.[0]?.page_rank_integer || 0,
          data.seo?.length || 0,
          Object.keys(data.lighthouse?.categories || {}).length || 0
        ],
        backgroundColor: ["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"]
      }
    ]
  };

  return (
    <div style={{ width: "600px", margin: "auto" }}>
      <Bar data={chartData} />
    </div>
  );
}

export default Charts;
