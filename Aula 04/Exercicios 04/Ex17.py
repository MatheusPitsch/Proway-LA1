print('''
1 - José Bolinha
2 - Maria Nascimento
3 - João da Silva
4 - Voto nulo
5 - Voto em branco 
''')

jose_bolinha = 0
maria_nascimento = 0
joao_da_silva = 0
voto_nulo = 0
voto_em_branco = 0

while (True):
    voto = int(input('Digite seu voto: '))

    if voto == 0:
        break

    elif voto == 1:
        jose_bolinha = jose_bolinha + 1

    elif voto == 2:
        maria_nascimento = maria_nascimento + 1

    elif voto == 3:
        joao_da_silva = joao_da_silva + 1

    elif voto == 4:
        voto_nulo = voto_nulo + 1 
    
    elif voto == 5:
        voto_em_branco = voto_em_branco + 1 

print(f'''
Total de Votos 2022
José Bolinha:     {jose_bolinha} voto(s)
Maria Nascimento: {maria_nascimento} voto(s)
João da Silva:    {joao_da_silva} voto(s)
Votos nulos:      {voto_nulo} voto(s)
Votos em branco:  {voto_em_branco} voto(s)

''')
