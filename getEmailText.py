import factGetter as factz

FIRST_EMAIL = 'emails/welcomeEmail.txt'
CAT_FACT_EMAIL = 'emails/catFactEmail.txt'
CANCEL_FACTZ_EMAIL = 'emails/cancelCatFactz.txt'

def get_email(path):
	with open(path, 'r') as email:
		emailText = email.read()

	return emailText

def get_first_email():
	return get_email(FIRST_EMAIL)

def get_cat_fact_email():
	fact = factz.get_random_fact()
	return get_email(CAT_FACT_EMAIL).replace('{0}', fact)

def get_cancel_subscription_email():
	fact = factz.get_random_fact()
	return get_email(CANCEL_FACTZ_EMAIL).replace('{0}', fact)

print get_cat_fact_email()