#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
#e R$0,45 para viagens mais longas.

dkm = float(input('Qual a distância da viagem em KM: '))
if dkm <= 200:
    Precopassagem1 = dkm * 0.50
    print('O valor da passagem é R${:.2f}'.format(Precopassagem1))

else:
    Precopassagem2 = dkm * 0.45
    print('O valor da passagem é R${:.2f}'.format(Precopassagem2))


