import "./App.css";
import { useState } from "react";
import Searcher from "./components/Searcher";
import icon from "./icon.svg";
import map from "./map.svg";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("ej: incendios en ...");
  const [response, setResponse] = useState(null);
  const data = { query: prompt };
  const [email, setEmail] = useState("ej: email@email.com");

  const handlePromptChange = (event) => {
    console.log(event.target.value);
    setPrompt(event.target.value);
  };

  const handleEmailChange = (event) => {
    console.log(event.target.value);
    setEmail(event.target.value);
  };

  const url_api = "http://127.0.0.1:8000/api/v1.0/disasters/";
  const url_email = "http://127.0.0.1:8000/api/v1.0/disasters/email/";

  const sendPost = async () => {
    try {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: prompt }),
      };

      const response = await fetch(url_api, requestOptions);
      const data = await response.json();

      setResponse(data);
      setResponse(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const sendEmail = async () => {
    try {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email }),
      };

      const response = await fetch(url_email, requestOptions);
      const data2 = await response.json();

      setEmail(data2);
      setEmail(data2);
    } catch (error) {
      console.error("Error:", error);
    }
  };

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
      {!response ? (
        <div id="mapa" className="mapa">
          <img
            src={map}
            alt="mapamundi"
            style={{ height: "600px", width: "600px" }}
          />
        </div>
      ) : (
        <div id="mapa" className="mapa" style={{ marginBottom: "200px" }}>
          <p style={{ marginTop: "200px" }}>{response}</p>
        </div>
      )}

      <div
        id="buscador"
        class="container text-center"
        style={{ marginTop: "-97px", marginBottom: "-67px" }}
      >
        <h5 style={{ marginBottom: "20px", color: "white" }}>
          Ingresa tu correo para recibir notificaciones
        </h5>
        <div id="lupa y barra" className="lupa-barra">
          <Searcher
            prompt={prompt}
            handlePromptChange={handleEmailChange}
            sendPost={sendEmail}
          />
        </div>
      </div>
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
