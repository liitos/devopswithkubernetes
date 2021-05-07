from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello kubeworld'

if __name__ == '__main__':
    app.run()
    print(f"Server started in port {PORT}")
