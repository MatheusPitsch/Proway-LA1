lista = []
lista2 = []
posicao = 0

for i in range(5):
    valores_1 = int(input(f'Digite um valor para {posicao}: '))
    lista.append(valores_1)

    valores_2 = int(input(f'Digite um valor para {posicao}: '))
    lista2.append(valores_2)
    posicao += 1

posicao = 0

for i in lista:
    for j in lista2:
        if i == j:
            print(f'na posição {posicao} os numeros SÃO identicos')
            break
    if i != j:
        print(f'Na posição {posicao} os números NÃO são identicos')
    
    
    posicao +=1

print(lista)
print(lista2)