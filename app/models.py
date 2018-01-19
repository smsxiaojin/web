# coding :utf8

from app import db
from _datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@127.0.0.1:8000/constact"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.debug = True


class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    email = db.Column(db.String(20), unique=True)
    message = db.Column(db.Text)

    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<User %r>" % self.name