import { useEffect, useState } from "react";
import "./App.css";
import Temp from "./components/Temp";

function App() {
  const [temps, setTemps] = useState([]);

  async function getTemp() {
    try {
      const response = await fetch("http://localhost:4000/temp", {
        method: "GET",
        headers: {
          "Content-type": "application/json",
        },
      });
      if (response.ok) {
        const data = await response.json();
        setTemps(data); // Armazenar os dados de temperatura
      } else {
        throw new Error("Não foi possível obter a temperatura");
      }
    } catch (e) {
      alert(e);
    }
  }

  useEffect(() => {
    getTemp();
    const intervalId = setInterval(() => {
      getTemp();
    }, 5000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <Temp temperatures={temps} /> {/* Passar as temperaturas como prop */}
    </div>
  );
}

export default App;
