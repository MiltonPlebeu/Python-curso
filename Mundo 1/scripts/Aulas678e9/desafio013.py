sal_atual = float(input('Digite o salário atual: '))
sal_novo = sal_atual + (sal_atual * 15 / 100)
print('O salário de R${:.2f} com 15% de aumento será de R${:.2f}'.format(sal_atual, sal_novo))
