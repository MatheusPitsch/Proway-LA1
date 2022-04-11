'''
6) Elabore uma função que receba um vetor e retorne outro 
etor que tenha todos os números que são pares e estão em
índices pares do vetor.
'''
def retorna_pares() ->list[int]:
    '''Recebe numeros e cria uma matriz somente com numeros pares'''
    valores = []
    valores_pares = []
    for i in range(5):
        numeros = int(input('Digite os valores: '))
        valores.append(numeros)
    
    for i, numeros in enumerate(valores):
        if numeros % 2 == 0:
            valores_pares.append(numeros)

    print(f'Os valores digitados foram: {valores}')
    print(f'Os valores pares são: {valores_pares}')

retorna_pares()


