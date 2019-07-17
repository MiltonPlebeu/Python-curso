from random import choice

print('{:=^100}'.format('\033[1;31;m Play Jokempô \033[m'))
print("""
[1] PEDRA
[2] PAPEL
[3] TESOURA
""")
opcao = int(input('ESCOLHA UMA OPÇÃO:'))

lista = ['1', '2', '3']
escolhadopc = choice(lista)
print('Escolha do Computador >>> {}'.format(escolhadopc))

if opcao == 1 and escolhadopc == 2:
    print('O computador venceu por ter escolhido PAPEL')

elif opcao == 1 and escolhadopc == 3:
    print('Você venceu por ter escolhido a PEDRA')
else:
    print('Tente novamente')


