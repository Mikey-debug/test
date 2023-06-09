from curl_cffi.requests import get
r= get("https://animepahe.ru/api?m=search&q=Oshi%20No%20Ko", impersonate="chrome101")
print(r.json())
