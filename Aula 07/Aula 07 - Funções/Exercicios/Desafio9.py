from ast import Global
import os
from typing import List

matriz_aluno = []

def mostrar_menu():
    '''Mostra o menu parao o cliente.'''

    print('''
    
        Menu do Professor

    1) Cadastrar aluno
    2) Editar informações do aluno
    3) Cadastrar notas de um aluno
    4) Listar alunos
    0) Sair
    ''')

def cadastro_aluno() -> List[int]:
    '''Cadastra o aluno no sistema da escola.'''
    aluno = []
    matricula = int(input('Digite a matricula do aluno: '))
    if verificacao_matricula(matricula) == True:
        input('Aluno ja cadastrado')
    else:
        nome = str(input('Digite o nome do aluno: '))
        aluno = [matricula,nome,'--','--','--','--','--']
        matriz_aluno.append(aluno)

def verificacao_matricula(matricula) -> int:
    '''Verifica se o aluno existe no sistema.'''
    for i in matriz_aluno:
        if i[0] == matricula:
            return True
    return False

def editar_informacao_aluno() -> str:
    '''Edita o nome do aluno'''
    matricula = int(input('Digite a matricula do aluno: '))
    indece_aluno = obtem_matricula(matricula)
    if indece_aluno < 0:
        input('Não existe um aluno com a matricula informada.')
        return
    nome_novo = str(input('Digite o novo nome do aluno: '))
    matriz_aluno[indece_aluno][1] = nome_novo

def obtem_matricula(matricula) -> int:
    '''Usado para localizar aonde o aluno se encontra.'''
    global matriz_aluno
    for i, aluno in enumerate(matriz_aluno):
        if aluno[0] == matricula:
            return i 
    return -1

def cadastra_nota_aluno() -> int:
    '''Cadastra a nota do aluno no siste, mostra a media e se esta aprovado ou não.'''
    global matriz_aluno
    matricula = int(input('Digite a matricula do aluno: '))
    indece_aluno = obtem_matricula(matricula,)
    
    if indece_aluno < 0:
        input('Não existe um aluno com a matricula informada.')
        return
    soma = 0
    for i in range (1,4):
        nota = int(input(f'Digite a {i}ª nota do aluno: '))
        soma += nota
        
        matriz_aluno[indece_aluno][i + 1] = nota
    media = soma/3
        
    matriz_aluno[indece_aluno][5] = media
    
    if media >= 6:
        matriz_aluno[indece_aluno][6] = 'Aprovado'
    else:
        matriz_aluno[indece_aluno][6] = 'Reprovado'

def listar_alunos() -> list:
    '''Mostra a lista dos alunos cadastrados no sistema.'''
    for aluno in matriz_aluno:
        for coluna in aluno:
            print(coluna, end=' ')
        print()
    input('Aperte enter para continuar.')

while True:
    os.system('cls')
    mostrar_menu()

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        cadastro_aluno()
    elif opcao == 2:
        editar_informacao_aluno()
    elif opcao == 3:
        cadastra_nota_aluno()
    elif opcao == 4:
        listar_alunos()
    elif opcao == 0:
        break
    else:
        input('Opção invalida.')