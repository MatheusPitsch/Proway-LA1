'''
Matrizes sã
'''
matriz = [
    #0   1   2
    [1, 0, 0], #Linha 0
    [0, 1, 0], #Linha 1
    [0, 0, 1]  #Linha 2 
]
#Mostra a matriz em forma de matriz
for i,linha in enumerate(matriz): #percorre a linha
    for j, valor in enumerate(linha): #percorre as culunas dentro da linha 
        print(valor,end=" ")            #printa os valores que estão na linha e na coluna, end serve para printar na mesma linha
    print() #printa um vazio para pular a linha 

# Mostrando um elemento dentro de uma matriz
print(matriz[1][1])

# Mostrando uma matriz na tela
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()

# Cadastrando valores em uma matriz
nova_matriz = []
#Aqui sera uma matrix 3x3 (range3)
for i in range(3): #A linha em que voce estara acrescentando  
    linha = []
    for j in range(3): #A coluna que você estara acrescentando 
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz: "))
        linha.append(valor) 
    nova_matriz.append(linha)

print(nova_matriz)

