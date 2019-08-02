from random import randint
from time import sleep
import emoji


print('{:=^100}'.format("\033[1;31;m Play Jokempô \033[m" + emoji.emojize("\033[1;31;m :sunglasses: \033[m", use_aliases=True)))
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
jogador = int(input('ESCOLHA UMA OPÇÃO:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print("-=" * 14)
print('O computador escolheu: \033[1;31;m {} \033[m'.format(lista[computador]))
print('O jogador escolheu: \033[1;31;m {} \033[m'.format(lista[jogador]))
print("-=" * 14)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print("VITÓRIA DO JOGADOR!")
    elif jogador == 2:
        print("VITÓRIA DO COMPUTADOR!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: # computador jogou PAPEL
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print("VITÓRIA DO COMPUTADOR!")
    elif jogador == 2:
        print("VITÓRIA DO JOGADOR!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print("VITÓRIA DO JOGADOR!")
    elif jogador == 1:
        print("VITÓRIA DO COMPUTADOR!")
    else:
        print("JOGADA INVÁLIDA!")
