#!/usr/bin/env python3
import pickle
dictionary = {}

f = open('adj', 'r')
for l in f:
	dictionary[str(l[:-1])] = 'adj'
f.close()

f = open('adv', 'r')
for l in f:
	dictionary[str(l[:-1])] = 'adv'
f.close()

f = open('noun', 'r')
for l in f:
	dictionary[str(l[:-1])] = 'noun'
f.close()

f = open('verb', 'r')
for l in f:
	dictionary[str(l[:-1])] = 'verb'
f.close()

with open('wordnet3.pkl', 'wb') as fo:
	pickle.dump(dictionary, fo, pickle.HIGHEST_PROTOCOL)
# dictionary