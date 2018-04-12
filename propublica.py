import json, requests
from pprint import pprint
from ppds import Candidate

from base import DbManager

API_BASE = "https://api.propublica.org"
API_KEY = "esfTxmzDJFzCaY4UsKzjyqaDlFPYE4lD5lxqmvz6"

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

db = DbManager()

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

db.begin()
for state in states:
    search_url = 'https://api.propublica.org/campaign-finance/v1/2014/races/{}.json'.format(state)
    state_candidates = get_data(search_url)
    for cand in state_candidates['results']:
        candidate = Candidate()
        candidate.parse_candidate(cand)
        cand_data = db.open().query(Candidate).filter(Candidate.fec_id == candidate.fec_id).all()
        if len(cand_data) == 0:
            db.save(candidate)
db.end()