'''
3) Escreva uma função que receba dois parâmetros. O primeiro é o elemento que repetirá, enquanto o segundo é
o número de vezes que haverá a repetição. Um array deve ser retornado.
Exemplo:
repetir_elemento("oi", 3) // ["oi", "oi", "oi"]
'''
from typing import List


def retornar_elementos( mensagem: str, vezes: int) -> List[str]:
    '''Retorna uma lista com a mensagem repetida pela quantidade de vezes informada.'''
    lista=[]
    for i in range(vezes):
        lista.append(mensagem)
    return lista
print(retornar_elementos('oi',3))