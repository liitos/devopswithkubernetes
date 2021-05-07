import random
import string
import time
from datetime import datetime, timezone
from flask import Flask
app = Flask(__name__)
PORT=3000
result_str = ''

@app.route('/')
def index():
    
    now = datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S.%fZ') 

if __name__ == '__main__':
    app.run(port=PORT)
    result_str = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-', k = 40))
