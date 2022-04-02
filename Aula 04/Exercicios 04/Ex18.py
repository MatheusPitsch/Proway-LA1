a: int = 0
b: int = 0
c: int = 0
d: int = 0
for i in range(4):
    media = float(input('Digite a média do aluno: '))

    if media <= 4.9:
        d += 1
    elif media <= 6.9:
        c += 1
    elif media <= 8.9:
        b += 1
    elif media <= 10:
        a += 1

print(f'A:{a}')
print(f'B:{b}')
print(f'C:{c}')
print(f'D:{d}')
