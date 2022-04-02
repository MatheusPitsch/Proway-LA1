repeticao = int(input('Digite um número: '))

for i in range(repeticao + 1):
   
    if i % 2 == 0:
        print(f'{i} é par')
    
    else:
        print(f'{i} é impar')