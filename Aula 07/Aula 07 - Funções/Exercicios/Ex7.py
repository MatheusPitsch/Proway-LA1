'''
7) Desenvolva uma função que receba como parâmetro um número de 1 a 10. Internamente, na função, será
gerado um número aleatório de 1 a 10. A função deverá retornar se o parâmetro de entrada foi igual ao número
sorteado internamente. Se o valor fornecido foi o sorteado, retorne "Parabéns! O número sorteado foi o X". Se
não for igual, retorne "Que pena! O número sorteado foi o X". X é o número que foi sorteado.
'''

import random


def sorteador_numeros() ->int:
    valor_escolhido = int(input('Digite um valor: '))

    numero_aleatorio = random.randint(1,10)

    if numero_aleatorio == valor_escolhido:
        print(f'Parabéns! O número sorteado foi o {numero_aleatorio}')
    else:
        print(f"Que pena! O número sorteado foi o {numero_aleatorio}")

sorteador_numeros()