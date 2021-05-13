import random
import string
import time
import requests
from datetime import datetime, timezone
from flask import Flask
app = Flask(__name__)
result_str = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-', k = 40))

@app.route('/')
def index():
    now = datetime.now()
    fnow = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(f"{fnow}: {result_str}")
    r = requests.get(url = 'http://pingpong-svc/pingpong')
    rtext = r.text 
    return f'{fnow}: {result_str} \n{rtext}'


if __name__ == '__main__':
    app.run()
