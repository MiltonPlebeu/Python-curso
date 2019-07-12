preço = float(input('Digite o valor do produto: R$ '))
novo_preço = preço - (preço * 5 / 100)
print('O valor do produto de R$:{:.2f} com desconto de 5% é de: R$:{:.2f}'.format(preço, novo_preço))
