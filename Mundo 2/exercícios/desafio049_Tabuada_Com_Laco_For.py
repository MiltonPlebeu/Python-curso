#Refaça o DESAFIO 009, mostrando a tabuada de um número
#que o usuário escolher, só que agora utilizando um laço for.
#r = 0
#n = int(input('Digite um número para ver sua tabuada: '))
#for c in range(1, 11):
#    r = n*c
#    print('{}x{}={}'.format(n, c, r))
#Usando apenas 3 linhas
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))

