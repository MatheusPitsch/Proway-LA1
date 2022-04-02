lista = []
maior_valor = 0
posicao = 0

for i in range(5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if i == 0:
        maior_valor = valor

    elif valor > maior_valor:
        maior_valor = valor
        posicao = i

print(lista) 
print(maior_valor) 
print(posicao) 