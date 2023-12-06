import pysmashgg
from config import smash_key
import pprint
import datetime
import json
from LGLSData import LGLS_1_Players

haysTournaments = []
#this will import the API key from the config file
#This will allow you to make the call to the website that will grab the LGLS info
smash = pysmashgg.SmashGG(smash_key, True)
for i in range(1, 10):
    #this command will print out active tournements in the state you choose
    tournaments_by_state = smash.tournament_show_by_state('KS',  i)
    #pprint.pprint(tournaments_by_state)

    if tournaments_by_state != []:
        for tourney in tournaments_by_state:
            if tourney['city'] == 'Hays':
                haysTournaments.append(tourney)

#pprint.pprint(haysTournaments)
#print("\n\n\n")

for tourney in haysTournaments:
    events = smash.tournament_show_events(tourney['slug'])
    tourney['events'] = events
    #pprint.pprint(events)

    for event in tourney['events']:
        results = smash.tournament_show_lightweight_results(tourney['slug'],event['slug'], 1)
        event['results'] = results


pprint.pprint(haysTournaments)