import random
import string
import time
from datetime import datetime, timezone
from flask import Flask
app = Flask(__name__)
result_str = ''

@app.route('/')
def index():
    with open("/usr/app/log.txt") as file: 
        row = file.readline()
    return row

if __name__ == '__main__':
    app.run()
