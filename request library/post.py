import requests
import config

url = config.users()
data = dict()
data["name"] = input("Enter name: ")
data["email"] = input("Enter Email: ")
data["status"] = input("active or inactive? ")
data["gender"] = input("male or female? ")

headers = config.header()
r = requests.post(url, data=data, headers=headers)
print(r)
print(r.json())

val = r.json()
val1 = val['id']
end_points = str(val1)


