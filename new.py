import requests
import jenkins
import json
import os
from datetime import datetime

username = "pilot"
password = "12345"
jenkins_url = "http://172.31.0.75:8080"


jenkins_url = jenkins_url
job_name = "test"
    
request_url = "{0:s}/job/{1:s}/api/json{2:s}".format(
jenkins_url,
job_name,
"?tree=builds[fullDisplayName,id,number,timestamp]{0,3}"
)

response = requests.get(request_url, auth=(username, password)).json()
print(response)

