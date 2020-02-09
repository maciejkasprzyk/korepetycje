def zamien_na_10(liczba,podstawa):
    wynik = 0
    i = 0

    if liczba[0] == "-":
        i = i + 1

    while i < len(liczba):
        wynik = wynik * podstawa
        wynik = wynik + int(liczba[i])
        i += 1

    if liczba[0] == "-":
        return -wynik
    return wynik



godziny1 = []
temperatury1 = []


with open("../zadaniaZbior/rozwiazania/58/dane_systemy1.txt") as plik:
    for linia in plik:
        dane = linia.split()
        godzina = dane[0]
        temperatura = dane[1]
        godzina10 = zamien_na_10(godzina, 2)
        temperatura10 = zamien_na_10(temperatura, 2)
        godziny1.append(godzina10)
        temperatury1.append(temperatura10)

print(godziny1)
print(temperatury1)
