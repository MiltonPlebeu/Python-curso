#Análise de Strings
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro = Ana
#últino = Souza

nome = str(input('Digite um nome completo: ')).strip()
nomefatiado = nome.split()
print('Primeiro nome: {}'.format(nomefatiado[0]))
print('Último nome: {}'.format(nomefatiado[-1]))




