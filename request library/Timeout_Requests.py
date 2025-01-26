import requests
from requests.exceptions import Timeout


base_url = "https://gorest.co.in/public/v2/users"
max_tries = 3

for i in range(max_tries):
    try:
        response = requests.get(base_url, timeout=1)
        print(response.text)
    except Timeout as to:
        print("Timeout error")

else:
    print("All tries failed")