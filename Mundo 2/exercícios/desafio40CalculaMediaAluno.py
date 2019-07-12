#Crie um programa que leia duas notas de um aluno e calcule
#sua média, mostrando uma mensagem no final, de acordo com a média
#atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.1 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

soma = (nota1 + nota2)
media = soma / 2
print('{} é a somada de  nota 1 e nota 2, média {}'.format(soma, media))

if media <= 5.0:
    print('REPROVADO!')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
