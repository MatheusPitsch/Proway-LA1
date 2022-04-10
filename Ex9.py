matriz_alunos = [[71719,'matheus']]


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

def cadastro_aluno():
    '''Retorna a identificação do aluno.'''
    aluno = []
    nome = str (input('Digite o nome do aluno: '))
    matricula = int (input('Digite a matricula do aluno: '))
    if verificacao_matricula(matricula) == True:
        input('Aluno ja cadastrado')
    else:
        aluno.append([matricula,nome,'--','--','--'])
        matriz_alunos.append(aluno)
        
def verificacao_matricula(matricula) -> bool:
    for i  in matriz_alunos:
        if i[0] == matricula:
            return True
    return False

def editar_informacao_aluno():
    '''Editar a informações do aluno.'''
    matricula = int(input('Digite a matricula do aluno que deseja alterar o nome: '))
    
    if verificacao_matricula(matricula) == True:
        nome_novo = str(input('Digite o novo nome do aluno: '))
        for i in matriz_alunos:
            if i[0] == matricula:
                i[1] = nome_novo
    else:
        input('Aluno não encontrado')

def cadastrar_notas_aluno():
    '''Cadastra as 3 notas do aluno.'''
    matricula = int(input('Digite a matricula do aluno que deseja insirir as notas: '))
    if verificacao_matricula(matricula) == True:
        for i in range(3):
            nota = float(input(f'Digite a nota {i} do aluno: '))
            for i in matriz_alunos:
                if i[2] == '--':
                    i[2] == nota
                elif i[3] == '--':
                    i[3] == nota
                elif i[4] == '--':
                    i[4] == nota
    else:
        input('Aluno não encontrado')

def listar_alunos():
    '''Lista todos os alunos que foram cadastrados.'''

