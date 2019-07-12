largura = float(input('Largura da parede:'))
altura  = float(input('Altura da parede:'))
área = largura * altura
qt_tinta = área / 2
print('Dada a largura {:.2f} e altura {:.2f}, sua área total é de {:.2f}m2'.format(largura, altura, área))
print('Para pintar {:.2f}m2 serão necessários {:} litros de tinta'.format(área, qt_tinta))
