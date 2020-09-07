from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Model的M请大写...
class Flight(db.Model):
    #for any table we want inside of our database
    #we're going to have one class inside of this Model file
    #对每一个要用的用数据库里的表，都需要对应建一个类
    __tablename__ = "flights"
    #表名
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    #relationship的概念
    #passenger is not a column of this table
    #just a relationship that can connect multiple tables
    #if I have a flight object, I can use this passenger's property
    #to extract all of the passengers that are on taht particular flight
    # backref: make reverse enable
    passengers = db.relationship("Passenger",backref="Flight",lazy=True)
    

    #add functionality,add featuers to the model
    def add_passenger(self,name):
        p=Passenger(name = name,flight_id = self.id)
        db.session.add(p)
        db.session.commit()
class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    flight_id=db.Column(db.Integer, db.ForeignKey("flights.id"),nullable=False)

#有上面的语法建立的类后，就可以直接用下面的语句直接建所有的表
#db.creat_all()
#见create.py