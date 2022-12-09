import csv
import json 
import requests
from pprint import pprint

from serviceability import call_serviceability
from syndicate import call_syndicate

baseurl = "https://www.samsung.com/in/api" 

if __name__ == '__main__':
  responses =[]

  response = call_serviceability() 
  responses.append(response) 
  # print(f"***{response.status_code}*** {response.url}")

  response = call_syndicate()
  responses.append(response)
  [print(f"***{response.status_code}*** {response.url}") for response in responses]

  

