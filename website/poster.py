import requests
API_ENDPOINT = "http://localhost:5000/transactions/new"
data={"sender":"1","recipient":"2","amount":51}
r = requests.post(url = API_ENDPOINT, headers={"content-type":"application/json"}, json = data) 
print(r.text)