from random import choic
#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador
#
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

n1 = 0
n2 = 1
n3 = 3
n4 = 4
n5 = 5

lista = [n1, n2, n3, n4, n5]
nsorteado = choice(lista)
print('Escolhendo um número entre 0 e 5 ......')
numero = int(input('Qual foi o número que escolhi? '))
if numero == nsorteado:
    print('Número escolhido pelo computador {}'.format(nsorteado))
    print('Número sorteado {}, Parabens! Você acertou!'.format(numero))
else:
    print('Número escolhido pelo computador {}'.format(nsorteado))
    print('Você errou! Tente novamente e boa sorte.')









