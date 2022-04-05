
matriz = []
matriz_2 = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

i = 0
j = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor_2 = int(input('Digite um valor 2: '))
        linha.append(valor_2)
    matriz_2.append(linha)


matriz_maior = []
maior = 0
i = 0
j = 0

for i, linha in enumerate(matriz):
    for j,valor in enumerate(linha): 
       if maior == 0 or valor > maior:
        maior = valor
        matriz_maior.append(maior)
        
        i = 0
        j = 0
        valor = 0
        
        for i,valor in enumerate(matriz_maior):
            if valor > i:
                matriz_maior[i] = valor
        
print(matriz_maior)





print(matriz)
print(matriz_2)
