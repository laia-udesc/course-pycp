N = int(input())

joey = 0
monica = 0

for _ in range(N):
    valores = input().split()
    v1 = int(valores[0])
    v2 = int(valores[1])
    if (v1 + v2) % 2 == 0:
        joey += 1
    else:
        monica += 1
        
if joey > monica:
    print('JOEY')
elif monica > joey:
    print('MONICA')
else:
    print('EMPATE')