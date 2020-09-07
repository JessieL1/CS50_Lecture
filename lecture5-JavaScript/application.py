import requests

from flask import Flask, render_template,request,jsonify


app = Flask(__name__)

#lesson5
#做一个查询利率的前台，输入货币类型，显示利率
#相关文件 /templates/index.html,index.js

@app.route("/")
def index():   
    return render_template("index.html")
    
@app.route("/convert",methods=["POST"])
def convert():

    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest",params={"access_key":"0b0dcf0836ed45c220563980d18cb19c","base":"USD","symbols":currency})

    if res.status_code !=200:
        return jsonify({"success":False})
    
    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success":False})

    return jsonify({"success":True,"rate":data["rate"][currency]})

 

