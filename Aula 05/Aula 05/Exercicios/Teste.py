numeros = [1,8,5,4,3,6,7,2,]
ma = 0
sequencia = []

for indice, numero in enumerate(numeros):
    if numero > ma:
        numero = ma
   
    if numero < ma:
        numero = ma
        sequencia.append(ma)
    else: 
        

print(sequencia)