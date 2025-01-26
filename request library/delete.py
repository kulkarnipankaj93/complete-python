import requests
import config
import post

user = post.end_points
url = config.users()+user
headers = config.header()

response = requests.delete(url,headers=headers)
print(response.status_code)
print(response)
print(response.text)
