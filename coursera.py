fname = input('Enter file name: ')

try:
    fhandle = open(fname)
    counts = dict()
except:
    print('Wrong file name enter!')
    exit()

for line in fhandle:
    words = line.split()
   
    for word in words:
        counts[word]=counts.get(word,0)+1

bigWord = None
bigCount = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print('Big word', bigWord,' Big count', bigCount)
print()
print(counts)