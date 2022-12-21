import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "./index.css";
import { UserContextProvider } from "./context/UserContext";
import { LayoutContextProvider } from "./context/LayoutContext";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <UserContextProvider>
        <LayoutContextProvider>
          <App />
        </LayoutContextProvider>
      </UserContextProvider>
    </BrowserRouter>
  </React.StrictMode>
);
reportWebVitals();
