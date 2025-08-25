se = input()
s = {}
for i in se:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
for x, y in s.items():
    print(x, y)