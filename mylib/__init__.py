import requests

def getip():
    return requests.get("https://checkip.amazonaws.com/").text
