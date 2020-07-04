fname = input('Enter file name: ')

try:
    fhandle = open(fname)
    counts = dict()
except:
    print('Wrong file name enter!')
    exit()

text_list = list()
for line in fhandle:
    words = line.split()
    text_list.append(words)
    for word in words:
        counts[word]=counts.get(word,0)+1

print(counts)
print()
print(text_list)

