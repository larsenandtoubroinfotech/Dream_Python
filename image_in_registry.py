#!/usr/bin/python
import json
import requests
def __init__(self):
    return self
def image_search(registry_url, image_name):
    #registry_url = sys.argv[1]
    #image_name = sys.argv[2]
    response_json = json.loads(requests.get(registry_url, verify=False).text)
    if image_name in response_json['repositories']:
        return 'present'
