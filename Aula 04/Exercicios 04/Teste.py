soma: int = 0
while (True): # Loop infinito
    valor: int = int(input("Digite um número: "))

    if valor < 0 :
        break

    soma += valor
    
print(f"Soma: {soma}")