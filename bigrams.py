#!/usr/bin/env python3
import os
from smartdictionary import SmartDictionary

def preprocess(path):
	with open(path, 'r') as file:
		data = file.read().replace('\n', ' ').lower()

	data = data.replace('_', '')
	for c in ['‘','’','’']:
		data = data.replace(c, '\'')

	data = data.replace('\'ll',' _will')
	data = data.replace('\'m',' _am')
	data = data.replace('\'re',' _are')
	data = data.replace('\'ve',' _have')
	data = data.replace('n\'t',' _not')
	data = data.replace('\'s',' _s')
	data = data.replace('\'d',' _d')
	for c in [',','(',')','[',']','"','“',
			'”','-','|','»','«','<','>','—','/']:
		data = data.replace(c,' ')

	for n in ['1','2','3','4','5','6','7','8','9','0']:
		data=data.replace(n,'')

	data = data.replace('\'','')

	for c in ['!','?',';',':']:
		data = data.replace(c,'.')

		return data

fpath = 'training_set/'

sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)

fo = open('bigrams.txt', 'w+')

trains = []

for root, dirs, files in os.walk(fpath):
    for file in files:
        if file.endswith(".txt"):
            trains.append(os.path.join(root, file))

print(trains)

to_save = set()

for train in trains:
	print(train)
	book = preprocess(train)
	phrases = book.split('.')

	for p in phrases:
		words = p.split()
		if len(words) > 1:
			if all(sd.check_existance(w) for w in words):
				for i in range(len(words) - 1):
					to_save.add('{0}+{1}\n'.format(words[i], words[i+1]))

for item in to_save:
	fo.write(item)
fo.close()