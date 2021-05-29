from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

username = os.environ['USER']
password = os.environ['PWD']
host = os.environ['HOST'] 
dbname = os.environ['DBNAME']

app = Flask(__name__)

print(password)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}/{dbname}"
print(app.config["SQLALCHEMY_DATABASE_URI"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import Pings
db.create_all()
db.session.commit()

migrate = Migrate(app, db)

@app.route('/pingpong')
def index():

    count = Pings.query.count()
    count += 1

    ping = Pings(message="pong")
    db.session.add(ping)
    db.session.commit()

    return f'Ping / Pongs {count}'

if __name__ == '__main__':
    app.run()
