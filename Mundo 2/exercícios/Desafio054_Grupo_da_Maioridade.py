#Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
#No final mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.
#atual = date.today().year
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    anonasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = atual - anonasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print('{} Pessoas não atingiram a maioridade'.format(menores))
print('{} Pessoas já atingiram a maioridade'.format(maiores))


