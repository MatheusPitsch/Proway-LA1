matriz = [
    
    ['*', '*', '*'],            #Preciso achar definir a variavel linha aqui
    ['*', '*', '*'],
    ['*', '*', '*']
]

while True:

    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        for q, linha in enumerate(matriz): #PARA COLOCAR A VARIAVEL LINHA AQUI
            if q == '*':
                print('Tudo certo')
            else:    
                break

    
    matriz = [ [0 for i in range(3)] for j in range(3)]
        


    A = int(input('Digite uma posição X: '))
    A_1 = int(input('Digite uma posição Y: '))
   
    
    if matriz[A][A_1] == '*':
        matriz[A][A_1] = 'X'
    else:
        print('Essa posição ja esta ocupada!')
        continue
    
    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        for q, linha in enumerate(matriz): #PARA COLOCAR A VARIAVEL LINHA AQUI
            if q == '*':
                print('Tudo certo')
            else:    
                break


    B = int(input('Digite uma posição I: '))
    B_1 = int(input('Digite uma posição M: '))
    
    if matriz[B][B_1] == '*':
        matriz[B][B_1] = '0'
    else:
        print('Essa posição ja esta ocupada!')
        continue

    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        for q, linha in enumerate(matriz): #PARA COLOCAR A VARIAVEL LINHA AQUI
            if q == '*':
                print('Tudo certo')
            else:    
                break
    
    

    for i,linha in enumerate(matriz): #Print para mostrar a matriz
        for j, valor in enumerate(linha): 
            print(valor,end=" ")        
        print()