numeros = []
soma: int = 0

for i in range(8):

    valores = int(input('Digite um valor: '))
    numeros.append(valores)

while True:

    stop=str(input('Deseja Continuar?'))
    
    if stop in 'Nn' :
        break


    x = int(input('Digite uma posição da lista: '))
    y = int(input('Digite uma posição da lista: '))

    if numeros[x] and numeros[y] :
        soma = numeros[x] + numeros[y]

    else:
        print('A posição digitada na lista não foi encontrada')

    print(soma)
print('Programa Finalizado')