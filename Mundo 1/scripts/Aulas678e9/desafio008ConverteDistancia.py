media = float(input('Digite uma distância em metros: '))
cm = media * 100
mm = media * 1000
km = media / 1000
hm = media / 100
dam = media / 100
print('A medida em {}m corresponde a {:.0f}cm , {:.0f}mm , {}Km , {}hm , {}dam'.format(media, cm, mm, km, hm, dam))