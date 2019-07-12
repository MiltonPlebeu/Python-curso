#A confederação nacional de natação precisa de um programa que leia o ano de
#nascimento de um atleta e mostre sua categoria de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER

from datetime import date
atual = date.today().year

anonascimento = int(input('Digite o ano de nascimento: '))
idade = atual - anonascimento
print('O atleta tem {}, anos '.format(idade), end='')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print(' Classificação JUNIOR')
elif idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('MASTER')
