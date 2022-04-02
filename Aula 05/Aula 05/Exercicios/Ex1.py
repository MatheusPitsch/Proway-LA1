lista = []
for i in range(10):
    valor = int(input('Digite um valor: ')) 
    lista.append(valor)

contador = 0

for valor in lista:
    if valor % 2 == 0:
        contador +=1

print(f'Na lista possui {contador} pares')