'''
2) Crie uma função que recebe um número como parâmetro e retorne uma string com o símbolo "#" na quantidade
especificada no parâmetro.
Exemplo:
mostra_simbolo(10) // ##########
'''

def retorna_string(quantidade:int)->str:
    '''Retorna uma string com o simbolo # repitido pela quantidade de vezes informada.'''
    return quantidade * '#'
print(retorna_string(5))




