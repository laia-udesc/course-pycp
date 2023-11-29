n = int(input())

for _ in range(n):
    valor = int(input())
    soma = 0
    for i in range(1, valor):
        if valor % i == 0:
            soma += i
    print(soma)