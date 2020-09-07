import os
import csv

#对比lesson3-SQL/import.py
#导入的库有不同，语法配置有不同

from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
#配置数据库信息
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#tie thw database with the flask application
db.init_app(app)



def main():
    #打开要导入的数据文件
    f = open("flights.csv")
    reader = csv.reader(f)
    for ori,dest,dur in reader:
        #对比lesson3-SQL/import.py
        #定义flight表示要插入哪些值
        #执行db.session.add添加数据
        flight = Flight(origin=ori,destination=dest,duration=dur)
        db.session.add(flight)
        print(f"Added flight from {ori} to {dest}, lasting {dur} minitues.")
    db.session.commit()

if __name__ == "__main__":
    #对比lesson3-SQL/import.py
    #增加了with语句
    with app.app_context():
        main()

