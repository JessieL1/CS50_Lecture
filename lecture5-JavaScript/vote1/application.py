
import os
import requests

from flask import Flask, render_template,request,jsonify
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#lesson5
#做一个实时显示投票结果并统计的前台，刷新页面不会冲掉结果
#相关文件 /templates/index.html,index.js

#gloabal variable
votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():   
    return render_template("index.html",votes = votes)
    

@socketio.on("submit vote")
def vote(data):

    selection = data["selection"]
    votes[selection] += 1
    #print("------votes",votes)
    emit("vote totals", votes, broadcast = True)
    #emit("vote totals",{"selection":selection},broadcast = True)
    #emit("announce vote",{"selection":selection},broadcast = True)
    

