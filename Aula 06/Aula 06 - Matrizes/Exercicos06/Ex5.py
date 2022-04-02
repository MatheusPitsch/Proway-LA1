matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

print(matriz)

soma = 0 
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if i < j:
            soma += valor
print(f'Matriz:{matriz}')
print(f'Soma: {soma}')
print('Programa Finalizado.')