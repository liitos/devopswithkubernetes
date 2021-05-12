import random
import string
import time
from datetime import datetime, timezone
from flask import Flask
app = Flask(__name__)
result_str = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-', k = 40))

@app.route('/')
def index():
    now = datetime.now()
    fnow = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(f"{fnow}: {result_str}")

    with open("/usr/app/log.txt", "r") as file: 
        row = file.readline()
    return f'{fnow}: {result_str} \nPing / Pongs: {row}'


if __name__ == '__main__':
    app.run()
