'''
The purpose of this program is to create results of a tournamet and post them to a website.
This is done by using the start.gg API and a python wrapper called pysmashgg.
'''

import pysmashgg
from config import smash_key
import pprint
import datetime
import json
from LGLSData import LGLS_1_Players

'''
This is an empty list that will be used to store the tournament info
that I will be grabing from startgg's site.
'''
haysTournaments = []

smash = pysmashgg.SmashGG(smash_key, True)
for i in range(1, 10):
    '''
    
    '''
    tournaments_by_state = smash.tournament_show_by_state('KS',  i)

    if tournaments_by_state != []:
        for tourney in tournaments_by_state:
            if tourney['city'] == 'Hays':
                haysTournaments.append(tourney)

for tourney in haysTournaments:
    events = smash.tournament_show_events(tourney['slug'])
    tourney['events'] = events

    for event in tourney['events']:
        results = smash.tournament_show_lightweight_results(tourney['slug'],event['slug'], 1)
        event['results'] = results


pprint.pprint(haysTournaments)