ma: int = 0
me: int = 0
for i in range(5):

    valor = int(input('Digite um valor: ')) 

    if i == 1:
        me=ma=valor
    else:
        if valor > ma:
            ma = valor
        if valor < me:
            me = valor

print(ma)
print(me)