import time
import requests

from flask import Flask, render_template,request,jsonify


app = Flask(__name__)

#lesson6
#有无限的帖子滚动加载显示
#相关文件 /templates/index.html,index.js

@app.route("/")
def index():   
    return render_template("index.html")
    
@app.route("/posts",methods=["POST"])
def posts():

    #get me some posts

    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9 ))

    #generate listof posts
    data = []
    for i in range(start,end+1):
        data.append(f"Post #{i}")

        time.sleep(1)
    

    return jsonify(data)

 

