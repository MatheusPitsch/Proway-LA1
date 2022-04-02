i=1

par=impar=0

for i in range(5):
   
    i = int(input('Digite um número: '))
    
    if i % 2 == 0:
        par = par + 1
   
    else:
        impar = impar + 1

print(f'Você Digitou {par} números pares e {impar} números impares')