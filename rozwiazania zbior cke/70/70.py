from math import sqrt


def f(x):
    return x ** 4 / 500 - x ** 2 / 200 - 3 / 250


def g(x):
    return (-x ** 3 / 30) + (x / 20) + 1 / 6


print("zad 70.1")

gora = 19 + 61 / 125
dol = -32 - 2 / 3
pole_prostokata = (gora - dol) * 8
print(pole_prostokata)

skok = 0.00001
pole1 = 0
x = 2
while x < 10 - skok:
    podstawa1 = abs(gora - f(x))
    podstawa2 = abs(gora - f(x + skok))
    pole1 += (podstawa1 + podstawa2) / 2 * skok
    x += skok

pole2 = 0
x = 2
while x < 10 - skok:
    podstawa1 = abs(dol - g(x))
    podstawa2 = abs(dol - g(x + skok))
    pole2 += (podstawa1 + podstawa2) / 2 * skok
    x += skok

print(pole_prostokata, pole1, pole2)
print(round(pole_prostokata - pole1 - pole2, 3))

print("zad 70.2")


def dl_krzywej(funkcja, a, b):
    krok = (b - a) / 1000
    wynik = 0
    while a < b:
        wynik += sqrt((krok) ** 2 + (funkcja(a) - funkcja(a + krok)) ** 2)
        a += krok
    return wynik


obwod = abs(gora - dol) + 8 * 2
print(obwod)
obwod += dl_krzywej(f, 2, 10) + dl_krzywej(g, 2, 10)
print(obwod)

print("zad 70.3")

krok = 0.25
x = 10 - krok
suma = 0
while x > 2:
    suma += (abs(f(x) - g(x)))//1
    x -= krok
print(suma)
