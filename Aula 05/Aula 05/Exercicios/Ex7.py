numeros = []
soma = []
cauculo=0

for i in range(5):
    valor = int(input('Digite um número: '))
    numeros.append(valor)

for num in numeros:
    calculo = num**2
    soma.append(calculo)

print(f'Os valores digitados foram: {numeros}')
print(f'Esses valores elevados ao quadrado são: {soma}')