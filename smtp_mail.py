# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
f=open('test.txt','w')
f.write("HELLO  WORLD")
f.close()
import smtplib,getpass,email.encoders,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
uid="mailid" #change this to mail id
passd="password" #change this to password
to="mailid"
msg1=" PFA \n\n\n\n\nThanks,\nsyed"
SMTP_URL = "smtp.gmail.com" #or smtp domain name
msg = MIMEMultipart('alternative')
msg['Subject'] = "TEST"
msg['From'] = uid
msg['To'] = to
p1=MIMEText(msg1,'plain')

filename = "test.txt"

#attachment = MIMEText(f.read())
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(open(filename, 'rb').read())
email.encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(p1)

msg.attach(attachment)
#uid = getpass.getuser()

svr = smtplib.SMTP(SMTP_URL)
svr.ehlo()#for google
svr.starttls()#for google
svr.ehlo()#for google
svr.login(uid,passd)
#msg = "From: " + uid + "\nTo: " + to + "\nSubject: " + subject + "\n" + msg
svr.sendmail(uid, to, msg.as_string())
svr.quit()
