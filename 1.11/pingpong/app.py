from flask import Flask
import os
app = Flask(__name__)
pong = [-1]

@app.route('/pingpong')
def index():
    if not os.path.exists("/usr/app/log.txt"):
        pong[0] = 0
    else:
        with open("/usr/app/log.txt") as file:
            pong[0] = int(file.readline())
            pong[0] += 1
    with open("/usr/app/log.txt", "w+") as file:
        file.write(str(pong[0]))
    return f'Ping / Pongs {pong[0]}'

if __name__ == '__main__':
    app.run()
