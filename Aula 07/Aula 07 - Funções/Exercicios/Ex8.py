'''
8) A fim de manter o calendário anual ajustado com o movimento de translação da Terra, criou-se os anos
bissextos, que têm 366 dias em vez dos 365 presentes nos anos normais.
Para determinar se um ano é bissexto, é necessário saber se ele é multiplo de 4. Não pode ser múltiplo de 100,
exceto se for também múltiplo de 400.
Com isso em mente, desenvolva uma função que recebe um número correspondente a um ano e retorna se ele
é bissexto ou não (True ou False). Após isso mostre na tela uma mensagem "O ano <ano_digitado> é bissexto" 
ou "O ano <ano_digitado> não é bissexto".
Exemplo:
checar_ano_bissexto(2020) // true
checar_ano_bissexto(2100) // false
'''
def checar_ano_bissextos(ano:int)  -> bool:

    divisao_ano = ano/4

    print(divisao_ano == float)

checar_ano_bissextos(2020)