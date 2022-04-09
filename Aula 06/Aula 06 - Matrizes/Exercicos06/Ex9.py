matriz = [
    
    ['*', '*', '*'],            #Preciso achar definir a variavel linha aqui
    ['*', '*', '*'],
    ['*', '*', '*']
]
d = True

while d == True:

    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        if matriz != ['*']:
            None
        else:    
            d == False


    A = int(input('Digite uma posição X: '))
    A_1 = int(input('Digite uma posição Y: '))
   
    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        if matriz != ['*']:
            None
        else:    
            d == False

    if matriz[A][A_1] == '*':
        matriz[A][A_1] = 'X'
    else:
        print('Essa posição ja esta ocupada!')
        continue
    

    
    B = int(input('Digite uma posição I: '))
    B_1 = int(input('Digite uma posição M: '))
    
    for i, d in enumerate(matriz):#VERIFICAR DE PARADA
        if matriz != ['*']:
            None
        else:    
            d == False

    if matriz[B][B_1] == '*':
        matriz[B][B_1] = '0'
    else:
        print('Essa posição ja esta ocupada!')
        continue

    
    
    

    for i,linha in enumerate(matriz): #Print para mostrar a matriz
        for j, valor in enumerate(linha): 
            print(valor,end=" ")        
        print()