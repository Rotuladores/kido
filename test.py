from hmm import hmm
from smartdictionary import SmartDictionary
import pickle
import os

path = 'training_set/'

sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)
net = hmm()
# training_set = []
# for root, dirs, files in os.walk(path):
#     for file in files:
#         if file.endswith(".txt"):
#              training_set.append(os.path.join(root, file))
training_set = ['training_set/It.txt']

net.train(training_set, sd)

c1, _ = net.build_viterbi(2, 10, 'dan\'t', sd)
c2, _ = net.add_viterbi_layer(2, 10, 'usr')

print(c1)
print(c2)


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

# with open('trained_test.pkl', 'wb') as foutput:
# 	pickle.dump(net, foutput, pickle.HIGHEST_PROTOCOL)

