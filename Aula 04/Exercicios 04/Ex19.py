i = 0
soma = 0
while (True) :
    codigo = int(input('Digite o código do aluno: '))
    
    if codigo == 0:
        break

    for i in range(3):
        nota = int(input(f'Digte a nota do aluno {codigo}: '))

        soma += nota
    media = soma/3
    print(f'A media do aluno {codigo} é: {media:.2f}')
