a = list()
b = []

a = [1,2,3]
print(a)
a.append(4)
print(a)
a.insert(3, 5)
print(a)
a.append('안녕')
print(a)
a.append(True)
print(a)
print(a[3])
print(a[:3])
print(a[1:3])
print(a[4:])
print(a[1:4:2])

try:
    print(a[10])
except IndexError:
    print('존재하지 않는 인덱스')

b = [3.5]
print(b)

del b[0]
print(b)
del a[6]
print(a)
a.remove('안녕')
print(a)
print(a.pop())
print(a)
print(a.pop(0))
print(a)
print(a.pop(1))
print(a)