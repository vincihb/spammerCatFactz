import smtplib, json
from email.mime.text import MIMEText

def send_first_email():
    with open('basicEmail.txt', 'r') as myfile:
        basicEmail=myfile.read()
    
    print(basicEmail);

def get_preferences():
    with open('preferences.txt', 'r') as prefText:
        preferences = prefText.read()
    
    return json.loads(preferences)

send_first_email();




#catFactz = open(catFactsText.txt

#msg['Subject'] = 'The contents of %s'
#msg['From'] = me
#msg['To'] = you

