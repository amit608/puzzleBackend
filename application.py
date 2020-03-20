import json
from flask import Flask
from flask import request
from flask_cors import CORS
from analytics import * 
app = Flask(__name__)
CORS(app)

def errRes():
    return app.response_class(response="error reading from file", status=500, mimetype='text/html')

@app.route("/")
def hello():
    log("entry to servers root")
    return "hello, to are not authorized. please exit"

@app.route("/addRecord", methods=['POST'])
def addRecord():
    log("record add request")
    records = read_from_json_file(db)     
    if records == "err":
        return errRes()

    records = insert(records, request.get_json(force = True))
    result = write_to_json_file(records, db)
    if result == "err":
        return errRes()

    return app.response_class(
    response="success",
    status=200,
    mimetype='application/json'
            )

@app.route("/getRecords", methods=['GET'])
def getRecord():
    log("record get request")
    records = read_from_json_file(db)    
    if records == "err":
        return errRes()
    
    level = request.args['level']
    records = recordsByLevel(records, level)
    return app.response_class(
        response=json.dumps(records),
        status=200,
        mimetype='application/json'
    )

@app.route("/countRecords", methods=['GET'])
def countRecords():
    log("count records request")
    records = read_from_json_file(db)
    if records == "err":
        return errRes() 

    level = request.args['level']
    count = countRecordsByLevel(records, level)
    return app.response_class(
        response=str(count),
        status=200,
        mimetype='application/json'
    )

@app.route("/countAllRecords", methods=['GET'])
def countAllRecord():
    log("count all records request")
    records = read_from_json_file(db)
    if records == "err":
        response = errRes()

    count = countTotalRecords(records)
    return app.response_class(
        response=str(count),
        status=200,
        mimetype='application/json'
    )

@app.route("/averageTime", methods=['GET'])
def getRecordsAvg():
    log("record average time request")
    records = read_from_json_file(db)
    if records == "err":
        response = errRes()
   
    level = request.args['level']
    avg = averageTimeByLevel(records, level)
    return app.response_class(
        response=json.dumps(str(avg)),
        status=200,
        mimetype='application/json'
    )

@app.route("/topPlayers", methods=['GET'])
def gettopPlayers():
    log("top players request")
    records = read_from_json_file(db)
    if records == "err":
        response = errRes()
   
    dic = topPlayers(records)
    return app.response_class(
        response=json.dumps(dic),
        status=200,
        mimetype='application/json'
    )






