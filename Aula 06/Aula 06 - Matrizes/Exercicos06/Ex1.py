matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

maior = 0
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if valor > 10:
            maior += 1
print(f'Ha {maior} maior que 10.')
print('Programa Finalizado.')