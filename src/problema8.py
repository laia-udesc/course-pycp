lista = eval(input())
b = int(input())

menor = lista[0]
for numero in lista[:b]:
    if numero < menor:
        menor = numero
        
print(menor)