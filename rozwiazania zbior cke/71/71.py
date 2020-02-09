def f(x):
    if x < 1:
        wspolczynniki = tab[0]
    elif x < 2:
        wspolczynniki = tab[1]
    elif x < 3:
        wspolczynniki = tab[2]
    elif x < 4:
        wspolczynniki = tab[3]
    else:
        wspolczynniki = tab[4]
    wynik = 0
    for wsp in reversed(wspolczynniki):
        wynik *= x
        wynik += wsp
    return wynik

def bisekcja(a,b):
    s = (b + a) / 2
    while b - a > 0.000001:
        if f(a) * f(s) < 0:
            b = s
        else:
            a = s
        s = (b + a) / 2
    return round(s,5)


tab = []
with open("funkcja.txt") as plik:
    for linia in plik:
        print(linia.split())
        tab.append([float(x) for x in linia.split()])

print("zad 70.1")

print(round(f(1.5),5))

print("zad 70.2")

epsilon = 0.00001

x = 4
kon = 5
maxf = 0
maxx = 0
while x < kon:
    if maxf < f(x):
        maxf = f(x)
        maxx = x
    x += epsilon

print(round(maxx,3), round(maxf,5))

print("zad 71.3")

print(bisekcja(0,1), bisekcja(2,3), bisekcja(3,4), bisekcja(4,5))
