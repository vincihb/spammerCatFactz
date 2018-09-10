import json
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

def get_preferences():
    with open('preferences.json', 'r') as prefText:
        preferences = prefText.read()
    return json.loads(preferences)

def sendEmail(emailBody):
    prefs = get_preferences()
    yourEmail = str(prefs['your-email'])
    victimEmail = str(prefs['victim'])
    password = str(prefs['your-password'])

    msg = MIMEMultipart()
    msg['From'] = yourEmail
    msg['To'] = victimEmail
    msg['Subject'] = "Cat Factz! You'll love it"
    msg.attach(MIMEText(emailBody, 'plain'))

    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    server.login(yourEmail, password)
    server.ehlo()
    text = msg.as_string()
    server.sendmail(yourEmail, victimEmail, text)
    
sendEmail("TESTING LIMITS OF MANKIND");
