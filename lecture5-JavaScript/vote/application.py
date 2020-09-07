
import os
import requests

from flask import Flask, render_template,request,jsonify
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


#lesson5
#做一个实时显示投票结果的前台
#相关文件 /templates/index.html,index.js

@app.route("/")
def index():   
    return render_template("index.html")
    

@socketio.on("submit vote")
def vote(data):

    selection = data["selection"]
    emit("announce vote",{"selection":selection},broadcast = True)
    

