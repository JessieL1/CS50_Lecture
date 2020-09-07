import os

from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
#配置数据库信息
DATABASE_URL='postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/lecture4'
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#tie thw database with the flask application
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

     