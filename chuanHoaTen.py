n = input('Day la ten ban a ')
a = ' '.join(n.split()).title()
b = input('Day la ngay sinh ban a ')
if b[1] == '/':
    b = '0' + b
if b[4] ==  '/':
    b = b[0:3] + '0' + b[3:]
print(a)
print('xac nhan lai', a, 'co ngay sinh la', b)
print('version 5')
