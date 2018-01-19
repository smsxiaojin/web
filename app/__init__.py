# coding :utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@127.0.0.1:8000/movie"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SECRET_KEY'] = "ac4958d5-4332-4c41-97e4-49e51f6962c0"
#app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint

# from app.admin import admin as admin_blueprint
app.register_blueprint(home_blueprint)


# app.register_blueprint(admin_blueprint,url_prefix="/admin")
#@app.errorhandler(404)
#def error(error):
 #   return render_template("home/error.html"), 404
