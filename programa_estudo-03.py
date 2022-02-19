# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
print('# Exemplo 01')
n = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n + n2) / 2
print(' De acordo com suas notas, sua media será', m)

print('# Exemplo 02')
n = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(' De acordo com suas notas, sua media será {}'.format((n + n2) / 2))

print('# Exemplo 03 usando for')
media = 0
soma = 0
for c in range(1, 3):
    nota_1 = float(input('a {}° nota é: '.format(c)))
    soma += nota_1
    media = soma / c
print('De acordo com suas notas sue média é {}'.format(media))
