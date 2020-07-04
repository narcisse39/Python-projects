fname = input('Enter file name: ')

try:
    fhandle = open(fname)
    counts = dict()
except:
    print('file cannot be open!')
    exit()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
   
    counts[words[1]]=counts.get(words[1],0) + 1

bigWord = None
bigCount = None

for word, count in counts.items():
	##word = keys, count = values
    if bigCount is None or count > bigCount:
	##bigCount is None => first word
        bigWord = word
        bigCount = count

print(bigWord,bigCount)

