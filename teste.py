from ast import Global
from typing import List

matriz_aluno = [[71719,'matheus''--','--','--']]

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
        aluno = [matricula,nome,'--','--','--']
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
    global matriz_aluno
    for i, aluno in enumerate(matriz_aluno):
        if aluno[0] == matricula:
            return i 
    return -1


editar_informacao_aluno()
print(matriz_aluno)