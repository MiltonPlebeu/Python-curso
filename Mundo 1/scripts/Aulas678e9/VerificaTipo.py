val = input("Digite alguma coisa: ")
print(type(val))
print('É Composto por letras maiusculas?',val.isupper())
print('É composto por letras ou números?',val.isalnum())
print('É composto por letras',val.isalpha())
print('É composto por números?',val.isnumeric())
print('É composto por decimais?',val.isdecimal())
print('É composto por dígitos?',val.isdigit())
print('É composto por letras minúsculas',val.islower())
print('É um título',val.istitle())
print('É possível imprimir',val.isprintable())
