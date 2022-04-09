'''
4) Escreva um script que receba o ano em que você nasceu e calcule a sua idade.
 Utilize uma função que retorna a idade.
'''
from datetime import datetime


def retorna_idade( ano_nascimento: int):
    '''Retorna o cauculo da idade que você tem.'''
    ano_atual = datetime.now().year
    return  ano_atual - ano_nascimento 
print(retorna_idade(2002))