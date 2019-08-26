# funkcja obliczająca ile jest dzielników pierwszych
def policz_ile_dzielnikow(liczba):
    liczba_dzielnikow = 0
    dzielnik = 2
    while dzielnik * dzielnik < liczba:  # jeżeli liczba n ma dzielnik różny niz jeden i n to znajduję się on w przedziale 1...pierwiastek(n)
        if liczba % dzielnik == 0:
            liczba_dzielnikow += 1
        # zrobiłem tak aby while był po if'ie a nie wewnątrz, wydaję się czytelniej a nie powinno nic zmienić
        while liczba % dzielnik == 0:
            liczba //= dzielnik  # inaczej: liczba = liczba // dzielnik
        dzielnik += 1

    if liczba > 1:
        liczba_dzielnikow += 1

    return liczba_dzielnikow


def podpunkt_a(liczby):
    wynik = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            continue  # continue sprawia, że pętla od razu przechodzi do kolejnego obrotu, pomijając cały dalszy kod
        dzielniki = policz_ile_dzielnikow(liczba)
        if dzielniki == 3:
            wynik += 1
    print(f"Zadanie 1:\n{wynik}")

def podpunkt_b(liczby):
    for liczba in liczby:
        s = str(liczba)

        print()

# wczytywanie danych
liczby = []
with open("dane/59/liczby.txt") as plik:
    for linia in plik:
        liczby.append(int(linia.strip()))

podpunkt_a(liczby)
podpunkt_b(liczby)