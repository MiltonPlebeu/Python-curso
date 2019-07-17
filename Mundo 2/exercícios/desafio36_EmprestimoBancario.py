#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
#será negado.

valorCasa = float(input('Valor da casa: R$ '))
valorSalario = float(input('Salário do comprador: R$ '))
quantosAnos = int(input('Quantos anos de financiamento ? '))
prestacao = valorCasa / (quantosAnos * 12)
minimo = (valorSalario * 30) / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, quantosAnos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao >= minimo:
    print('Crédito Reprovado!')

else:
    print('Crédito Aprovado')






