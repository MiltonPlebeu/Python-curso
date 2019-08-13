# Desenvolva um programa que leia o NOME, IDADE e SEXO de
# 4 pessoas. No final do programa, mostre:
#   => A média de idade do grupo.
#   => Quantas mulheres têm menos de 20 anos
#   => Qual o nome do homem mais velho.
somaIdade = 0
mediaIdade = 0
somaIdadeHomem = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulherMenor20 = 0
for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade+= idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Fm' and idade < 20:
        mulherMenor20 += 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulherMenor20))
