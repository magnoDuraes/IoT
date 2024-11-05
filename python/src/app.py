from flask import Flask
from flask_cors import CORS
from getTemp import getTemp
import subprocess
import os

app = Flask(__name__)
current_directory = os.getcwd()
path = f"{current_directory}\\Temp_Python_Arduino.py"
print(f"caminho: {path}")

CORS(app)

@app.route('/temp', methods=['GET'])
def temp():
    try:
        return getTemp()
    except:
        return None

if __name__ == '__main__':
    subprocess.Popen(["python", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    app.run(debug=True, port=4000)