import json, requests
from pprint import pprint
from pp_entities import Candidate
from base import DbManager

API_BASE = "https://api.propublica.org"
API_KEY = "esfTxmzDJFzCaY4UsKzjyqaDlFPYE4lD5lxqmvz6"

DEFAULT_HEADER = {"X-API-Key":API_KEY}

class PPDS:
    def __init__(self):
        self.db = DbManager()

    def get_json(self, url):
        print('GET\t<{}>'.format(url))
        response = requests.get(url, headers=DEFAULT_HEADER)
        return json.loads(response.text)

    def get_candidates(self, state):
        state_cands_url = 'https://api.propublica.org/campaign-finance/v1/2014/races/{}.json'.format(state)
        results = self.db.open().query(Candidate).filter(Candidate.url == state_cands_url).all()

    def get_person(self, i):
        person_url = 'http://data.coding.kitchen/api/person/{}'.format(i) 
        results = self.db.open().query(Person).filter(Person.url == person_url).all()
        if len(results) == 0:
            json_data = self.get_json(person_url)
            person = Person()
            return results[0]