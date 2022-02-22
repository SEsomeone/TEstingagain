import requests

url = "http://192.168.1.3/spicyx/"
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header:")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("******")

url2 = "http://httpbin.org/heeaders"
rh = requests.get(url2, headers=headers)
print(rh.text)