n = int(input())

for _ in range(n):
    str1, str2 = input().split()
    
    if len(str1) > len(str2):
        tamanho = len(str1)
    else:
        tamanho = len(str2)
    
    resultado = ''
    for i in range(tamanho):
        if i < len(str1):
            resultado += str1[i]
        if i < len(str2):
            resultado += str2[i]
    print(resultado)