vetor_1 = []
vetor_2 = []
vetor_3: int = []

for i in range(5):
    valor1 = int(input('Digite um valor1: '))
    vetor_1.append(valor1)
    
    valor2 = int(input('Digite um valor2: '))
    vetor_2.append(valor2)

for i in vetor_1:
    for j in vetor_2:
        if i == j:
            vetor_3.append(i)

print(vetor_1)
print(vetor_2)
print(vetor_3)
