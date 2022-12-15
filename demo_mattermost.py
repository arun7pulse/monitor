import requests
from pprint import pprint

#https://mattermost.com/blog/mattermost-integrations-incoming-webhooks/

baseurrl = "eu-chat-ccv2.seasam.org"
apikey = "eu6o4f5nobnytmarb1m1y89fpr"

# the part where we read the actual temperatures is  replaced by the next line
temperature= 3.14159265358979323846
   
#actual code for sending
headers = {'Content-Type': 'application/json',}
values = '{ "text": "This is test channel and test message '+str(temperature).replace(".",",")+' degrees Celcius"}'
response = requests.post(f'https://{baseurrl}/hooks/{apikey}', headers=headers, data=values) 
print(response)
# https://eu-chat-ccv2.seasam.org/kyma/channels/sre-test

pprint(response.json())