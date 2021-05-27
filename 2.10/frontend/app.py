import os.path
import requests
from datetime import date
from os import path
import json
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
service_url = os.environ.get("SERVICE_URL")
@app.route('/')
def index():
    today = date.today()
    d1 = today.strftime("%d-%m-%y")+'.jpg'
    print(d1)
    if not path.exists(f"static/{d1}"):
        response = requests.get("https://picsum.photos/400")
        file = open(f"static/{d1}", "wb")
        file.write(response.content)
        file.close()
    
    r = requests.get(url = 'http://projekti-be-svc/todos')
    rs = r.json()
    todolist = rs['todos']
    todo_url = service_url + '/todos'
    return render_template('main.html', d1=d1, todos=todolist, todo_url=todo_url)

if __name__ == '__main__':
    app.run()
