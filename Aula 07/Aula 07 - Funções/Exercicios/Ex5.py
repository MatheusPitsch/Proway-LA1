'''
5) Faça uma função que receba um array de 5 elementos. 
Modifique o vetor[1] = 10 e vetor[2] = 30 e retorne o vetor modificado. 
Ao final mostre na tela o vetor original e o vetor modificado.
'''

from re import I
from typing import List
def troca_valores(lista2_valores2) -> bool:
    for i,valores in lista2_valores2:
        if valores[1]:
            valores[1] == 10
        return True
    return False

def lista_alterada() -> List[int]:
    '''Lista ira receber 5 valores e criara uma outra lista com valores diferentes'''
    lista_valores = []
    lista2_valores2 = []
    for i in range(5):
        valores = int(input('Digite um valor: '))
        lista_valores.append(valores)
    
    lista2_valores2 = lista_valores[::]
    if troca_valores == True:
        valores[2] == 30
    
    print(lista_valores)
    print(lista2_valores2)
        
lista_alterada()