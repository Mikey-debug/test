import requests

r = requests.get("http://127.0.0.1:5000/pahe/")
print(r.json())
                
