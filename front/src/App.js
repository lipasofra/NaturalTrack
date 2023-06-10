import "./App.css";
import { useState } from "react";
import Searcher from "./components/Searcher";
import icon from "./icon.svg";
import map from "./map.svg";
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState("ej: incendios en ...");
  const [response, setRespose] = useState(null);

  const handlePromptChange = (event) => {
    console.log(event.target.value);
    setPrompt(event.target.value);
    console.log(prompt);
  };

  const sendPost = async () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: prompt }),
    };
    const response = await axios.post("http://18.217.99.4:8000/api/v1.0/disasters/", requestOptions)

    console.log(response)

      }

  return (
    <div className="app-container">
      <div className="logo-style">
        <div id="logo" className="icon-style">
          <img src={icon} alt="equipo1" className="icon-icon" />
          <h1 style={{ color: "white", margin: "20px 0 0 20px" }}>
            Natural <br></br>Track
          </h1>
        </div>
        <div className="main-title">
          <h2 className="main-h2-title" id="main title">
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
        <div id="lupa y barra" className="lupa-barra">
          <Searcher
            prompt={prompt}
            handlePromptChange={handlePromptChange}
            sendPost={sendPost}
          />
        </div>
      </div>
      {!response ? 
      <div id="mapa" className="mapa">
        <img
          src={map}
          alt="mapamundi"
          style={{ height: "600px", width: "600px" }}
        />
      </div>
      : 
      <div id="mapa" className="mapa">
        <p>{response}</p>
      </div>
  }
      <div id="imagen-reporte" className="embebido">
        <iframe
          title="holi"
          width="90%"
          height="2000"
          frameborder="0"
          src="https://app.hex.tech/2f4305db-d567-4b07-8c33-652d7eb206c5/app/ed7149ad-9ca0-4662-a838-a0ec735ec38b/latest?embedded=true"
        />
      </div>
    </div>
  );
}

export default App;
