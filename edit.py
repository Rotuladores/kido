def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


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

    search = smart_dictionary[word_len[k_min] : word_len[k_max]]

    for s in search:
        lev = levenshtein(word, s)
        if lev <= threshold:
            ret.append((lev, s))
    ret = sorted(ret, key=lambda x: x[0])

    print([x[1] for x in ret])




smart_dictionary, word_len = import_smart_dictionary('dictionary/smart_wordnet3.dat')

# voglio tutte le parole con distanza massimo 4 da TEST
test = 'garbagd'

edit_search(smart_dictionary, word_len, test, 2)
