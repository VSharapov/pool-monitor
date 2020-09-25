#!/usr/bin/python3

import json
import pprint

pp = pprint.pprint

f = open("ignore.json", 'r')
x = json.load(f)
z = x['d']
v = z['Value']
runs = {}
for spot in range(len(v)):
    avList = v[spot]['Availability']
    c = [i for i in avList if i['IsAvailable']]
    #pp((spot, len(c),c[0], c[-1]))
    runs[spot] = []
    for moment in avList:
        newRun = {
                'avail':moment['IsAvailable'],
                'first':moment['TimeId'],
                'last':moment['TimeId']
            }
        if runs[spot] == []:
            runs[spot].append(newRun)
        else:
            if runs[spot][-1]['avail'] == moment['IsAvailable']:
                runs[spot][-1]['last'] = moment['TimeId']
            else:
                runs[spot].append(newRun)

pp(runs)
