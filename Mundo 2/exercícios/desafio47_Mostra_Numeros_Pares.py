#Crie um programa que mostre na tela TODOS OS NÚMEROS PARES
#que estão no intervalo em 1 e 50

#Resolução 1 com mais iterações, mais processamento.
r = 0
for c in range(1, 51):
    print('.', end=' ')
    if (c % 2 == 0):
        r = c
        print(r, end=' ')
print('Fim')

#Resolução 2 com menos processamento
for n in range(2, 51, 2):
    print('.', end=' ')
    print(n, end=' ')
print('Fim')


