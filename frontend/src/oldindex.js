import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // This is where your main app component is rendered
import './index.css'; // Import global styles (if you want)

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
