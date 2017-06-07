from smartdictionary import SmartDictionary
import re

sd = SmartDictionary(SmartDictionary.SMART_WORDNET3)

def preprocess(s):
	# Abbreviations
	s = s.replace('n\'t', ' not')
	s = s.replace('\'ve' , ' ve')
	s = s.replace('\'d' , ' d')
	s = s.replace('\'re' , ' are')

	# Punctionation
	s = s.replace('\'' , '')
	s = s.replace(',' , '')
	s = s.replace(';' , '')
	# s = s.replace('-' , '')
	# s = s.replace(':' , '')
	s = s.replace('!' , '.')
	s = s.replace('?' , '.')

	frasi = s.split('.')
	for f in frasi:
		words = f.split(' ')
		for w in words:
			if sd.check_existance(w):
				print(w)

	return s


    
#tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
#emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 

 
tweet = 'RT @marcobonzanini: just\'re an\'d examplen\'t aren\'t! :D http://example.com #NLP'
print(preprocess(tweet))
# ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']