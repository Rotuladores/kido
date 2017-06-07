import numpy as np
import re

with open('/home/ld/virtualshare/txts/ap.txt', 'r') as myfile:
    data=myfile.readlines()

print(len(data))

processed = []
for line in data:
    pline = re.sub('[]',line)
    for c in [',','.','-','(',')','/','&','%','$','"','`','\'','+','_','*','<','>','?','!',';',':']:
        pline = pline.replace(c,' ')
    processed.append(pline)

processedfile = open('/home/ld/daniele/UniMiB/Magistrale/Metodi probabilistici/roba_progetto/giusto.txt', 'w')

for line in processed:
  processedfile.write("%s" % line)
