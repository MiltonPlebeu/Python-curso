# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela a seguir:
# 1 Abaixo de 18.5 : ABAIXO DO PESO
# 2 Entre 18.5 e 25: PESO IDEAL
# 3 De 25 até 30: SOBREPESO
# 4 De 30 até 40: OBESIDADE
# 5 Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Qual é seu peso (Kg) ?'))
altura = float(input('Qual é sua altura (m) ?'))

imc = peso / (altura ** 2) #o calculo do IMC é a divisão do peso por alrura ao quadrado.
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
