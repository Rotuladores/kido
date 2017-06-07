from google_ngram_downloader import readline_google_store

reader = readline_google_store(ngram_len=2)

while True:
    fname, url, records = next(reader)
    print(url)
    while True:
        record = next(records)
        print(record)
