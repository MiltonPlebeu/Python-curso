#Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA
#para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1
#segundo entre eles.
from time import sleep
import emoji

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

print(emoji.emojize('Fogos! Fogos! Fogos! :smile:', use_aliases=True))

