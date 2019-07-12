nome = str(input('Digite um nome completo: ')).strip()
print(nome)
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}:'.format(nome.upper()))
print('Seu nome em minúsculas é {}:'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome têm {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} ele tem {} letras'.format(separa[0], len(separa[0])))






