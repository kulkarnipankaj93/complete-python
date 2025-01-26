import requests
import config
import post

user = post.end_points
print("user is- ",user)
url = config.users()+user
headers = config.header()
data = dict()
data['name'] = input("updated name: ")
data['email'] = input("Updated email: ")
response = requests.put(url, data=data, headers=headers)

print(response.status_code)
print(response.json())

