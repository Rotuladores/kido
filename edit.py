import edlib

def import_smart_dictionary(path):
    word_len = []
    smart_dictionary = []
    with open(path, 'r') as f:
        skip = f.readline()
        h = f.readline().strip()[1:].split(' ')
        word_len = list(map(lambda x: int(x), h))
        for l in f:
            smart_dictionary.append(l.strip())
    return smart_dictionary, word_len

def edit_search(smart_dictionary, word_len, word, threshold):
    k = len(word)
    k_min = k - threshold
    k_max = k + threshold + 1

    ret = []

    if k_min < 0:
        k_min = 0
    if k_max > len(word_len):
        k_max = len(word_len)

    search = smart_dictionary[word_len[k_min] : word_len[k_max] -1]

    for s in search:
        lev = edlib.align(word, s)["editDistance"]
        if lev <= threshold:
            ret.append((lev, s))
    ret = sorted(ret, key=lambda x: x[0])

    return [x[1] for x in ret]




smart_dictionary, word_len = import_smart_dictionary('dictionary/smart_wordnet3.dat')

# voglio tutte le parole con distanza massimo k da TEST
test = 'garbaged'

edit = edit_search(smart_dictionary, word_len, test, 3)

print(edit)
