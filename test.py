import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {"job": "retired", "duration": 445, "poutcome": "success"}

result = requests.post(url, json=data).json()
print(result)
