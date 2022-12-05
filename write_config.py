import json

data = {"jira":{
    "token" : "NDQ2NzcxOTIwMTY1OsL1Nrb3LbsuNcbcN6BLdib9UT2Y",
    "tokenname" : "ask-jira", 
    "url" :""
}, "conf": {"token":"NDA3MjQ3MjY2ODMzOkrm2bw/fQJQnXV40pPtbD6I3L3M", "tokenname":"arun-conf"}}
myJSON = json.dumps(data)

with open("config.json", "w") as jsonfile:
    jsonfile.write(myJSON)
    print("Write successful")