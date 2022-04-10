matriz_alunos = [[71719,'matheus']]
def verificacao_matricula(matricula) -> bool:
    for i  in matriz_alunos:
        if i[0] == matricula:
            return True
    return False
def editar_informacao_aluno() -> str:
    '''Editar o nome do aluno.'''
    matricula = int(input('Digite a matricula do aluno que deseja alterar o nome: '))
    
    if verificacao_matricula(matricula) == True:
        nome_novo = str(input('Digite o novo nome do aluno: '))
        for i in matriz_alunos:
            if i[0] == matricula:
                i[1] = nome_novo
    else:
        input('Aluno não encontrado')
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

editar_informacao_aluno()
print(matriz_alunos)