import os

from flask import Flask, render_template,request,jsonify
from models import *

app = Flask(__name__)

#DATABASE_URL="postgresql://postgres:postgres@localhost/postgres"
#engine = create_engine(os.getenv("DATABASE_URL"))

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#db=scoped_session(sessionmaker(bind=engine))

#lesson4
#做一个book航班的前台，所有航班列表在/flights，点击连接可跳转至详细界面
#涉及数据库postgres,表flights,passengers
#相关文件 /templates/index3.html,layout3.html,Success.html,Error.html,flights.html,flight.html

@app.route("/")
def index():
    #从数据库里取所有航班信息的数据赋值给flights
    #flights=db.execute("select * from flights").fetchall()
    #对比lesson3,改成用models建的类的相关语法
    flights = Flight.query.all()
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
    
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("Error.html",message="No such flight with that id.")
    #db.execute("insert into passengers (name,flight_id) values (:name,:flight_id)",{"name":name,"flight_id":flight_id})
    
    '''
    passenger = Passenger(name=name,flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    '''

    #如果Flight类中添加了add_passenger函数，则上面的语句可以简化如下
    flight.add_passenger(name)
    
    return render_template("Success.html")

@app.route("/flights")
def flights():
    #flights=db.execute("select * from flights").fetchall()
    flights = Flight.query.all()
    #返回html文件
    return render_template("flights.html",flights=flights)

@app.route("/flight/<int:flight_id>")
def flight(flight_id):
    
    #flight=db.execute("select * from flights where id=:id",{"id":flight_id}).fetchone()
    flight=Flight.query.get(flight_id)
    #返回html文件
    #如果没有该航班信息，返回错误页面
    if flight is None:
        return render_template("Error.html",message="Invalid flight number.")

    #如果有信息，把该id的航班flight和相关的passengers传入参数，调用render_template显示处理
    #passengers=db.execute("select * from passengers where flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
    
    #passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    
    #如果加了relationship
    passengers = flight.passengers

    return render_template("flight.html",flight=flight,passengers=passengers)

@app.route("/api/flight/<int:flight_id>")
def flight_api(flight_id):

    #Make flight exits
    flight=Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error":"Invalid flight number."}),422

    #Get all passengers
    passengers = flight.passengers

    names=[]
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin":flight.origin,
        "destination":flight.destination,
        "duration":flight.duration,
        "name":names
    })



 

