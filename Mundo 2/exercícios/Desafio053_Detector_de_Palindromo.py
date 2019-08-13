#Crie um programa que leia uma FRASE qualquer
#e diga se ela é um PALÍNDROMO, desconsiderando os espaços
# Exemplos de PALÍNDROMOS
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
#Com FOR
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''

#SEM FOR
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Tem um palíndromo')
else:
    print('Não forma um palíndromo')




