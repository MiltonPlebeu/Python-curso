#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
#triângulo será formado:
#EQUILÁTERO: Todos os lados Iguais
#ISÓSCELES: Dois lados iguais
#ESCALENO: Todos os lados deferentes

reta1 = float(input('Digite o comprimento da Reta 1 '))
reta2 = float(input('Digite o comprimento da Reta 2 '))
reta3 = float(input('Digite o comprimento da Reta 3 '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os seguimentos acima PODEM FORMAR UM triângulo!')
    if reta1 == reta2 == reta3:
        print('Triangulo EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')

else:
    print('Os seguimentos acima NÃO PODEM FORMAR Triângulo')
