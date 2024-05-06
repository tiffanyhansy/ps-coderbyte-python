import React, { useState } from "react";
import { createRoot } from "react-dom/client";

const Toggle = () => {
  const [on, setOn] = useState(true);

  return <button onClick={() => setOn(!on)}>{on ? "ON" : "OFF"}</button>;
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<Toggle />);
