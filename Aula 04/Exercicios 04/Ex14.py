
from math import factorial

soma: int = 0
valor = int(input('Digite um valor: '))

if valor < 0 or valor == 0:
    print('Esse número é invalido')

else:
    factorial: int = 1
    
    while valor > 1:
        factorial *= valor
        valor -= 1


print(factorial)
    




