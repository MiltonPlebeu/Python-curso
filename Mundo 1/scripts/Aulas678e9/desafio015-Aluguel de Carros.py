d = int(input('Digite quantos dias de locação: '))
km = float(input('Digite quantos KM rodados: '))
pd = d * 60
pkm = km * 0.15
pt = pd + pkm
print('O valor a pagar pelo aluguel é de R$ {:.2f}'.format(pt))



