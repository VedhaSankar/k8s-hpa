from flask import Flask, render_template
import datetime
from dotenv import load_dotenv
import os
from tasks import stress_cpu

# Importing the library
import psutil

load_dotenv()

PORT = os.environ.get('PORT')

app = Flask(__name__)

@app.route('/')
def start():

    return render_template('index.html')

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result

@app.route('/stress')
def stress():

    # stress the cpu
    result = stress_cpu.delay()

    result = {
        "stress"  : "we are stressing the cpu"
    }

    return result

@app.route('/check-cpu-usage')
def check_cpu_usage():
        
        cpu_usage = psutil.cpu_percent(4)
    
        result = {
            "cpu_usage"  : cpu_usage
        }
        return result


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = PORT)