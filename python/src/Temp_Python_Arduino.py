import serial
import smtplib
import email.message
from time import sleep
import os
from dotenv import load_dotenv
import json
from datetime import datetime

current_directory = os.getcwd()
load_dotenv(dotenv_path=f"{current_directory}\\.env")

EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_TO = os.getenv('EMAIL_TO')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))

with open(f"{current_directory}\\logs\\temp.json", "r") as file:
    data = json.load(file)
    data = list(data)

def enviar_email(letter: str) -> str:
    corpo_email = ""
    match letter:
        case "A":
            corpo_email = """<p>Olá</p><br><p>Vermelho!</p>"""
        case "B":
            corpo_email = """<p>Olá</p><br><p>Azul!</p>"""
        case "C":
            corpo_email = """<p>Olá</p><br><p>Verde!</p>"""

    msg = email.message.Message()
    msg['Subject'] = "WARNING"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    with smtplib.SMTP(f'{SMTP_SERVER}: {SMTP_PORT}') as s:
        s.starttls()
        s.login(EMAIL_FROM, PASSWORD)
        s.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string().encode('utf-8'))
        print('Email enviado')
        
    with open(f"{current_directory}\\logs\\temp.json", "w") as archive:
        data.insert(0,{"temp_status": letter, "date": str(datetime.now()) })
        if len(data) == 11:
            data.pop()
        json.dump(data, archive, indent=4)
        
    return letter

try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    sleep(2) 
    last_letter = None
    while True:
        if arduino.in_waiting > 0:
            letter = arduino.readline().decode('utf-8').strip()
            if letter != last_letter:
                print(f'Letra mudou para: {letter}')
                last_letter = enviar_email(letter)         
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial: {e}")