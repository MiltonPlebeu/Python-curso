#Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem PARES. Se o
#valor digitado for IMPAR, desconsidere-o.
r = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 != 0:
        print('Valor IMPAR, DESCONSIDERADO')
    else:
        r += c
        print('A soma de {} + {} é: {}'.format(n, c, r))
        

