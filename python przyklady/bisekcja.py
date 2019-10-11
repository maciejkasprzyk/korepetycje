import matplotlib.pyplot as plt


def bisekcja(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Niepoprawne dane")
        return

    while (b - a > epsilon):
        srodek = (a + b) / 2
        f_srodek = f(srodek)
        if f(a) * f_srodek < 0:
            b = srodek
        elif f(b) * f_srodek < 0:
            a = srodek
        elif f_srodek == 0:
            print("Znalezlismy dokladnie rozwiazanie")
            return srodek,srodek
        else:
            print("Blad, prawdopodobnie funkcja nie byla ciagla")
            return
        print(a,b)
    return a, b


def funkcja(x):
    return (x - 1) * (x - 4)


x = [i * 0.05 for i in range(100)]
y = [funkcja(i) for i in x]

plt.plot(x, y)
plt.show()

a, b = bisekcja(funkcja, 2, 100, 0.000001)
print(a,b)
