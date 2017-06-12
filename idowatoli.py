#!/usr/bin/env python3

from tkinter import *
import pickle
from hmm import hmm
from smartdictionary import SmartDictionary


class Interface(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.master.title("IDoWaToLi")

		self.master.rowconfigure(1, weight=1)
		self.master.columnconfigure(3, weight=1)
		self.grid(sticky=W+E+N+S)

		self.label_co = Label(self, text="Correction")
		self.label_co.grid(row=0, column=0, sticky=W)
		self.label_correct = Label(self, text="...", width=50)
		self.label_correct.grid(row=0, column=1, sticky=W)

		self.label_in = Label(self, text="Write here:")
		self.label_in.grid(row=1, column=0, sticky=W)
		self.edit_input = Entry(self, width=50)
		self.edit_input.grid(row=1, column=1, sticky=W)


		# Load net
		with open('trainted_test.pkl', 'rb') as finput:
			load_net = pickle.load(finput)

		self.net = load_net
		self.sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)
		self.vitello = []

	def correct(self, event):
		# print(self.vitello)
		inserted = self.edit_input.get().split()
		# if len(self.vitello) < 4:
		correct, probability = self.net.viterbi(2,50,inserted, self.sd, draw=False)
		self.label_correct['text'] = ' '.join(correct)
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