

from pickle import TRUE
from numpy import true_divide

intervalo = 0

valor = 0

while (True):
    valor = int(input('Digite um valor: '))

    if valor < 0:
        break
    
    elif valor > 10 and valor <20:
        intervalo = intervalo + 1
    
print(intervalo)