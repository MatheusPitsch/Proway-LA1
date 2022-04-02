notas_aluno = []
i = 0
soma_nota = 0
maior = 0

while i >= 0:
    notas = int(input(f'Digite a {i} nota: '))

    if notas >= 0:
         notas_aluno.append(notas)
    
    else:
        break

    i+=1

for num in notas_aluno:
    soma_nota+=num

    media = soma_nota/i

for num in notas_aluno:
    if maior == 0 or num > maior:
        maior = num

print(f'A media da sala é: {media}')
print(f'A maior nota foi: {maior}')
