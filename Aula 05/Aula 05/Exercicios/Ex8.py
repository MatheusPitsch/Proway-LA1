
numeros = []

while True:
    
    if numeros[6::]:
        break
    
    valores = float(input('Digite numeros INTEIROS e PARES: '))

    if valores % 2 == 0:
        numeros.append(valores)

    else:
        print('Esse número não é par!')
print(numeros[::-1])

    

