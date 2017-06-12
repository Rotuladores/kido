from hmm import hmm
from smartdictionary import SmartDictionary
import pickle
import os

def visit_dir(path):
    l = []
    gen = next(os.walk(path))
    l = l + gen[2]
    l = list(map(lambda x: gen[0][len(os.getcwd())+1:]+x,l))
    for s in gen[1]:
        l = l+visit_dir(path+s+'/')
    return l

path = 'training_set/'

sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)
net = hmm()
training_set = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
             training_set.append(os.path.join(root, file))
# training_set = ['training_set/It.txt',
# 				'training_set/hp1.txt',
# 				'training_set/hp2.txt',
# 				'training_set/hp3.txt',
# 				'training_set/hp4.txt',
# 				'training_set/hp5.txt',
# 				'training_set/hp6.txt',
# 				'training_set/hp7.txt',
# 				'training_set/dune1.txt',
# 				'training_set/dune2.txt',
# 				'training_set/dune3.txt',
# 				'training_set/dune4.txt',
# 				'training_set/dune5.txt',
# 				'training_set/dune6.txt',
# 				'training_set/dune7.txt',
# 				'training_set/dune8.txt']
net.train(training_set, sd)

#print(sd.edit_search('swol', 1))

# test_prior = ['has', 'was', 'i', 'if', 'but', 'therefore', 'although', 'cat', 'hippopotamus', 'filly', 'bill', 'bull']
# for word in test_prior:
# 	print('{0}: {1}'.format(word, net.get_prior(word)))

# test_transition = [('bill', 'has'), ('said', 'bill'), ('bill', 'said'), ('it', '_s'),
# 					('it', 'is'), ('i', '_will'), ('you', '_are'), ('you', 'are'),
# 					('lobster', 'man'), ('bat', 'man'), ('rain', 'bull')]
# for couple in test_transition:
# 	print('({0} - {1}): {2}'.format(couple[0], couple[1], net.get_transition(couple[0],couple[1])))
# while True:
# 	inp = input('Dimmi qualcosa... ')
# 	phrase_test = inp.split()

# 	#phrase_test = ['bill', 'said', 'zt', 'was', 'alt', 'ight']
# 	#phrase_test = ['fpllow','me','if','yu','dlpn\'t','wsnt','to','live']
# 	#phrase_test = ['the','bsall','is','on','the','table']

# 	print('Input: \'' + ' '.join(phrase_test) + '\'')

# 	correct, probability = net.viterbi(2,25,phrase_test, sd, draw=False)

# 	print('Correction: \''+' '.join(correct) + '\'')
# 	print('Probability: ' + str(probability))
# 	print('')

# TEST SAVING

with open('trained_test.pkl', 'wb') as foutput:
	pickle.dump(net, foutput, pickle.HIGHEST_PROTOCOL)

# with open('trainted_test.pkl', 'rb') as finput:
# 	load_net = pickle.load(finput)

# print('-'*30)
# for word in test_prior:
# 	print('{0}: {1}'.format(word, load_net.get_prior(word)))
# for couple in test_transition:
# 	print('({0} - {1}): {2}'.format(couple[0], couple[1], load_net.get_transition(couple[0],couple[1])))
