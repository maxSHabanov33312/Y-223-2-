x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a1 = ''
a2 = ''
if (x1-1)%2==0 and y1%2==0:
    a1 = 'черная'
else:
    a1 = 'белая'
if (x2-1)%2==0 and y2%2==0:
    a2 = 'черная'
else:
    a2 = 'белая'
if a1 == a2:
    print('да')
else:
    print('нет')
