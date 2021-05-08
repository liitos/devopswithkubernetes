from flask import Flask
app = Flask(__name__)
pong = [-1]

@app.route('/pingpong')
def index():
    pong[0] += 1
    return f'pong {pong[0]}'

if __name__ == '__main__':
    app.run()
