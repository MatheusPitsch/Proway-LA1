'''
5) Faça uma função que receba um array de 5 elementos. 
Modifique o vetor[1] = 10 e vetor[2] = 30 e retorne o vetor modificado. 
Ao final mostre na tela o vetor original e o vetor modificado.
'''


def lista_alterada():
    '''Lista ira receber 5 valores e criara uma outra lista com valores diferentes'''
    lista_valores = []
    lista2_valores2 = []
    for i in range(5):
        valores = int(input('Digite um valor: '))
        lista_valores.append(valores)
    
    lista2_valores2 = lista_valores[::]
    
    lista2_valores2[1] = 10
    lista2_valores2[2] = 30
    
    print(lista_valores)
    print(lista2_valores2)
        
lista_alterada()