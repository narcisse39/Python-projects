fname = 'mbox-short.txt'
try:
    fhand = open(fname)
    counts = dict()
    lst_item = list()
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    _hour = words[5].split(':')
    counts[_hour[0]] = counts.get(_hour[0], 0) + 1

print(counts)

for key,val in counts.items():
	newtup = (val,key)
	lst_item.append(newtup)

print('='*60)
print('Flipped\n',lst_item)

print('='*60)
lst_item = sorted(lst_item)
print('Sorted\n',lst_item)

print('='*60)
for value,key in lst_item:
	print(key,value)

