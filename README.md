# sliding puzzle backend

this is the sliding puzzle by Gad Zuaretz and Amit Ronen backend.

## files
1. application.py - main API application interface file
2. analytics.py  - helper functions to analyze the data
3. utils.py - utilities functions
4. db.json - json database that stores all records

## API
1. `addRecord`, POST - add a new record to the database
2. `getRecords` (level=e/m/h), GET - get records by level
3. `countRecords` (level=e/m/h), GET - get the count of records by level
4. `getRecords` (level=e/m/h), GET - get records by level
5. `countAllRecords` , GET - get the count of all records
2. `averageTime` (level=e/m/h), GET - get average time by level
3. `topPlayers`, GET - get number of games played for each user