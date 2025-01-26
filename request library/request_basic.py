# First we need to create environment and install library using following steps -
# 1 - Open command prompt --> go to folder where we want to create environment
# 2 - run command "python -m venv demo_env(environment name)" - this will create new environment
# 3 - To activate the environment use command "demo_env(env_name)/Srcipts/activate.bat" - this will activate env
# 4 - To install requests library use command "pip install requests" - this will install latest version of requests
#   - if we want any specific version use command "pip install requests==version number"
# 5 - To check if library is install use command "pip list" - it will list down all libraries installed

# Script to activate environment is present at location - env_name-->Scripts-->activate.bat
# Installed library is present at - env_name--> lib-->site-packages-->requests

# Now the environment is created and library is installed we can use that library by importing it into script as below
# Request library is used to make rest api calls
import requests
import json

# get() - to get response from APi
response = requests.get("https://gorest.co.in/public/v2/posts")
# print(response.json())                                        # to get all data
# we can run the file from command prompt as well

# required data is list of dictionaries so to get specific fields we use for loop as below
res = response.json()
for data in res:
    print(data["user_id"])
    print(data["title"])
