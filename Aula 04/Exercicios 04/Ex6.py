soma = 0
for i in range(5):
    numeros=int(input('Digite um número: '))
    
    soma += numeros
    soma2 = soma/5
print(f'A soma dos números foi: {soma}')
print(f'A media dos números foi: {soma2:.2f}')