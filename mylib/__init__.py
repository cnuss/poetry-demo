import requests


def getip():
    return requests.get("https://checkip.amazonaws.com/").text


def whoami():
    return "i am mylib"
