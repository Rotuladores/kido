#!/usr/bin/env python3

from tkinter import *
import pickle
from hmm import hmm
from smartdictionary import SmartDictionary
import numpy as np
import operator


class Interface(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.master.title("IDoWaToLi")

		self.master.rowconfigure(1, weight=1)
		self.master.columnconfigure(3, weight=1)
		self.grid(sticky=W+E+N+S)

		self.button1 = Button(self,text = '...', width=50, command=lambda: self.change_prob(1))
		self.button1.grid(row=1,column=1,sticky=W)
		self.button2 = Button(self,text = '...', width=50, command=lambda: self.change_prob(2))
		self.button2.grid(row=2,column=1,sticky=W)
		self.button3 = Button(self,text = '...', width=50, command=lambda: self.change_prob(3))
		self.button3.grid(row=3,column=1,sticky=W)
#		b = Button(text='one',command=lambda: callback(b['text']))
		self.label_co = Label(self, text="Correction")
		self.label_co.grid(row=0, column=0, sticky=W)
		self.label1_correct = Label(self, text="...", width=50)
		self.label1_correct.grid(row=0, column=1, sticky=W)
#		self.label2_correct = Label(self, text="...", width=50)
#		self.label2_correct.grid(row=1, column=1, sticky=W)
#		self.label3_correct = Label(self, text="...", width=50)
#		self.label3_correct.grid(row=2, column=1, sticky=W)

		self.label_in = Label(self, text="Write here:")
		self.label_in.grid(row=2, column=0, sticky=W)
		self.edit_input = Entry(self, width=50)
		self.edit_input.grid(row=4, column=1, sticky=W)


		# Load net
		with open('trained_test.pkl', 'rb') as finput:
			load_net = pickle.load(finput)

		self.net = load_net
		self.sd = SmartDictionary(SmartDictionary.SMART_WORDSEN_BIGRAM)
		self.previous_len = 0
		# self.vitello = []

	def correct(self, event):
		# print(self.vitello)
		inserted = self.edit_input.get().split()
		#print(len(inserted))
		#print(inserted)
		#print(self.previous_len)
		if len(inserted) == 1:
			correct, _ = self.net.build_viterbi(2,25,inserted[0], self.sd)
			#print(correct)
			self.previous_len = 1
			self.button1['text'] = ' '.join(correct)
		elif len(inserted) == self.previous_len + 1:
			self.net.add_viterbi_layer(2,25,inserted[-1], auto_reconstruct=False)
			# ordino e prendo i 3 max
			self.net.prob
			col = self.net.prob[:,-1]
			#print(col)
			p = np.argsort(col)
			l={}
			for i in range (0, len(p)):
				l[' '.join(self.net.reconstruct_viterbi_index(p[i])[-2:])] = (col[p[i]], p[i])
			sorted_l = sorted(l.items(), key=operator.itemgetter(1), reverse=True)
			print(self.net.reconstruct_viterbi_index(p[-1]))
			print(sorted_l)
			print(sorted_l[2][0])
			correct1_label = self.net.reconstruct_viterbi_index(p[-1])
			#correct2 = self.net.reconstruct_viterbi_index(p[-2])[-2:]
			#correct3 = self.net.reconstruct_viterbi_index(p[-3])[-2:]
			correct1 = sorted_l[0][0]
			correct2 = sorted_l[1][0]
			correct3 = sorted_l[2][0]
			#print(correct1)
			#print(correct2)
			#print(correct3)					
			self.previous_len += 1	
			
			self.label1_correct['text'] = ' '.join(correct1_label)
			self.button1['text'] = ''.join(correct1)
			self.index_change = []
			self.index_change.append(sorted_l[0][1][1])
			self.button2['text'] = ''.join(correct2)
			self.index_change.append(sorted_l[1][1][1])
			self.button3['text'] = ''.join(correct3)
			self.index_change.append(sorted_l[2][1][1])
		else:
			return

	def change_prob(self, index):
		k = self.index_change[index-1]
		print(k)
		print(self.net.prob)

		for i in range(self.net.prob.shape[0]):
			if i == k:
				self.net.prob[i, self.net.prob.shape[1]-1] = 1e10
			else:
				self.net.prob[i, self.net.prob.shape[1]-1] = -1e-40
		print(self.net.prob)

		
		# self.vitello.append(previous)
		# else:
		# 	previous_text = self.label_correct['text'].split()
		# 	to_correct = inserted[-3:]
		# 	print(previous_text)
		# 	print(to_correct)
		# 	correct, probability, previous = self.net.viterbi(2,50,to_correct, self.sd, draw=False, prior=self.vitello[-3])
		# 	self.label_correct['text'] = ' '.join(previous_text[:-3] + correct)
		# 	self.vitello.append(previous)



if __name__ == "__main__":
	gui = Interface()
	gui.bind_all("<space>", gui.correct)
	gui.mainloop()
