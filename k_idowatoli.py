from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.properties import ObjectProperty, StringProperty
import pickle
from hmm import hmm
from smartdictionary import SmartDictionary
import numpy as np
import operator

Config.set('graphics', 'width', '680')
Config.set('graphics', 'height', '170')


class GridLayout(GridLayout):
	label_wid = ObjectProperty()
	text_wid = ObjectProperty()
	b1_wid = ObjectProperty()
	b2_wid = ObjectProperty()
	b3_wid = ObjectProperty()
	with open('trained_test.pkl', 'rb') as finput:
		load_net = pickle.load(finput)
	net = load_net
	sd = SmartDictionary(SmartDictionary.SMART_WORDSEN_BIGRAM)
	previous_len = 0

	def do_action(self):
		self.label_wid.text = self.text_wid.text

	def whitelist_chars(self, text):
		if len(text) > 0:
			if text[-1] == ' ':
				#print('Attivazione')
				self.correct()

	def correct(self):
		global sd
		inserted = self.text_wid.text.split()
		#print(inserted)
		if len(inserted) == 1:
			#print('init ' + str(self.previous_len))
			correct, _ = self.net.build_viterbi(2, 25, inserted[0], self.sd)
			#print(self.net.prob)
			col = self.net.prob[:, -1]
			p = np.argsort(col)
			l = {}
			for i in range(0, len(p)):
				l[' '.join(self.net.reconstruct_viterbi_index(
					p[i])[-2:])] = (col[p[i]], p[i])
			sorted_l = sorted(
				l.items(), key=operator.itemgetter(1), reverse=True)
			correct1_label = self.net.reconstruct_viterbi_index(p[-1])
			correct1 = sorted_l[0][0]
			try:
				correct2 = sorted_l[1][0]
			except:
				correct2 = '-'
			try:
				correct3 = sorted_l[2][0]
			except:
				correct3 = '-'
			#print(correct1_label)
			self.previous_len = 1
			self.label_wid.text = ' '.join(correct1_label)
			self.b1_wid.text = ''.join(correct1)
			self.index_change = []
			self.index_change.append(sorted_l[0][1][1])
			self.b2_wid.text = ''.join(correct2)
			try:
				self.index_change.append(sorted_l[1][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
			self.b3_wid.text = ''.join(correct3)
			try:
				self.index_change.append(sorted_l[2][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
		elif len(inserted) == self.previous_len + 1:
			#print('goz ' + str(self.previous_len))
			self.net.add_viterbi_layer(2, 25, inserted[-1], auto_reconstruct=False)
			# ordino e prendo i 3 max
			#print(self.net.prob)
			col = self.net.prob[:, -1]
			# print(col)
			p = np.argsort(col)
			l = {}
			for i in range(0, len(p)):
				l[' '.join(self.net.reconstruct_viterbi_index(
					p[i])[-2:])] = (col[p[i]], p[i])
			sorted_l = sorted(
				l.items(), key=operator.itemgetter(1), reverse=True)
			# print(self.net.reconstruct_viterbi_index(p[-1]))
			# print(sorted_l)
			# print(sorted_l[2][0])
			correct1_label = self.net.reconstruct_viterbi_index(p[-1])
			#correct2 = self.net.reconstruct_viterbi_index(p[-2])[-2:]
			#correct3 = self.net.reconstruct_viterbi_index(p[-3])[-2:]
			correct1 = sorted_l[0][0]
			try:
				correct2 = sorted_l[1][0]
			except:
				correct2 = '-'
			try:
				correct3 = sorted_l[2][0]
			except:
				correct3 = '-'
			# print(correct1)
			# print(correct2)
			# print(correct3)
			#print(correct1_label)
			self.previous_len += 1
			self.label_wid.text = ' '.join(correct1_label)
			self.b1_wid.text = ''.join(correct1)
			self.index_change = []
			self.index_change.append(sorted_l[0][1][1])
			self.b2_wid.text = ''.join(correct2)
			try:
				self.index_change.append(sorted_l[1][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
			self.b3_wid.text = ''.join(correct3)
			try:
				self.index_change.append(sorted_l[2][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
		elif len(inserted) == self.previous_len:
			if '_' not in self.net.sequence[-1]:
				self.net.sequence = self.net.sequence[:-1] 
				self.net.path = self.net.path[:,:-1]
				self.net.prob = self.net.prob[:,:-1]
			else:
				self.net.sequence = self.net.sequence[:-2]
				self.net.path = self.net.path[:,:-2]
				self.net.prob = self.net.prob[:,:-2]
			self.net.add_viterbi_layer(2, 25, inserted[-1], auto_reconstruct=False)
			# ordino e prendo i 3 max
			#print(self.net.prob)
			col = self.net.prob[:, -1]
			# print(col)
			p = np.argsort(col)
			l = {}
			for i in range(0, len(p)):
				l[' '.join(self.net.reconstruct_viterbi_index(
					p[i])[-2:])] = (col[p[i]], p[i])
			sorted_l = sorted(
				l.items(), key=operator.itemgetter(1), reverse=True)
			# print(self.net.reconstruct_viterbi_index(p[-1]))
			# print(sorted_l)
			# print(sorted_l[2][0])
			correct1_label = self.net.reconstruct_viterbi_index(p[-1])
			#correct2 = self.net.reconstruct_viterbi_index(p[-2])[-2:]
			#correct3 = self.net.reconstruct_viterbi_index(p[-3])[-2:]
			correct1 = sorted_l[0][0]
			try:
				correct2 = sorted_l[1][0]
			except:
				correct2 = '-'
			try:
				correct3 = sorted_l[2][0]
			except:
				correct3 = '-'
			# print(correct1)
			# print(correct2)
			# print(correct3)
			#print(correct1_label)
			#self.previous_len += 1
			self.label_wid.text = ' '.join(correct1_label)
			self.b1_wid.text = ''.join(correct1)
			self.index_change = []
			self.index_change.append(sorted_l[0][1][1])
			self.b2_wid.text = ''.join(correct2)
			try:
				self.index_change.append(sorted_l[1][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
			self.b3_wid.text = ''.join(correct3)
			try:
				self.index_change.append(sorted_l[2][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
			#print('fuu ' + str(self.previous_len))
		else:
			#print('faafaa ' + str(self.previous_len))
			#print(self.net.prob)
			if '_' not in self.net.sequence[-1]:
				self.net.sequence = self.net.sequence[:-1] 
				self.net.path = self.net.path[:,:-1]
				self.net.prob = self.net.prob[:,:-1]
			else:
				self.net.sequence = self.net.sequence[:-2]
				self.net.path = self.net.path[:,:-2]
				self.net.prob = self.net.prob[:,:-2]
			#print('sequenza ' + str(self.net.sequence))
			col = self.net.prob[:, -1]
			# print(col)
			p = np.argsort(col)
			l = {}
			for i in range(0, len(p)):
				l[' '.join(self.net.reconstruct_viterbi_index(
					p[i])[-2:])] = (col[p[i]], p[i])
			sorted_l = sorted(
				l.items(), key=operator.itemgetter(1), reverse=True)

			correct1_label = self.net.reconstruct_viterbi_index(p[-1])
			correct1 = sorted_l[0][0]
			try:
				correct2 = sorted_l[1][0]
			except:
				correct2 = '-'
			try:
				correct3 = sorted_l[2][0]
			except:
				correct3 = '-'

			#print('faafaa: ' + str(correct1_label))
			if self.previous_len > 1:
				if self.previous_len == len(inserted)+1:
					self.previous_len -= 1
				else:
					self.previous_len -= 1 
				if self.previous_len <= 1:
					self.previous_len = -1
			self.label_wid.text = ' '.join(correct1_label)
			self.b1_wid.text = ''.join(correct1)
			self.index_change = []
			self.index_change.append(sorted_l[0][1][1])
			self.b2_wid.text = ''.join(correct2)
			try:
				self.index_change.append(sorted_l[1][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])
			self.b3_wid.text = ''.join(correct3)
			try:
				self.index_change.append(sorted_l[2][1][1])
			except:
				self.index_change.append(sorted_l[0][1][1])

	def change_prob(self, index):
		k = self.index_change[index - 1]
		# print(k)
		# print(self.net.prob)
		for i in range(self.net.prob.shape[0]):
			if i == k:
				self.net.prob[i, self.net.prob.shape[1] - 1] = 1e10
			else:
				self.net.prob[i, self.net.prob.shape[1] - 1] = -1e-40
		self.label_wid.text = ' '.join(self.net.reconstruct_viterbi()[0])
		# print(self.net.prob)


class KidoApp(App):
    def build(self):
        return GridLayout()


prova = KidoApp()
prova.run()
