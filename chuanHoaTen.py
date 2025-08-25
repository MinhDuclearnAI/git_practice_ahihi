n = input('Day la ten ban a ')
a = ' '.join(n.split()).title()
b = input('Day la ngay sinh ban a ')
d = list(map(int, input().split()))
d = [x ** 2 for x in d]
print(d)
print(a)
