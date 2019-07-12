#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
# 1 À vista dinheiro/cheque: 10% de desconto
# 2 À vista no cartão: 5% de desconto
# 3 Em até 2x no cartão: preço normal
# 4 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Preço das compras: R$ '))
print(''' ESCOLHA UMA FORMA DE PAGAMENTO A SEGUIR:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros ''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
