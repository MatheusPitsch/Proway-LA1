lista = []
mai = men = 0
posicaomen: int = 0
posicaomai: int = 0

for i in range(5):
    valores = int(input('Digite um valor: '))
    lista.append(valores)

    if i == 0:
        mai = men = lista[i]
    
    else:
        if lista[i] > mai:
            mai = lista[i]
            posicaomai += 1

        if lista[i] < men:
            men = lista[i]
            posicaomen += i

print(f'O maior valor é {mai} e se encontra na posição {posicaomai}')
print(f'O menor valor é {men} e se encontra na posição {posicaomen}')
print(f'Os valores digitados foram {lista}')