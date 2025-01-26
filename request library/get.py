import requests
import config
url = config.users()
response = requests.get(url)
print("status code is -", response.status_code)
print(response.json())            # We can use response.text for text format
                                  # response.content for binary format

