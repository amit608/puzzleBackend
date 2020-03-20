from utils import *
import json
db = "db.json"

# filter records by level
def recordsByLevel(records, level):
    records = read_from_json_file(db)    
    newRec  = []
    for r in records:
        if r["level"] == level:
            newRec.append(r)
    return newRec

# calc average time by level
def averageTimeByLevel(records, level):
    count  = 0
    summ = 0
    for r in records:
        if r["level"] == level:
            count += 1
            summ += r["time"]
    if count == 0:
        return "N/A"
    avg = round(summ / count / 1000)
    avgSec = prettify(avg % 60)
    avgMin = prettify(round(avg /60))
    return avgMin+":"+avgSec
# count total number of records
def countTotalRecords(records, level):
    count  = 0
    for r in records:
        if r["level"] == level:
            count += 1
    return count

# count number of records per level
def countRecordsByLevel(records, level):
    count  = 0
    for r in records:
        if r["level"] == level:
            count += 1
    return count

# calculate number of games per player
def topPlayers(records):
    d = {} 
    for r in records:
        if r["username"] in d:
            d[r["username"]] += 1
        else:
            d[r["username"]] = 1
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
    