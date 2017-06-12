import edlib
import numpy as np
class SmartDictionary():
	SMART_WORDNET3 = 'dictionary/smart_wordnet3.dat'
	SMART_WORDSEN = 'dictionary/smart_wordsen.dat'
	SMART_WORDSEN_BIGRAM = 'dictionary/smart_wordsen_bigram.dat'
	def __init__(self, path):
		word_len = []
		smart_dictionary = []
		index_dict = {}
		index = 0
		with open(path, 'r') as f:
			skip = f.readline()
			h = f.readline().strip()[1:].split(' ')
			word_len = list(map(lambda x: int(x), h))
			for l in f:
				smart_dictionary.append(l.strip())
				index_dict[l.strip()] = index
				index += 1
		self.smart_dictionary = smart_dictionary
		self.word_len = word_len
		self.index_dict = index_dict
		self.len = len(smart_dictionary)

	def index(self, word):
		try:
			return self.index_dict[word]
		except:
			return -1

	def check_existance(self, word):
		if self.index(word) != -1:
			return True
		else:
			return False

	def edit_search(self, word, threshold):
		k = len(word)
		k_min = k - threshold
		k_max = k + threshold + 1

		ret = []

		if k_min < 0:
			k_min = 0
		if k_max > len(self.word_len):
			k_max = len(self.word_len)

		search = self.smart_dictionary[self.word_len[k_min] : self.word_len[k_max] -1]

		for s in search:
			lev = edlib.align(word, s)["editDistance"]
			if s != '' and lev <= threshold:
				ret.append((lev, s))

		ret = sorted(ret, key=lambda x: x[0])
		return [x[1] for x in ret]

	# 	matrice = np.loadtxt('matrice.txt',delimiter=',')
	# 	retProb = []
	# 	for r in ret:
	# 	    #print(r)
	# 	    p = self.calculate_observation(r[1],word,matrice)
	# 	    retProb.append((p,r[0],r[1]))
	#
	# 	retProb = sorted(retProb, key=lambda x: x[0], reverse=True)
	# 	#print(retProb)
	# 	return [x[2] for x in retProb]
	#
	# def calculate_observation(self, obs, real, perturbation):
	# 	from Bio import pairwise2
	#
	# 	#print(obs + ' ' + real)
	# 	areal = real
	# 	aobs = obs
	# 	if len(obs) != len(real):
	# 		align = pairwise2.align.globalxx(real, obs)[0]
	# 		areal = align[0]
	# 		aobs = align[1]
	# 	ret = 1
	# 	for c in range(0,len(aobs)):
	# 		ret *= perturbation[self.get_index(aobs[c]), self.get_index(areal[c])]
	# 	return ret
	#
	# #@staticmethod
	# def get_index(self,c):
	# 	if c == '-':
	# 		return 26
	# 	else:
	# 		return ord(c) - 97

def test():
	d = SmartDictionary(SmartDictionary.SMART_WORDNET3)
	print(d.index('garbage'))
	print(d.index('garbags'))

	print(d.check_existance('garbage'))
	print(d.check_existance('garbags'))

    # voglio tutte le parole con distanza massimo k da TEST

	test = 'garbaged'
	edit = d.edit_search(test, 3)
	print(edit)


if __name__ == '__main__':
	test()
