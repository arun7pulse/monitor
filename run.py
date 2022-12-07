import csv
import json 
import requests
from pprint import pprint

baseurl = "https://www.samsung.com/in/api"
list_of_get = []

with open("./url.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=',')
  for row in csvreader:
    if(row[1]=='GET'):
        list_of_get.append(f"{baseurl}{row[0]}")

print(list_of_get)

payload={}
headers = {
  'Cookie': 'ak_bmsc=414F4E9EFBB3B70F3499F2C2134FD1C0~000000000000000000000000000000~YAAQ3jpvPfhkbN+EAQAAF/pA5hIy/Zog43pFZHFIE+NTkwNgYRSA/LV6QGRWfnr8TYp+rF6U3yWrYLyk8FgkXviQxpihqFzIbOD4S8q4qRDsMckQ5L3wK1lWfG+hbYLgdZhbJWxbko8Bqj3O2XTcQ29nEpmj6GTrv67Ph1EuJl0urrxJaZRqUF4+OY/WsIPIre6qW1mlvsOSEVVTUmX/i8vyLM0Pet2hdKYSSnHGWTRZRKmEewW2teV9gIGL6pbdE3IeYHj1Xhi9YQAp4Os78yG2pDOI1UUI7vg+HqjQZxvlwXlZEna7EA0s4ZaMWHAYHrZlMYj7LUdqv55p97nw37MLsOTqcwjLTyFgEcZCi0fkXQM2BbsQyvqEOMLTJg=='
}

for url in list_of_get:
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)