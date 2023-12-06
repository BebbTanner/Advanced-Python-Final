'''
The purpose of this program is to create results of a tournament and post them to a website.
This is done by using the start.gg API and a python wrapper called pysmashgg.
'''

import pysmashgg
from config import smash_key
import pprint
import datetime
import json

'''
This is an empty list that will be used to store the tournament info
that I will be grabbing from startgg's site.
'''
haysTournaments = []

smash = pysmashgg.SmashGG(smash_key, True)
for i in range(1, 10):
    '''
    The command on line 24 is sorting all of the tournaments by state.
    It is only finding the tournaments in the state of Kansas.
    '''
    tournaments_by_state = smash.tournament_show_by_state('KS',  i)

    if tournaments_by_state != []:
        '''
        This is further sorting through the tournaments.
        Once it has found all of the tournaments in the state of Kansas,
        it is then looking for all of the tournaments in the city of Hays.
        '''
        for tourney in tournaments_by_state:
            if tourney['city'] == 'Hays':
                '''
                After the program has found those tournaments in Hays, It is adding 
                them to the list that I created at the beginning of the program.
                '''
                haysTournaments.append(tourney)

for tourney in haysTournaments:
    events = smash.tournament_show_events(tourney['slug'])
    tourney['events'] = events

    for event in tourney['events']:
        results = smash.tournament_show_lightweight_results(tourney['slug'],event['slug'], 1)
        event['results'] = results


pprint.pprint(haysTournaments)