matriz_alunos = []
def cadastro_aluno():
    '''Retorna a identificação do aluno.'''
    aluno = []
    nome = str (input('Digite o nome do aluno: '))
    matricula = int (input('Digite a matricula do aluno: '))
    if verificacao_matricula(matricula) == True:
        input('Aluno ja cadastrado')
    else:
        aluno.append([nome,matricula,'--','--','--'])
        matriz_alunos.append(aluno)

def verificacao_matricula(matricula) -> bool:
    for i  in matriz_alunos:
        if i[0] == matricula:
            return True
    return False

def cadastrar_notas_aluno():
    '''Cadastra as 3 notas do aluno.'''
    matricula = int(input('Digite a matricula do aluno que deseja insirir as notas.'))
    if verificacao_matricula == True:
        for i in range(3):
            nota = float(input(f'Digite a nota {i} do aluno: '))
            for i in matriz_alunos:
                if i[2] == '--':
                    i[2] == nota
                elif i[3] == '--':
                    i[3] == nota
                elif i[4] == '--':
                    i[4] == nota

cadastro_aluno()
print(matriz_alunos)
cadastrar_notas_aluno()
print(matriz_alunos)