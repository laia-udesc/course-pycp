pontos = eval(input())

media = 0
for ponto in pontos:
    media += ponto
media = media / len(pontos)

qtd = 0
for ponto in pontos:
    if ponto > media:
        qtd += 1

print(qtd)