class SmartDictionary():
	SMART_WORDNET3 = 'dictionary/smart_wordnet3.dat'

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

def test():
	d = SmartDictionary(SmartDictionary.SMART_WORDNET3)
	print(d.index('garbage'))
	print(d.index('garbags'))

	print(d.check_existance('garbage'))
	print(d.check_existance('garbags'))


if __name__ == '__main__':
	test()



