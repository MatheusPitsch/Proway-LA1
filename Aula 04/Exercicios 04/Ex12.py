from ast import Break


soma : int = 0
while (True):
    valor: int= int(input('Digite um valor: '))

    if valor < 0:
        break

    soma = soma + valor
    soma2 = soma/valor
print(f'A média aritmética dos valores recebido é : {soma2}')

