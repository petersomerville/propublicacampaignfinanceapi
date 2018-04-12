import json, requests
from pprint import pprint

API_BASE = "https://api.propublica.org"
API_KEY = "??????????????????????????????????????????"

ENDPOINT_MEMBERS = "/congress/v1/{}/{}/members.json"
ENDPOINT_HOUSE = "/congress/v1/{}/house/members.json"
ENDPOINT_SENATE = "/congress/v1/{}/senate/members.json"

DEFAULT_HEADER = {"X-API-Key":API_KEY}

def get_data(url):    
    response = requests.get(url, headers=DEFAULT_HEADER)
    return json.loads(response.text)

def get_senate(chamber):
    if 80 <= chamber and chamber <= 115:
        return get_data(API_BASE + ENDPOINT_SENATE.format(chamber)) 
    else:
        return None

def get_house(chamber):
    if 102 <= chamber and chamber <= 115:
        return get_data(API_BASE + ENDPOINT_HOUSE.format(chamber))
    else:
        return None

def get_members(chamber, branch):
    pass

pprint(get_senate(80))