#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
        print("Você foi multado! O valor da multa é R${:.2f}".format((velocidade - 80) * 7 ))
else:
    print("Parabéns! Você está no limite permitido!")


