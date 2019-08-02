#Faça um programa que calcule a soma entre todos os
#NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se
#encontram no intervalo de 1 até 500
r = 0 #resultado da soma dos valores
cont = 0 # soma quantidade de valores solicitados no intervalo de 1 a 501 divisiveis por 3
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        r += c
        #print(c, end=' ')
print('A soma de todos os {} valores solicitados é {}'.format(cont, r))

