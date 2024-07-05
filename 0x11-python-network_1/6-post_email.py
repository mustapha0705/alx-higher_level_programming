#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    r_dict = r.json()
    print("Your email is: {}".format(r_dict['form']['email']))
