from os import path
from os import remove

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

# create the db file if it doesn't exist
db_file = Config().get_db_file()
if not path.exists(db_file):
    with open(db_file, 'w') as fp:
        pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
api = Api(app)
db = SQLAlchemy(app)
