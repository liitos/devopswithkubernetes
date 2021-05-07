from flask import Flask
app = Flask(__name__)
PORT=5000

@app.route('/')
def index():
    return 'Hello kubeworld'

if __name__ == '__main__':
    app.run(port=PORT)
    print(f"Server started in port {PORT}")
