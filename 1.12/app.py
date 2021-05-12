import os.path
import requests
from datetime import date
from os import path
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    today = date.today()
    d1 = today.strftime("%d-%m-%y")+'.jpg'
    print(d1)
    if not path.exists(f"static/{d1}"):
        response = requests.get("https://picsum.photos/400")
        file = open(f"static/{d1}.jpg", "wb")
        file.write(response.content)
        file.close()
    
    return render_template('main.html', d1=d1)

if __name__ == '__main__':
    app.run()
