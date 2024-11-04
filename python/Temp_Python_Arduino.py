import serial
import smtplib
import email.message
import time

def enviar_email1():
    corpo_email = """
    <p>Olá</p>
    <p>Verde</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'pythonteste9@gmail.com'
    msg['To'] = 'pythonteste9@gmail.com'
    password = 'hmfb dnvy yeqc gnic'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def enviar_email2():
    corpo_email = """
    <p>Olá</p>
    <p>Vernelho</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'pythonteste9@gmail.com'
    msg['To'] = 'pythonteste9@gmail.com'
    password = 'hmfb dnvy yeqc gnic'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def enviar_email3():
    corpo_email = """
    <p>Olá</p>
    <p>PAmarelo</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'pythonteste9@gmail.com'
    msg['To'] = 'pythonteste9@gmail.com'
    password = 'hmfb dnvy yeqc gnic'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


try:
    
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2) 

    
    last_letter = None

    
    while True:
        if arduino.in_waiting > 0:  # Verifica se há dados para ler
            # Lê a entrada, decodifica e remove espaços em branco
            letter = arduino.readline().decode('utf-8').strip()

            # Verifica se a letra recebida é diferente da última letra
            if letter != last_letter:
                print(f'Letra mudou para: {letter}')
                
                # Executa a ação com base na nova letra
                if letter == "A":
                    print("Executando ação para A")
                    enviar_email1()
                    last_letter = letter

                elif letter == "B":
                    print("Executando ação para B")
                    enviar_email2()
                    last_letter = letter

                elif letter == "C":
                    print("Executando ação para C")
                    enviar_email3()
                    last_letter = letter


except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Fecha a porta serial com segurança
    try:
        arduino.close()
    except:
        pass
