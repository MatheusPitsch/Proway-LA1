lista= []
i = 0
numeros_negativos: int = 0
soma: int = 0

for i in range(10):
    
    numeros = int(input('Digite um número: '))
    lista.append(numeros)


    if lista[i] < 0 :
        numeros_negativos += 1
    
    else:
        soma += lista[i]

    
print(f'Os números negativos são: {numeros_negativos}')
print(f'A soma dos números positivos é: {soma}')
