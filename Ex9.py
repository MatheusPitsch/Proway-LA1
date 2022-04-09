matriz_alunos = []


def mostrar_menu():
    '''Mostra o menu parao o cliente.'''

print('''
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
    
    if verificacao_matricula (matricula):
        input('Matricula já cadastrada.')
        


    
    aluno.append([nome,matricula,'--','--','--'])
    matriz_alunos.append(aluno)
        
def verificacao_matricula(matricula) -> bool:
    for i , aluno in matriz_alunos:
        if i[0] == matricula:
            return True
    return False

def editar_informacao_aluno(matricula):
    '''Editar a informações do aluno.'''
    informar_matricula = int(input('Digite a matricula do aluno que deseja alterar o nome: '))
    
    if verificacao_matricula == True:
        nome_novo = str(input('Digite o novo nome do aluno: '))
        nome_novo

def cadastrar_notas_aluno():
    '''Cadastra as 3 notas do aluno.'''
def listar_alunos():
    '''Lista todos os alunos que foram cadastrados.'''