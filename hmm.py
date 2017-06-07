class hmm():
	def __init__(self, alpha=0.00001, pi=0.0002):
		self.prior = {}
		self.transition = {}
		self.alpha = alpha
		self.pi = pi
		self.trained = False
		self.trans_row = {}

	def train(self, files, sd):
		for file in files:
			book = self.preprocess(file)
			phrases = book.split('.')

			for p in phrases:
				words = p.split()
				if len(words) > 1:
					if all(sd.check_existance(w) for w in words):
						self.increment_prior(words[0])
						for i in range(len(words) - 1):
							self.increment_transition(words[i], words[i+1])
							self.increment_trans_row(words[i])

		self.normalize(sd.len)
		self.trained = True

	def normalize(self, N):
		# Prior 
		tot = sum(self.prior.values()) + N * self.pi
		for key in self.prior.keys():
			self.prior[key] /= tot
		self.not_prior = self.pi / tot

		self.not_transition = {}
		# Transition
		# for key in [x[0] for x in self.transition.keys()]:
			# tot = sum([self.transition[k] for k in self.transition.keys() if k[0] == key]) + N * self.alpha
			# for k in self.transition.keys():
			# 	if k[0] == key:
			# 		self.transition[k] /= tot
		for key in self.trans_row.keys():
			self.trans_row[key] += N * self.alpha

		for key in self.transition.keys():
			tot = self.trans_row[key[0]]
			self.transition[key] /= tot
			self.not_transition[key] = self.alpha / tot

		self.not_not_transition = 1 / N

	def get_prior(self, word):
		if not self.trained:
			raise Exception('HMM not trained')
		try:
			return self.prior[word]
		except KeyError:
			return self.not_prior

	def get_transition(self, word1, word2):
		if not self.trained:
			raise Exception('HMM not trained')
		try:
			return self.transition[word1, word2]
		except KeyError:
			try:
				return self.not_transition[word1]
			except KeyError:
				return self.not_not_transition


	def increment_prior(self, word):
		try:
			self.prior[word] += 1
		except KeyError:
			self.prior[word] = 1 + self.alpha

	def increment_trans_row(self, word):
		try:
			self.trans_row[word] += 1
		except KeyError:
			self.trans_row[word] = 1 + self.alpha

	def increment_transition(self, word1, word2):
		try:
			self.transition[word1, word2] += 1
		except KeyError:
			self.transition[word1, word2] = 1 + self.alpha

	@staticmethod
	def preprocess(path):
		with open(path, 'r') as file:
			data = file.read().replace('\n', ' ').lower()

		data = data.replace('_', '')
		for c in ['‘','’','’']:
			data = data.replace(c, '\'')

		data = data.replace('\'ll',' _will')
		data = data.replace('\'re',' _are')
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

def test():
	from smartdictionary import SmartDictionary

	net = hmm()
	sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)
	test = ['training_set/it_small.txt']

	net.train(test, sd)

	print(net.prior)
	print(net.transition)

	# present in prior
	print(net.get_prior('but'))
	# absent in prior
	print(net.get_prior('what'))

	# present in transition
	print(net.get_transition('grabbed', 'him'))
	# absent in transition
	print(net.get_transition('it', 'sleep'))
	# absent at all
	print(net.get_transition('ittto', 'sleep'))





if __name__ == '__main__':
	test()