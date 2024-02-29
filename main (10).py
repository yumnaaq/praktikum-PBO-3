class Koordinat2D:
    X = 0
    Y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Koordinat3D(Koordinat2D):
    z = 0
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def tampilkan_koord(self):
        print('x =', self.x)
        if hasattr(self, 'y'):
            print('y =', self.y)
        print('z =', self.z)

titik1 = Koordinat3D(1, 2, 3)

print('Koordinat awal:')
titik1.tampilkan_koord()
delattr(titik1, 'z')
print('\nEfek fungsi delattr():')
titik1.tampilkan_koord()
del titik1.y
print('\nEfek keyword del:')
titik1.tampilkan_koord()

