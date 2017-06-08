from hmm import hmm
from smartdictionary import SmartDictionary
import pickle

sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)
net = hmm()
training_set = ['training_set/It.txt']
net.train(training_set, sd)

# test_prior = ['has', 'was', 'i', 'if', 'but', 'therefore', 'although', 'cat', 'hippopotamus', 'filly', 'bill', 'bull']
# for word in test_prior:
# 	print('{0}: {1}'.format(word, net.get_prior(word)))

# test_transition = [('bill', 'has'), ('said', 'bill'), ('bill', 'said'), ('it', '_s'),
# 					('it', 'is'), ('i', '_will'), ('you', '_are'), ('you', 'are'),
# 					('lobster', 'man'), ('bat', 'man'), ('rain', 'bull')]
# for couple in test_transition:
# 	print('({0} - {1}): {2}'.format(couple[0], couple[1], net.get_transition(couple[0],couple[1])))

phrase_test = ['bill', 'said', 'ot', 'was', 'alt', 'ight']

correct, probability = net.viterbi(1,10,phrase_test, sd, draw=True)

print('Input: \'' + ' '.join(phrase_test) + '\'')

print('Correction: \''+' '.join(correct) + '\'')
print('Probability: ' + str(probability))

# TEST SAVING

# with open('trainted_test.pkl', 'wb') as foutput:
# 	pickle.dump(net, foutput, pickle.HIGHEST_PROTOCOL)

# with open('trainted_test.pkl', 'rb') as finput:
# 	load_net = pickle.load(finput)

# print('-'*30)
# for word in test_prior:
# 	print('{0}: {1}'.format(word, load_net.get_prior(word)))
# for couple in test_transition:
# 	print('({0} - {1}): {2}'.format(couple[0], couple[1], load_net.get_transition(couple[0],couple[1])))
