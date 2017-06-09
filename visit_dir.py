import os

def visit_dir(path):
    l = []
    gen = next(os.walk(path))
    l = l + gen[2]
    l = list(map(lambda x: gen[0][len(os.getcwd())+1:]+''+x,l))
    # print(gen)
    for s in gen[1]:
        l = l+visit_dir(path+s+'/')
    return l

path = '/home/ld/daniele/UniMiB/Magistrale/Metodi probabilistici/misspelling/training_set/'
z = visit_dir(path)
print(z)