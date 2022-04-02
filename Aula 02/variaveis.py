'''
Variavés

As variavés são espaços na memoria que sua aplicação utiliza para amazenar os dados em tempo execução.

Regra de nomenclatura
        *Não pode começar com simbolos (exeção do _) e números.
        *Os nomes devem ser descretivos e de simples entedimento
        *Cada nova palavra da variavel deve ser separada por _ 

Linguagens dinamicamente tipadas x linguagens esticamente tipadas
'''
nome: str = "Matheus"
cpf: str = "105.904.309-20" 
idade: int = 19
altura: float = 1,8
presente: bool = True
vazio = None

print(type(nome))#Type serve para mostrar o tipo do dado
print(cpf)
print(hex(id(cpf)))#(hex(id)) server para mostrar o edereço

valor1, valor2 = 10, 20
print(valor1, valor2)

a, b = 2, 4
auxiliar = a # a=2, b=4, auxiliar = 2
a = b  # a=4, b=4, auxiliar = 2
b = auxiliar # a=4, b=2, auxiliar = 1
print(a, b)


#Exclusivo py
c,d = 1,2
d,c = c,d
print(c,d)