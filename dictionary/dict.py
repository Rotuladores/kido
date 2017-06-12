#!/usr/bin/env python3
import pickle

dictionary = {}

smart_dict = []

word_len = {}

for i in range(32):
	word_len[i] = 0
index = 0
for path in ['wordsEn.txt', 'names.txt', 'bigrams.txt']:
	f = open(path, 'r')
	for l in f:
		word = str(l[:-1]).lower()
		if not word in smart_dict:
				smart_dict.append(word)
				dictionary[word] = path
		print(index)
		index +=1


	f.close()

# with open('wordnet3.pkl', 'wb') as fo:
# 	pickle.dump(dictionary, fo, pickle.HIGHEST_PROTOCOL)

alpha = sorted(smart_dict)

supersmart = sorted(alpha, key=len)

actual_len = 1
i = 0
for w in supersmart:
	if len(w) != actual_len:
		word_len[len(w)] = i
		actual_len = len(w)
	i+=1

with open('smart_wordsen_bigram.dat', 'w+') as fo:
	fo.write('#32\n')
	len_line = '#'
	for k in range(32):
		len_line += str(word_len[k]) + ' '
	fo.write(len_line + '\n')
	for w in supersmart:
		fo.write(w + '\n')
