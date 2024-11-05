import styles from "../styles/Temp.module.css";

interface TempProps {
  temperatures: { date: string; temp_status: string }[];
}

export default function Temp({ temperatures }: TempProps) {
  const letter = temperatures[0]?.temp_status;
  const dateObject = new Date(temperatures[0]?.date);
  const date = dateObject.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });
  const time = dateObject.toLocaleTimeString("pt-BR", {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false, // Se quiser usar o formato 24 horas
  });
  console.log(letter);

  const boxShadowColors: { [key: string]: string } = {
    A: "rgba(255, 0, 0, 0.25)",
    B: "rgba(0, 140, 255, 0.25)",
    C: "rgba(0, 255, 0, 0.25)",
  };

  const boxShadowColor = boxShadowColors[letter] || "rgba(128, 128, 128, 0.25)";

  // Definindo as mensagens e cores de texto
  let message = "Estado desconhecido";
  let textColor = "black"; // Cor padrão

  switch (letter) {
    case "A":
      message = "Quente";
      textColor = "red"; // Vermelho para "A"
      break;
    case "B":
      message = "Fria";
      textColor = "blue"; // Azul para "B"
      break;
    case "C":
      message = "Normal";
      textColor = "green"; // Verde para "C"
      break;
    default:
      message = "Estado desconhecido"; // Caso padrão
      textColor = "black"; // Cor padrão
      break;
  }

  return (
    <div
      className={styles.container}
      style={{
        boxShadow: `
          ${boxShadowColor} 10px 30px 150px -12px inset,
          ${boxShadowColor} 0px 10px 56px -15px inset
        `,
      }}
    >
      <div className={styles.box}>
        <h1>{date} - {time}</h1>
        <h1>A temperatura está:</h1>
        <h2 style={{ color: textColor }}>{message}</h2>
      </div>
    </div>
  );
}
