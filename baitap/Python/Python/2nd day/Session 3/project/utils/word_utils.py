
from itertools import count


def dictionary(list_word):
    count_word = dict()
    for x in list_word:
        if x in count_word:
            count_word[x] += 1
        else:
            count_word[x] = 1
    return count_word

def write_dict_to_file(dictionary, file_name):
    with open(file_name, 'w') as f: 
        for key, value in dictionary.items():
            f.write('%s:%s\n' % (key, value))
    f.close()