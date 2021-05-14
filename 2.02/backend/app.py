import os.path
import requests
from datetime import date
import os
from os import path
import json
from flask import Flask, render_template, redirect, url_for, request, jsonify
app = Flask(__name__)
database = ['do this', 'do that']
service_url = os.environ.get("SERVICE_URL")

@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        todotext = request.form.get('todotext')
        database.append(todotext)
        return redirect(service_url)
    else:
        return jsonify(todos=database), 200

if __name__ == '__main__':
    app.run()
