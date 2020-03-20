from utils import *
import json

def recordsByLevel(records, level):
    records = read_from_json_file(db)    
    newRec  = []
    for r in records:
        if r["level"] == level:
            newRec.append(r)
    return newRec

def averageTimeByLevel(records, level):
    count  = 0
    summ = 0
    for r in records:
        if r["level"] == level:
            count += 1
            summ += r["time"]

    avg = round(summ / count / 1000)
    avgSec = prettify(avg % 60)
    avgMin = prettify(round(avg /60))
    return avgMin+":"+avgSec

def countTotalRecords(records, level):
    count  = 0
    for r in records:
        if r["level"] == level:
            count += 1
    return count

def countRecordsByLevel(records, level):
    count  = 0
    for r in records:
        if r["level"] == level:
            count += 1
    return count
