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

		# Transition
		self.not_transition = {}
		for key in self.trans_row.keys():
			self.trans_row[key] += N * self.alpha

		for key in self.transition.keys():
			tot = self.trans_row[key[0]]
			self.transition[key] /= tot
			self.not_transition[key] = self.alpha / tot

		self.not_not_transition = 1 / N
		self.N = N

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
			self.prior[word] = 1

	def increment_trans_row(self, word):
		try:
			self.trans_row[word] += 1
		except KeyError:
			self.trans_row[word] = 1

	def increment_transition(self, word1, word2):
		try:
			self.transition[word1, word2] += 1
		except KeyError:
			self.transition[word1, word2] = 1

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

	def viterbi(self, max_edit, search_edit, sequence, smart_dictionary, draw=False):
		if not self.trained:
			raise Exception('HMM not trained')

		# offset = 0
		##### Missing observations
		import numpy as np
		self.perturbation = np.loadtxt('matrice.txt',delimiter=',')

		prob = np.zeros((search_edit, len(sequence)))
		path = np.zeros((search_edit, len(sequence)))

		word_edit = {}
		for w in sequence:
			word_edit[w] = smart_dictionary.edit_search(w, max_edit)[:search_edit]
		word_edit = self.check_word_edit(word_edit, search_edit)

		# Prior
		for i in range(search_edit):
			prob[i,0] = np.log(self.get_prior(word_edit[sequence[0]][i])) + np.log(self.calculate_observation(sequence[0], word_edit[sequence[0]][i]))
			path[i,0] = i
		# Dynamic
		for j in range(1, len(sequence)):
			for i in range(search_edit):
				r = [prob[k, j-1] + np.log(self.get_transition(word_edit[sequence[j-1]][k], word_edit[sequence[j]][i]))
					+ np.log(self.calculate_observation(sequence[j], word_edit[sequence[j]][i])) for k in range(search_edit)]

				m = max(r)
				p = np.argmax(r)
				prob[i, j] = m
				path[i, j] = p

		# Draw net
		if draw:
			import pydot
			from PIL import Image

			draw = pydot.Dot(graph_type='digraph', rankdir="LR")

			for i in range(1, len(sequence)):
				for current in word_edit[sequence[i]]:
					for parent in word_edit[sequence[i-1]]:
						edge = pydot.Edge(parent, current)
						draw.add_edge(edge)

			draw.write_png('draw.png')
			image = Image.open('draw.png')
			image.show()

		fpath = [0] * len(sequence)
		m = max(prob[:,len(sequence)-1])
		p = np.argmax(prob[:,len(sequence)-1])
		fpath[len(sequence)-1] = p
		final = [word_edit[sequence[len(sequence)-1]][p]]

		for i in range(len(sequence)-2, -1, -1):
			fpath[i] = int(path[fpath[i+1], i+1])
			final.insert(0, word_edit[sequence[i]][fpath[i]])
			m += prob[fpath[i+1], i+1]

		return (final, np.exp(m))

	@staticmethod
	def check_word_edit(word_edit, N):
		for key in word_edit.keys():
			k = len(word_edit[key])
			if k < N:
				for i in range(N-k):
					word_edit[key].append(word_edit[key][k-1])
		return word_edit


	def calculate_observation(self, obs, real):
		from Bio import pairwise2

		#print(obs + ' ' + real)

		align = pairwise2.align.globalxx(real, obs)[0]
		areal = align[0]
		aobs = align[1]

		ret = 1
		for c in range(0,len(aobs)):
			ret *= self.perturbation[self.get_index(aobs[c]), self.get_index(areal[c])]
		return ret

	@staticmethod
	def get_index(c):
		if c == '-':
			return 26
		else:
			return ord(c) - 97


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
