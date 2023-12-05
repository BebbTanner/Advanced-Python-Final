import pysmashgg
from config import smash_key
import pprint

#this will import the API key from the config file
#This will allow you to make the call to the website that will grab the LGLS info
smash = pysmashgg.SmashGG(smash_key, True)

#this command will print out active tournements in the state you choose
#tournaments_by_state = smash.tournament_show_by_state('KS',  1)
#pprint.pprint(tournaments_by_state)

#This will print out the list of events for a specfic bracket
#YOU WILL NEED TO KNOW THE SLUG NAME OF THE TOURNEY
events = smash.tournament_show_events('lgls-6-oct-13')
pprint.pprint(events)

#This will print out all of the entrants for lgls 1
#entrants = smash.tournament_show_entrants('lgls-3-sept-22', 'double-elim-bracket', 1)
#pprint.pprint(entrants)

from LGLSData import LGLS_1_Players
for player in LGLS_1_Players:
    pprint.pprint(player['entrantPlayers'][0]['playerTag'])