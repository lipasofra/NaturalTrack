import "./App.css";
import { useState } from "react";
import Searcher from "./components/Searcher";
import icon from "./icon.svg";
import map from "./map.svg";

function App() {
  const [prompt, setPrompt] = useState("ej: incendios en ...");

  const handlePromptChange = (event) => {
    console.log(event.target.value);
    setPrompt(event.target.value);
    console.log(prompt);
  };

  const sendPost = () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: prompt }),
    };
    fetch("http://localhost:5000/predict", requestOptions);
  };

  return (
    <div className="app-container">
      <div
      className="logo-style"
      >
        <div
          id="logo"
          className="icon-style"
        >
          <img
            src={icon}
            alt="equipo1"
            className="icon-icon"
          />
          <h1 style={{ color: "white", margin: "20px 0 0 20px" }}>
            Natural <br></br>Track
          </h1>
        </div>
        <div
          className="main-title"
        >
          <h2
            className="main-h2-title"
            id="main title"
          >
            Natural Disasters Report for Everyone
          </h2>
        </div>
      </div>

      <div
        id="buscador"
        class="container text-center"
        style={{ marginTop: "30px", marginBottom: "-140px" }}
      >
        <h3 style={{ marginBottom: "20px", color: "white" }}>
          ¿Qué deseas Saber?
        </h3>
        <div
          id="lupa y barra"
          className="lupa-barra"
        >
          <Searcher
            prompt={prompt}
            handlePromptChange={handlePromptChange}
            sendPost={sendPost}
          />
        </div>
      </div>
      <div
        id="mapa"
       className="mapa"
      >
        <img
          src={map}
          alt="mapamundi"
          style={{ height: "600px", width: "600px" }}
        />
      </div>
    </div>
  );
}

export default App;
