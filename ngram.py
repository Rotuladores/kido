from google_ngram_downloader import readline_google_store

string = 'fe'

reader = readline_google_store(ngram_len=2)

count = 10 + (ord(string[0]) - 97)*27 + ord(string[1]) - 97 + 1

while count > 0:
    fname, url, records = next(reader)
    count -= 1
    print(url)
#    while True:
#        record = next(records)
#        print(record)
