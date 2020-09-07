import os

#from sqlalchemy import create_engine
#sfrom sqlalchemy.orm import scoped_session,sessionmaker

from flask import Flask, render_template,request
from models import *

#DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost/postgres"
#engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')
#db=scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db=SQLAlchemy(app)
db.init_app(app)

def main():
    #执行SQL语句，取所有信息放入varibles flights
    #flights=db.execute("select origin,destination,duration from flights").fetchall()
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minitues.")

if __name__ == "__main__":
    with app.app_context():
        main()

