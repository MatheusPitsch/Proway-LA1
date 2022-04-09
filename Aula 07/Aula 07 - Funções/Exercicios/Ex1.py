from ast import List


def retorna_primeiro_ultimo_elemento(array: List[int]) -> List[int]:
    '''Retorna o primeiro e o último elemento de array.'''
    return [array[0],array[-1]]

print(retorna_primeiro_ultimo_elemento([1,2,3]))
