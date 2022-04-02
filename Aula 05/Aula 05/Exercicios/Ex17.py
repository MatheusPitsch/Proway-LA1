import random

lista = []
sequencia = []
ma = 0

for i in range(10):
    x = random.randint(0,20)
    lista.append(x)

for numero in enumerate(lista):
    if numero > ma:
        ma = numero
        sequencia.append(ma)


print(sequencia)