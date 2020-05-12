import requests
import json

url = 'http://0.0.0.0:5000/predict/'


x = [35,'female',35,3,'yes','southwest']


x_json = json.dumps(x)
headers = {'content-type':'application/json',
'Accept-Charset':'UTF-8'}
r = requests.post(url,data=x_json,headers=headers)

print(r,r.text)