#!/bin/bash

#curl "https://hnd-p-ols.spectrumng.net/WaverleyOaks/Library/OlsService.asmx/GetSchedulerResourceAvailability" \
#  -H "Connection: keep-alive" \
#  -H "Accept: application/json, text/javascript, */*; q=0.01" \
#  -H "X-Requested-With: XMLHttpRequest" \
#  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36" \
#  -H "Content-Type: application/json; charset=UTF-8" \
#  -H "Origin: https://hnd-p-ols.spectrumng.net" \
#  -H "Sec-Fetch-Site: same-origin" \
#  -H "Sec-Fetch-Mode: cors" \
#  -H "Sec-Fetch-Dest: empty" \
#  -H "Referer: https://hnd-p-ols.spectrumng.net/waverleyoaks/Members/Scheduler/BookSchedule.aspx?siteid=1803^&catid=d4447fb0-417f-4b27-8fc6-b5e58aedd9ea^&provid=0^&serviceid=7e4b0386-daf8-4ab4-8b63-0cfc087dc9d8^&d=09/28/2020" \
#  -H "Accept-Language: en-US,en;q=0.9" \
#  -H "Cookie: AspxAutoDetectCookieSupport=1; ASP.NET_SessionId=w4gdxmysks25lynmikg3gipd; IsKioskMode=false; LoginType=Members; .CSIASPXFORMSAUTH=C016A7721669CD8831E0F862069139F92176736042DE55577A21A846A8AFF8C22ADC99C9051336876809A290DC5EFA12DCC9CD2E279E8786DBF3B58276A04E044EB982EAA35D23D25E50DC23AFB8B803CD4E84ABEFAFF441A710E2D8C4F9F092FEEC622857EE705619E05CE8D09E8304D1ED92390D13DE4DC66B157919CEFDD3EC3FAFA8" \
#  --data-binary "^{^\^"siteId^\^":^\^"1803^\^",^\^"resourceIds^\^":^[^\^"7^\^",^\^"26^\^",^\^"27^\^",^\^"8^\^"^],^\^"selectedDate^\^":^\^"09/28/2020^\^"^}" \
#  --compressed

#curl \
#"https://hnd-p-ols.spectrumng.net/WaverleyOaks/Library/OlsService.asmx/GetSiteAvailability" -H \
#"Content-Type: application/json" --data-raw \
#'{"siteId":"1803","selectedDate":"09/26/2020"}'

curl 'https://hnd-p-ols.spectrumng.net/WaverleyOaks/Library/OlsService.asmx/GetSchedulerResourceAvailability' \
  -H 'Content-Type: application/json; charset=UTF-8' \
  --data-binary '{"siteId":"1803","resourceIds":["7","26","27","8"],"selectedDate":"09/25/2020"}'
