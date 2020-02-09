from math import *

class Punkt:
    x = 0
    y = 0
    def przesun_o_wek(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
    def skaluj_OX(self,wsp):
        self.x = self.x * wsp
    # def obroc(self, kat):
    def obroc(self,kat):
        radiany = kat / 360 * 2 * 3.1416
        x1, y1 = self.x, self.y
        self.y = y1 * cos(radiany) + x1 * sin(radiany)
        self.x = x1 * cos(radiany) - y1 * sin(radiany)

    def zwroc_r(self):
        return sqrt(self.x**2 + self.y ** 2)

punkt1 = Punkt()
print(punkt1.x, punkt1.y)
punkt1.x = 5
print(punkt1.x, punkt1.y)
punkt1.przesun_o_wek(-3,5)
print(punkt1.x, punkt1.y)
punkt1.obroc(180)

r = punkt1.zwroc_r()
print(r)


