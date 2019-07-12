#Escreva um programa que pergunte o salário de um
#funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
#Para salários inferiores ou iguais, calcule um aumento de 15%

salario = float(input('Qual o seu salário R$:'))

if salario > 1.250:
    novosalario = (salario + ((salario * 10) / 100))
    print('Seu novo salário será de R${:.2f}'.format(novosalario))

else:
    novosalario = (salario + ((salario * 15) / 100))
    print('Seu novo salário será de R${:.2f}'.format(novosalario))
