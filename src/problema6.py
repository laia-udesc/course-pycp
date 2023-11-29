n = int(input())

for _ in range(n):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])
    soma = 0
    for i in range(x, y + 1):
        soma += i
    print(soma)