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
'''
I am using command to get the info on every page of the results. Sorting by page is one 
of the arguments needed when searching for tourney info. If I want to get all of the 
information I have to sort through all of the pages. 

From what I understand 10 pages is no the max limit. It is just a random limit that was selected.
'''
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


'''
Some background information: Startgg has the tournamnet pages and in those pages are the individual events. 
That is what I need in order to get player placements.

With that being stated, This command is going to go through and find the slug names of the events.
When using these commands to find info about anything it is required to use the slug name.
'''
for tourney in haysTournaments:
    events = smash.tournament_show_events(tourney['slug'])
    tourney['events'] = events

    '''
    This for loop is going to go through all of the events for all of the tourneys that are in the 
    list and get the results of those events.
    
    If the event has not happened yet or been finished it will just put an empty value in the results section.
    '''
    for event in tourney['events']:
        results = smash.tournament_show_lightweight_results(tourney['slug'],event['slug'], 1)
        event['results'] = results

'''
This print statement was just implemented to be sure That everything is working correctly. More than likely this 
print statement will not be in the final version.
'''
pprint.pprint(haysTournaments)