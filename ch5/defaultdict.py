import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
#a = {'A': 5, 'B': 4}
print(a)
a['C'] += 1
print(a)

b = dict()
b = {'A':5, 'B':4}
print(b)
try:
    b['C'] += 1
except KeyError:
    print('존재하지 않는 키')

print(b)