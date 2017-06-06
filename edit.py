import edlib
from smartdictionary import SmartDictionary

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


def test():
    sd = SmartDictionary(SmartDictionary.SMART_WORDNET3)

    # voglio tutte le parole con distanza massimo k da TEST
    test = 'garbaged'
    edit = edit_search(sd.smart_dictionary, sd.word_len, test, 3)
    print(edit)

if __name__ == '__main__':
    test()