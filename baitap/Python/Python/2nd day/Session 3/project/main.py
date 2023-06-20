from utils import file_utils, word_utils

filename = "data.txt"
dictionary = word_utils.dictionary(file_utils.fhand(filename))
# print(dictionary)
word_utils.write_dict_to_file(dictionary, "result.txt")
