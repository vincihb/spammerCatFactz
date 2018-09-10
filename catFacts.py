import smtplib
from email.mime.text import MIMEText

basicEmail = open(basicEmail.txt, 'rb')
msg = MIMEText(basicEmail.read())
basicEmail.close()

print(msg);

#catFactz = open(catFactsText.txt

#msg['Subject'] = 'The contents of %s'
#msg['From'] = me
#msg['To'] = you

