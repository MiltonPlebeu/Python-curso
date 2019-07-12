#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem:
#O primeiro é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor :'))

if val1 > val2:
    print('O primeiro valor é maior')
elif val2 > val1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')