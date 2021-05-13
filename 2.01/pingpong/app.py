from flask import Flask
import os
app = Flask(__name__)
pong = [0]

@app.route('/pingpong')
def index():
    pong[0] += 1
    return f'Ping / Pongs {pong[0]}'

if __name__ == '__main__':
    app.run()
