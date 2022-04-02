matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

x = int(input('Digite um valor X: '))

posicao = ''
for i, linha in enumerate(matriz):
    for j , valor in enumerate(linha):
        if x == valor:
            posicao = f'[{i}][{j}]'
            break
    if posicao:
        break
if posicao:
    print(f'Achei: {posicao}')
else:
    print('Não achei')
        