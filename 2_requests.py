# requests is used to get data from url and saved in txt file
import requests

r=requests.get("https://api.github.com/events/monishgowda")
print(r.text)

with open("file.txt","w") as f:
    f.write(r.text)