creditos = input().split()
c1 = int(creditos[0])
c2 = int(creditos[1])
c3 = int(creditos[2])

if c1 == c2 or c1 == c3 or c2 == c3:
    print('S')
elif c1 + c2 == c3 or c1 + c3 == c2 or c2 + c3 == c1:
    print('S')
else:
    print('N')