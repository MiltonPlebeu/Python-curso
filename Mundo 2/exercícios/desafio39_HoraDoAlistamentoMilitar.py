#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year

nascimento = int(input('Ano de nascimento '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE, por que completou {} anos'.format(idade))

elif idade < 18:
    tempo = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o seu alistamento'. format(tempo))

elif idade > 18:
    tempo = idade -18
    print('Voce ja deveria ter se alistado ah {} anos'.format(tempo))








