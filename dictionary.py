import pickle
class Dictionary():
	dic = {}
	WORD_NET3 = 'dictionary/wordnet3.pkl'

	NOUN = 'noun'
	ADVERB = 'adv'
	ADJECTIVE = 'adj'
	VERB = 'verb'

	

	def __init__(self, file):
		with open(file, 'rb') as f:
			self.dic = pickle.load(f)

	def check_existance(self, word):
		if self.get_class(word)[1]:
			return True
		else:
			return False

	def get_class(self, word):
		word = word.lower()
		try:
			return (word, self.dic[word])
		except:
			return(word, None)

d = Dictionary(Dictionary.WORD_NET3)
print(d.get_class('sElF'))
print(d.check_existance('misspell'))
print(d.check_existance('culo'))