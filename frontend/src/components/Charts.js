import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

export default function ChartBlock({ title, labels, values }) {
  const data = {
    labels,
    datasets: [
      {
        label: title,
        data: values,
        backgroundColor: ["#4caf50", "#2196f3", "#ff9800"],
      },
    ],
  };
  return <Bar data={data} />;
}
