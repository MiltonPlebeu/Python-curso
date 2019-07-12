#Faça um programa que leia três números e
#mostre qual é o MAIOR e qual é o MENOR

import math

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

lista = [n1, n2, n3]
print('O maior número é:', max(lista))
print('O menor número é :', min(lista))



