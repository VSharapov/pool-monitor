#!/usr/bin/python3

import smtplib

fromName = 'Вася'
fromAddress = "vasiliy@vas.im"
toAddressList = ["vasiliys@gmail.com"]
subject = "Hello!"
body = "This message was sent with Python's smtplib."
message = """\
From: %s <%s>
To: %s
Subject: %s

%s
""" % (fromName, fromAddress, ", ".join(toAddressList), subject, body)

server = smtplib.SMTP('localhost')
server.sendmail(fromAddress, toAddressList, message.encode('utf-8'))
server.quit()
