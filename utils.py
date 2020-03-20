import json

# log function
def log(message):
    print(message)

# db read
def read_from_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        log("Error while reading from:" + file_name)
        return "err"

# db write
def write_to_json_file(record, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(record, file)
    except:
        log("Error while writing from:" + file_name)
        return "err"   

# Function to insert element to a sorted list
def insert(lst, n): 
    # Searching for the position 
    for i in range(len(lst)): 
        if lst[i]["time"] > n["time"]: 
            i = i-1
            break
    i = i+1
    # Inserting n in the list 
    lst = lst[:i] + [n] + lst[i:]
    return lst

# nicely format time MM / SS
def prettify(x):
        if x < 10:
            x = "0"+str(x)
        else:
            x = str(x)
        return x
