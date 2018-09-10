import random

FACTZ_PATH = 'factz/catFacts.txt'
ALL_FACTZ = []
NUMBER_O_FACTZ = 0

def get_random_fact():
	index = random.randint(0, NUMBER_O_FACTZ-1)
	return ALL_FACTZ[index].replace("\n", "")

def get_all_factz():
	global ALL_FACTZ
	global NUMBER_O_FACTZ
	print 'gettin me some FACTZ'
	with open(FACTZ_PATH, 'r') as factzFile:
		ALL_FACTZ = factzFile.readlines()

	NUMBER_O_FACTZ = len(ALL_FACTZ)

get_all_factz()