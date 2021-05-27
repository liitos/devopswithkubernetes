import os.path
import requests
from datetime import date
import os
from os import path
import json
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

##
username = os.environ['USER']
password = os.environ['PWD']
host = os.environ['HOST']
dbname = os.environ['DBNAME']
##

app = Flask(__name__)
#database = ['do this', 'do that']
service_url = os.environ.get("SERVICE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import Todos
db.create_all()
db.session.commit()

migrate = Migrate(app, db)


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        todotext = request.form.get('todotext')
        if len(todotext) > 140:
            return "Todo too long", 400
        todo = Todos(message=todotext)
        db.session.add(todo)
        db.session.commit()
        #database.append(todotext)
        return redirect(service_url)
    else:
        todos = Todos.query.all()
        r = []
        for t in todos:
            r.append(t.message)
        return jsonify(todos=r), 200

if __name__ == '__main__':
    app.run()
