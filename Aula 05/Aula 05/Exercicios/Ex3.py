lista = []
maior_valor = 0
menor_valor = 0

for i in range(5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if i == 0:
        maior_valor = valor
        menor_valor = valor
    
    elif valor > maior_valor:
        maior_valor = valor
    
    elif valor < menor_valor:
        menor_valor = valor

print(f'O maior valor é: {maior_valor}')
print(f'O menor valor é: {menor_valor}')
