import os

from flask import Flask, render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)

#DATABASE_URL="postgresql://postgres:postgres@localhost/postgres"
#engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')

db=scoped_session(sessionmaker(bind=engine))

@app.route("/",methods=["POST","GET"])
def index():
    foodcals=db.execute("select * from Calorie").fetchall()
    return render_template("testindex.html",cals=foodcals)
    
    theone=db.execute("select cal from Calorie where id=:id",{"id":food_id}).fetchone()
    return render_template("testindex.html",name=theone)
