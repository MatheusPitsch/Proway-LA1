from ast import Break

nomes = []


for i in range(5):
    nome = (input('Digite um nome: ')).upper()
    nomes.append(nome)


print('Para sair da consulta digite: Sair')


while True:
    nome_qualquer = (input('Digite o nome para vereficar se está na lista: ')).upper()

    if  nome_qualquer == 'SAIR' :
            break

    elif nome_qualquer in nomes:
        print(f'{nome_qualquer} está na lista.')

    else:
        print(f'{nome_qualquer} não esta na lista.')

print('Consulta Finalizado.')

    