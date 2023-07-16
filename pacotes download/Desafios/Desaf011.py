h = float(input("Altura da parede em metros:"))
l = float(input('Largura da parede em metros:'))
a = h * l
t = a / 2
print('Sua parecde tem {:.2f}m x {:.2f}m, que corresponde a uma àrea de {:.2f}m²'.format(h, l, a))
print('Você irá precisar de {:.2f}l de tinta para realizar a pitura.'.format(t))



