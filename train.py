from smartdictionary import SmartDictionary

sd = SmartDictionary(SmartDictionary.SMART_WORDNET3)

with open('/home/ld/virtualshare/txts/pg766.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
for c in [',','(',')','[',']','‘','’','"','“','”','-','|','»','«','<','>']:
    data=data.replace(c,' ')
data=data.replace('\'ll',' _will')
data=data.replace('\'re',' _are')
data=data.replace('n\'t',' _not')
data=data.replace('\'s',' _s')
data=data.replace('\'d',' _d')
data=data.replace('\'',' ')
for c in ['!','?',';']:
    data=data.replace(c,'.')

data_trans = data.split('.')

for f in data_trans:
    words = list(set(f.split(' ')))
    for w in words:
        w = w.lower()
        if not sd.check_existance(w):
            print(w)

processed = ''

print(data_trans[0:20])
