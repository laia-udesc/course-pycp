frase = input()
frase = frase.replace(' ', '')

dancante = True
for i in range(len(frase)):
    if i % 2 == 0:
        if frase[i] != frase[i].upper():
            print('NÃO')
            dancante = False
            break
    else:
        if frase[i] != frase[i].lower():
            print('NÃO')
            dancante = False
            break
            
if dancante:
    print('SIM')