import datetime
import os

from flask import Flask, render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)

#DATABASE_URL="postgresql://postgres:postgres@localhost/postgres"
#engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')

db=scoped_session(sessionmaker(bind=engine))
'''
@app.route("/")
def index():
    return "Hello, world!"

@app.route("/jessie")
def Jessie():
    return "Hello, Jessie"

@app.route("/<string:name>")
def user(name):
    #print("测试")
    return f"<h1>Hello, {name}</h1>"


@app.route("/<int:number>")
def page(number):
    return f"\n第{number}页"
'''
'''
@app.route("/")
def index():
    names=['Alice','Bod','Jessie','Sherry']
    return render_template("index.html",Names=names)
'''
'''
@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/more")
def more():
    return render_template("detail.html")

@app.route("/hello",methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html",name=name)
'''
#lesson3
#做一个book航班的前台，所有航班列表在/flights，点击连接可跳转至详细界面
#涉及数据库postgres,表flights,passengers
#相关文件 /templates/index3.html,layout3.html,Success.html,Error.html,flights.html,flight.html

@app.route("/")
def index():
    #从数据库里取所有航班信息的数据赋值给flights
    flights=db.execute("select * from flights").fetchall()
    #返回html文件
    return render_template("index3.html",flights=flights)
    
#TypeError: __init__() got an unexpected keyword argument 'method'
@app.route("/book",methods=["POST"])
def book():
    """book a flight"""
    #从form里获取名字
    name=request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("Error.html",message="Invalid flight number.")
    if db.execute("select * from flights where id=:id",{"id":flight_id}).rowcount==0:
        return render_template("Error.html",message="No such flight with that id.")
    db.execute("insert into passengers (name,flight_id) values (:name,:flight_id)",{"name":name,"flight_id":flight_id})
    db.commit()
    return render_template("Success.html")

@app.route("/flights")
def flights():
    flights=db.execute("select * from flights").fetchall()
    #返回html文件
    return render_template("flights.html",flights=flights)

@app.route("/flight/<int:flight_id>")
def flight(flight_id):
    flight=db.execute("select * from flights where id=:id",{"id":flight_id}).fetchone()
    #返回html文件
    #如果没有该航班信息，返回错误页面
    if flight is None:
        return render_template("Error.html",message="Invalid flight number.")

    #如果有信息，把该id的航班flight和相关的passengers传入参数，调用render_template显示处理
    passengers=db.execute("select * from passengers where flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
    return render_template("flight.html",flight=flight,passengers=passengers)

 

