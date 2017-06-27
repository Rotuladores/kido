#!/usr/bin/env python3

import re
import pickle
import string
import numpy as np
from hmm import hmm
from smartdictionary import SmartDictionary
from edlib import align

def preprocess(path):
    with open(path, 'r') as file:
        data = file.read().replace('\n', ' ').lower()

    data = data.replace('_', '')
    for c in ['‘','’','’']:
        data = data.replace(c, '\'')

    data = data.replace('\'ll',' _will')
    data = data.replace('\'m',' _am')
    data = data.replace('\'re',' _are')
    data = data.replace('\'ve',' _have')
    data = data.replace('n\'t',' _not')
    data = data.replace('\'s',' _s')
    data = data.replace('\'d',' _d')
    for c in [',','(',')','[',']','"','“',
            '-','|','»','«','<','>','—','/']:
        data = data.replace(c,' ')
    data = data.replace('&','and')

    for n in ['1','2','3','4','5','6','7','8','9','0']:
        data=data.replace(n,'')

    data = data.replace('\'','')

    for c in ['!','?',';',':','”']:
        data = data.replace(c,'.')

    return data

with open('trained_test.pkl', 'rb') as finput:
	load_net = pickle.load(finput)

net = load_net
sd = SmartDictionary(SmartDictionary.SMART_WORDSEN_BIGRAM)

book = preprocess('simple_test.txt')
phrases = book.split('.')
right_phrases = list(map(lambda x: x.strip(),phrases))
while right_phrases.count('') > 0:
    right_phrases.remove('')

matrix = np.loadtxt('matrice_9.txt', delimiter=',')

wrong_phrases = [''] * len(right_phrases)
checked_phrases = [''] * len(right_phrases)
# for i in range(10):
#     print(np.random.choice(list(string.ascii_lowercase)+['-'], p=matrix[0,:]))

for i in range(len(right_phrases)):
    print(i)
    print(right_phrases[i])

    preproc = right_phrases[i].split(' ')
    while preproc.count('') > 0:
        preproc.remove('')
    right_phrases[i] = ' '.join(preproc)

    sentence = ''
    flag = False
    for c in right_phrases[i]:
        if c != ' ':
            if c != '_':
            	sentence = sentence + np.random.choice(list(string.ascii_lowercase)+[''], p=matrix[(ord(c)-97),:])
            else:
            	sentence += '_'
        else:
            if np.random.uniform(low=0.0,high=1.0,size=None) > 0.9 and flag == False:
                sentence = sentence + ''
                flag = True
            else:
                sentence = sentence + ' '
                flag = False
    wrong_phrases[i] = sentence
    print(wrong_phrases[i])
    wl = wrong_phrases[i].split(' ')
    #print(wl)
    while wl.count('') > 0:
        wl.remove('')
    correct, probab = net.viterbi(2,25,wl,sd,draw=False)
    checked_phrases[i] = ' '.join(correct)
    print(checked_phrases[i])

print('')
print('Accuracy: ')        

abs_right_count = 0
abs_wrong_count = 0
abs_checked_count = 0
error_w = 0
error_w_2 = 0
total_w = 0
for z in range(len(right_phrases)):
    right_phrases[z] = right_phrases[z].replace(' _will', '\'ll')
    right_phrases[z] = right_phrases[z].replace(' _am', '\'m')
    right_phrases[z] = right_phrases[z].replace(' _are','\'re')
    right_phrases[z] = right_phrases[z].replace(' _have','\'ve')
    right_phrases[z] = right_phrases[z].replace(' _not','n\'t')
    right_phrases[z] = right_phrases[z].replace(' _s','\'s')
    right_phrases[z] = right_phrases[z].replace(' _d','\'d')
    right_phrases[z] = right_phrases[z].replace('+',' ')
    print(z)
    print(right_phrases[z])
    print(wrong_phrases[z])
    print(checked_phrases[z])
    lr = right_phrases[z].split(' ')
    while lr.count('') > 0:
        lr.remove('')
    dr = {}
    for w in lr:
        dr[w] = lr.count(w)

    lw = wrong_phrases[z].split(' ')
    dw = {}
    for w in lw:
        dw[w] = lw.count(w)

    lc = checked_phrases[z].split(' ')
    dc = {}
    for w in lc:
        dc[w] = lc.count(w)
    
    total_w += len(lr)
    error_w += np.fabs(len(dc)-len(dr))

    for key in dr:
        if not key in dc:
            continue
        else:
            error_w += np.fabs(dr[key] - dc[key])

    error_w_2 += np.fabs(len(dw)-len(dr))

    for key in dr:
        if not key in dw:
            continue
        else:
            error_w_2 += np.fabs(dr[key] - dw[key])  

    abs_right_count += len(right_phrases[z])
    abs_wrong_count += align(right_phrases[z],wrong_phrases[z])['editDistance'] 
    abs_checked_count += align(right_phrases[z],checked_phrases[z])['editDistance'] 

print('Edit error: ')
print(100*abs_wrong_count/abs_right_count)
print(100*abs_checked_count/abs_right_count)
print('Word error: ')
print(100*error_w_2/total_w)
print(100*error_w/total_w)
