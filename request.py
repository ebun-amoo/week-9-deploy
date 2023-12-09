import requests

url = 'http://localhost:5000/predict'
res = requests.post(url, json={'text':'Not sure I like this'})
print(res.text)