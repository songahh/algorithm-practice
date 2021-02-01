a = dict()
b = {}

a = {'key1':'value1', 'key2':'value2'}
print(a)
a['key3'] = 'value3'
a['key4'] = 'value4'
print(a)
print(a['key2'])
print('key1' in a)

try:
    print(a['key5'])
except KeyError:
    print('\'key5\' : 존재하지 않는 키')

del a['key3']
print(a)

if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

for k,v in a.items():
    print(k, v)