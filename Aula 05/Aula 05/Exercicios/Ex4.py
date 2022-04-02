lista1 = []
lista2 = []

for i in range(5):
    valor = int(input('Digite um valor: '))
    lista1.append(valor)
    lista2.insert(0,valor)
    
print(lista1)
print(lista2)