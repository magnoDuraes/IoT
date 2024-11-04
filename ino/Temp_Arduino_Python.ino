#include <LiquidCrystal.h>
#include <DHT11.h>

#define AlertaTempBaixa 8
#define AlertaTempAlta 7

LiquidCrystal LCD(12, 11, 5, 4, 3, 2);

int TempBaixa = 28;
int TempAlta = 32;

DHT11 dht11(10);

void setup()
{
  Serial.begin(9600);
  pinMode(AlertaTempBaixa, OUTPUT);
  pinMode(AlertaTempAlta, OUTPUT);

  LCD.begin(16, 2);
  LCD.setCursor(0, 0);
  LCD.print("Temp.:");
  LCD.setCursor(7, 0);
  LCD.print("      C      ");
}

void loop()
{

  int temperature = dht11.readTemperature();
  if (temperature != DHT11::ERROR_CHECKSUM && temperature != DHT11::ERROR_TIMEOUT)
  {
  }
  else
  {
    // se der erro
    Serial.println(DHT11::getErrorString(temperature));
  }

  LCD.setCursor(6, 0);
  LCD.print(temperature);

  if (temperature >= TempAlta)
  {
    digitalWrite(AlertaTempBaixa, LOW);
    digitalWrite(AlertaTempAlta, HIGH);
    Serial.println("A");
  }
  else if (temperature <= TempBaixa)
  {
    digitalWrite(AlertaTempBaixa, HIGH);
    digitalWrite(AlertaTempAlta, LOW);
    Serial.println("B");
  }
  else
  {
    digitalWrite(AlertaTempBaixa, LOW);
    digitalWrite(AlertaTempAlta, LOW);
    Serial.println("C");
  }

  delay(2000);
}
