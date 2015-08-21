#!/usr/bin/python3.4
import requests

if __name__ == '__main__':
    print('hello world')
    s = requests.session()
    response = s.get('https//:slack.com/', verify=True)
    print(response)
    """
    payload = {"type": "login",
               "email": cfg["email"]}

    s.get('https:slack.com/signin')
    """
