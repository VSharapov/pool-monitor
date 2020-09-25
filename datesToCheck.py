#!/usr/bin/python3

import datetime
import pytz
import pprint

pp = pprint.pprint

#a = datetime.datetime(2020, 1, 1)
#b = datetime.timedelta(minutes=405)
#a = a+b
#print(b)

now = datetime.datetime.now()
eastern = pytz.timezone('US/Eastern')
utc = pytz.utc
fmt = '%m/%d/%Y'
utc_dt = utc.localize(now)
loc_dt = utc_dt.astimezone(eastern)
#print(loc_dt.strftime(fmt))
datesToCheck = [loc_dt + datetime.timedelta(days=x) for x in range(4)]
datesToCheck = [x.strftime(fmt) for x in datesToCheck]
pp(datesToCheck)

