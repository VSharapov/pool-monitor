#!/usr/bin/python3

import smtplib

fromAddress = "vasiliy@vas.im"
toAddressList = ["vasiliys@gmail.com"]
subject = "Hello!"
body = "This message was sent with Python's smtplib."
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (fromAddress, ", ".join(toAddressList), subject, body)

server = smtplib.SMTP('localhost')
server.sendmail(fromAddress, toAddressList, message)
server.quit()
