from ppds import PPDS, Candidate
from pprint import pprint

ppds = PPDS()

# CANDIDATES IN ARKANSAS
ark_candidates = ppds.db.open().query(Candidate).filter(Candidate.state == '/races/AR.json').all()
pprint('Arkansas candidates for U.S. Senate and House in the 2013-14 election cycle:')
for ark_cand in ark_candidates:
    print('\t -{}'.format(ark_cand.name))