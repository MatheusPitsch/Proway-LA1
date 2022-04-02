####
from ast import AugStore


2
nome = 'Matheus Pitsch'
print(f'Olá meu nome é {nome}')
####
3
print("Cadastro do funcionário")
print('A)Cadastrar funcionários')
print('B)Listar funcionários')
print('C)Editar funcionários')
print('D)Remover funcionários')
print('E)Sair')

nome = input('digite a opção desejada: ')
print(nome)
####
4
admin, nome = None, None
nome = "João"
admin = nome
print(nome)
####
5
nome: int= input('Digite seu nome: ')
idade: float= input('Digite sua idade: ')
peso:float = input('Digite seu peso: ')
altura: float=input('Digite sua altura:')
telefone:int =input('Digite seu telefone:')

print(f'{nome}')
print(f'{idade}')
print(f'{peso}')
print(f'{altura}')
print(f'{telefone}')
####
6
titulo = input ('Titulo do ultimo livro que leu:')
edicao = input ('Edição do livro:')
autor = input ('Autor do livro:')
datadpub = input ('Data de Publicação do livro:')

print (titulo)
print (edicao)
print (autor)
print (datadpub)#publicação do livro
####
7
datadnasc = '13/05/2002'#data de nascimento
filhos = '3'
usuario = '71719'
####
8
print(f"Olá {1}") # ?
####
9
x,y = 10, 8
area = (x*y)/2+3**4
print(area)
####
10
a = 2
x = 1 + 2
print(a,x)
####
11
a = (10 - 2) * 3 + 1
b = 10 ** 2 - 4 / 3
c = 6 / 3 + 1
d = 10 % 3 + 1 * 2

print(a)
print(b)
print(c)
print(d)
####
12
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
print(area)
####
13
a = float(input('Digite um numero 1: '))
b = float(input('Digite um numero 2: '))
soma= a+b
print(soma)
####
14
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = ((n1+n2)/2)
print(media)
####
15
a= float(input('Difite numero 1: '))
b= float(input('Digite numero 2: '))
c= float(input('Digite numero 3: '))
soma1= a*2
soma2= b*2
soma3= c*2
print(f'Resultado 1 {soma1}')
print(f'Resultado 2 {soma2}')
print(f'Resultado 3 {soma3}')
####
16
a,b = 10, 20
resultado = b, a
print(resultado)
####
17
messes = int(input('Digite a quantidade de messes: '))
soma = 30*messes
print (f'{soma} dias')
####
18
n1 = float(input('digite um numero: '))
ant= (f'{n1-1} antecessor')
suc= (f'{n1+1} sucessor')
print(ant,suc)
####
19
r=float(input('Digite o raio da esfera: '))
soma= (4/3) * 3.14 * r*3
print(f'Volume da esfera: {soma}')

####
20
altura = float(input('Digite a altura do triangulo: '))
base = float(input('Digite a base do triangulo: '))
soma = (base*altura)/2
print(f'Base do triângulo {soma}')
####
21 
compra= float(input('Digite o valor da compra: '))
desconto= float(input('Digite o valor do desconto: '))
soma= compra-(compra*(desconto/100))
print(f'valor da compra R${soma}')
####
22
nome= (input('Digite o nome do vendedor: '))
salario= float(input('Digite o salario fixo do vendedor: '))
vendas= int(input(f'Digite o total de vendas de {nome}: '))  

comissao: float= vendas * .15
salariot= salario + comissao

print(f' salario {salariot}')
