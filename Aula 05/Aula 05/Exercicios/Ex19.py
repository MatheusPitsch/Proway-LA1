
texto = "Sem trocar que o espinho é seco.\n Sem trocar que seco é ser sol.\n Sem trocar que algum espinho seco secará."
texto_vetor = texto.split(' ')

print(texto)
print(texto_vetor)


for i, palavra in enumerate(texto_vetor):
    if palavra == 'trocar':
        texto_vetor[i] = 'sacar'
    
print(texto_vetor)

texto = ' '.join(texto_vetor)
print(texto)

print(texto.replace("sacar", "trocar"))