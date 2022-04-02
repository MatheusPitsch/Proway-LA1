from re import I
i=0
salario_total: int = 0
filho_total : int = 0
ma: int = 0
while (True) :
    salario = int(input('Digite o sálario: '))
    
    if salario < 0:
        break
    
    if salario > ma:
        ma = salario

    filho = int(input('Digite a quantidade de filho(s): '))

    i += 1

    salario_total += salario
    media = salario_total/i
    filho_total += filho
    media_filho = filho_total/i

print(f'A media salaria é: {media}')
print(f'A media de filhos é: {media_filho}')
print(f'O maior salario é: {ma}')