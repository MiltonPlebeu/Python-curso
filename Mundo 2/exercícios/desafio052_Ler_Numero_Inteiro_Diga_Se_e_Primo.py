#Faça um programa que leia um número inteiro e
#diga se ele é ou não um número primo.
total=0
numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi dividido {} vezes'.format(numero, total), end=' ')
if total == 2:
    print('\n ENTÃO É UM NÚMERO PRIMO!')
else:
    print('\n ENTÃO NÃO É UM NÚMERO PRIMO!')





