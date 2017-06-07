from smartdictionary import SmartDictionary

sd = SmartDictionary(SmartDictionary.SMART_WORDSEN)

with open('/home/ld/virtualshare/txts/It_-A-Novel-Stephen-King.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
for c in [',','(',')','[',']','‘','’','"','“','”','-','|','»','«','<','>','—','_','/']:
    data=data.replace(c,' ')
for n in ['1','2','3','4','5','6','7','8','9','0']:
    data=data.replace(n,'')
data=data.replace('\'ll',' _will')
data=data.replace('\'re',' _are')
data=data.replace('n\'t',' _not')
data=data.replace('\'s',' _s')
data=data.replace('\'d',' _d')
data=data.replace('\'',' ')
for c in ['!','?',';',':']:
    data=data.replace(c,'.')

data_trans = data.split('.')

manca = []
for f in data_trans:
    words = list(set(f.split(' ')))
    for w in words:
        w = w.lower()
        if not sd.check_existance(w):
            manca.append(w)
print(len(list(set(manca))))
print(len(manca))

data=data.replace('.',' ')
data=data.split(' ')
print(len(list(set(data))))
print(len(data))
