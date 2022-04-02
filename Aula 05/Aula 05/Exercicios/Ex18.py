import random


lista = []
pares = []
impares = []
soma_par = 0
multiplica_impar = 1

for i in range(10):
    numero = random.randint(1, 10)
    
    lista.append(numero)


for numero in lista:
    if numero % 2 == 0: 
        pares.append(numero)
        soma_par += numero
    else:
        impares.append(numero)
        multiplica_impar *= numero


print(lista)
print(soma_par)
print(multiplica_impar)


    