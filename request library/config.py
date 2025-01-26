
base_url = "https://gorest.co.in/"
base_path = "public/"
version = "v2/"
user = "users/"
# if we directly use access token in an variable and use it then it can be visible to other users where we upload script
# to hide that info we can use environment variable which will be limited for our machine
# to create environment variable first import os library
access_token = "d7af99074e4657b68a446f70ca359373d85776d7125bc55048abb64863155785"
headers = dict()
headers["Authorization"] = "Bearer " + access_token


def users():
    return base_url+base_path+version+user


def header():
    return headers
