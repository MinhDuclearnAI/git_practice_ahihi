se = input()
x, y, *z = se
print(x, y, z)
s = {}
for i in se:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
for x, y in s.items():
    print(x,'so lan xuat hien la', y)
print('version 7')