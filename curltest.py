#!/usr/bin/python3

import requests

date="09/25/2020"

url='https://hnd-p-ols.spectrumng.net/WaverleyOaks/Library/OlsService.asmx/GetSchedulerResourceAvailability'
headers={'Content-Type': 'application/json; charset=UTF-8'}
dataBinary='{"siteId":"1803","resourceIds":["7","26","27","8"],"selectedDate":"%s"}' % date
x=requests.post(url, data=dataBinary.encode(), headers=headers)
print(x.text)
