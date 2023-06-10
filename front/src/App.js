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
        style={{
          display: "flex",
          alignItems: "center",
        }}
      >
        <div
          id="logo"
          style={{
            display: "flex",
            alignItems: "flex-start",
            justifyContent: "flex-start",
          }}
        >
          <img
            src={icon}
            alt="equipo1"
            style={{
              marginRight: "10px",
              marginTop: "30px",
              height: "100px",
              width: "100px",
            }}
          />
          <h1 style={{ color: "white", margin: "20px 0 0 20px" }}>
            Natural <br></br>Track
          </h1>
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            marginLeft: "40px",
          }}
        >
          <h2
            className=""
            id="main title"
            style={{
              textAlign: "center",
              fontSize: "20px",
              fontStyle: "italic",
              fontWeight: "bold",
              paddingTop: "60px",
              marginBottom: "40px",
              color: "white",
            }}
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
          className="flex"
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
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
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          margin: "30px",
        }}
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
