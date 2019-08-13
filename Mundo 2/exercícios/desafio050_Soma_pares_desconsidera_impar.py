#Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem PARES. Se o
#valor digitado for IMPAR, desconsidere-o.
r = 0
cont = 0
i = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        r += n
        cont +=1
print('Você informou {} números PARES e a soma deles é {} '.format(cont,r))

