from pprint import pprint

candidate = {
    'candidate': {
        'id': 'S6WY00068',
        'name': 'BARRASSO, JOHN A',
        'party': 'REP',
        'relative_uri': '/candidates/S6WY00068.json'
        },
    'committee': '/committees/C00436386.json',
    'district': '/races/WY/senate.json',
    'state': '/races/WY.json'
    }

for data in candidate:
    pprint(candidate)