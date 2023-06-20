import re
dictionary = dict()

with open("data.txt", "r") as line:
    for x in re.split("\W+", line.read()):
        if(x in dictionary):
            dictionary[x] += 1
        else:
            dictionary[x] = 1

with open("result.txt", 'w') as f: 
    for key, value in dictionary.items(): 
        f.write('%s:%s\n' % (key, value))