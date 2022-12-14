import requests
url = "http://172.23.240.1:5011/f1/qualifying/10001"
res = requests.get(url)
res = res.json()

print(res)