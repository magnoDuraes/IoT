from flask import Flask, jsonify
from flask_cors import CORS
import random
import threading
from time import sleep

app = Flask(__name__)

CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

def teste():
    lista_teste = []
    while True:
        numero = random.randint(1, 99999)
        numero2 = random.randint(1, 99999)
        sleep(5)
        lista_teste.append((numero, numero2))
        print(f"Novo par de números adicionados: ({numero}, {numero2})") 

if __name__ == '__main__':
    thread = threading.Thread(target=teste)
    thread.daemon = True
    thread.start()
    app.run(debug=True)
