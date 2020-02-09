from math import sqrt


def f(x):
    return x**4/500 - x**2/200 - 3/250

def g(x):
    return x**3/30 - x/20 - 1/6

def calk(funkcja, min, max, epsilon):
    pole = 0
    while min <= max:
        pole += (funkcja(min) + funkcja(min + epsilon)) * epsilon / 2
        min += epsilon
    return pole

def obwod(funkcja, min, max, epsilon):
    obwod = 0
    while min <= max:
        obwod += sqrt(epsilon**2+(funkcja(min+epsilon)-funkcja(min))**2)
        min += epsilon
    return obwod

def pasy(f,g,min,max,epsilon):
    dl = 0
    while max > min:
        dl += (f(min) + g(min))//1
        min += epsilon
    return dl

def main():
    #zad.1
    pole =  calk(f,2,10,0.0001) + calk(g,2,10,0.0001)
    print(pole)

    #zad.2
    obw = 2*8 + 19+61/125 + 32+2/3
    print(obw)
    obw += obwod(f,2,10,8/1000) + obwod(g,2,10,8/1000)

    print("marek",obw)

    #zad.3
    print(pasy(f,g,2,10,1/4))


main()
