#import numpy as np
#import re

#with open('/home/ld/virtualshare/txts/ap.txt', 'r') as myfile:
#    data=myfile.readlines()

#print(len(data))

#processed = []
#for line in data:
#     pline = re.sub('[]',line)
#     for c in [',','.','-','(',')','/','&','%','$','"','`','\'','+','_','*','<','>','?','!',';',':']:
#         pline = pline.replace(c,' ')
#     processed.append(pline)
#
# processedfile = open('/home/ld/daniele/UniMiB/Magistrale/Metodi probabilistici/roba_progetto/giusto.txt', 'w')
#
# for line in processed:
#   processedfile.write("%s" % line)

import pandas as pd
import re

data = pd.read_excel('/home/ld/daniele/UniMiB/TXTM-eduopen/USA-Geolocated-tweets-free-dataset-Followthehashtag/dashboard_x_usa_x_filter_nativeretweets.xlsx', sheetname='Stream', header=0)
print(data.shape)
data = data[data['Tweet language (ISO 639-1)'] == 'en']
print(data.shape)
tweets = data['Tweet content'].tolist()
print(tweets[0:5])

ptweets = []
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
for tweet in tweets:
    ptweets.append(emoji_pattern.sub(r'', tweet))
print(ptweets[0:5])

