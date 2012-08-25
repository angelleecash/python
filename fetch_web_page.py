# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib,sys,smtplib,poplib,time


smtpServer = "smtp.gmail.com:587"
fromAddress = "chenliangcareer@gmail.com"
toAddress = "chenliangcareer@gmail.com"

msgHead = ['From:chenliangcareer@gmail.com', 'To:chenliangcareer@gmail.com', 'Subject:Nexus 7 being delivered']
msgBody = ['Nexus 7 being delivered']
msg = '\r\n\r\n'.join(['\r\n'.join(msgHead), '\r\n'.join(msgBody)])

def notifyMe():
    s = smtplib.SMTP(smtpServer)
    s.starttls()
    s.login("chenliangcareer@gmail.com", "!lp8ssword!")
    s.sendmail(fromAddress, toAddress, msg)
    s.quit()

while True:
    a=urllib.urlopen("http://www.culexpress.com/CulBill.aspx?wlnum=CUL000078925")
    b=a.read()
    #print b
    b.decode("utf8")
    #print b
    c=b.index("<tbody>")
    #print c
    #print c
    d=b.index("</tbody>")
    #d+=1
    if d != 6099:
        notifyMe()
        break
    else:
        print "not yet"

    time.sleep(5)
