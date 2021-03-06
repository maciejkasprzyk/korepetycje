# funkcja obliczająca ile jest dzielników pierwszych
def policz_ile_dzielnikow(liczba):
    liczba_dzielnikow = 0
    dzielnik = 3
    while dzielnik * dzielnik < liczba:  # jeżeli liczba n ma dzielnik różny niz
        # jeden i n to znajduję się on w przedziale 1...pierwiastek(n)
        if liczba % dzielnik == 0:
            liczba_dzielnikow += 1
        # zrobiłem tak aby while był po if'ie a nie wewnątrz, wydaję się czytelniej a nie powinno nic zmienić
        while liczba % dzielnik == 0:
            liczba //= dzielnik  # inaczej: liczba = liczba // dzielnik
        dzielnik += 1

    if liczba > 1:
        liczba_dzielnikow += 1

    return liczba_dzielnikow


def zadanie1(liczby):
    wynik = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            continue  # continue sprawia, że pętla od razu przechodzi do kolejnego obrotu, pomijając cały dalszy kod
        dzielniki = policz_ile_dzielnikow(liczba)
        if dzielniki == 3:
            wynik += 1
    print(f"Zadanie 1:\n{wynik}")


def odwroc(liczba):
    return int(str(liczba)[::-1])

def zadanie2(liczby):
    wynik = 0
    for liczba in liczby:
        suma = liczba + odwroc(liczba)
        if suma == odwroc(suma):
            wynik += 1
    print(f"Zadanie 2:\n{wynik}")


def iloczyn_cyfr(x):
    iloczyn = 1
    s = str(x)
    for c in s:
        cyfra = int(c)
        iloczyn *= cyfra
    return iloczyn

def iloczyn_cyfr2(x):
    iloczyn= 1
    while x > 0:
        iloczyn *= x % 10
        x //= 10

    return iloczyn

def licz_moc(x):
    moc = 1
    x = iloczyn_cyfr2(x)
    while x > 9:
        x = iloczyn_cyfr2(x)
        moc += 1
    return moc

def zadanie3(liczby):
    wyniki = [0, 0, 0, 0, 0, 0, 0, 0]

    minimum = 9999999999999999
    maximum = 0
    for liczba in liczby:
        moc = licz_moc(liczba)
        if moc < 9:
            wyniki[moc - 1] += 1
        if moc == 1:
            maximum = max(maximum, liczba)
            minimum = min(minimum, liczba)

    print("Zadanie 3:")
    for index, wynik in enumerate(wyniki):
        print(f"{index + 1} {wynik}")
    print(f"Max {maximum}, min {minimum}")


# wczytywanie danych
liczby = []

with open("liczby.txt") as plik:
    for linia in plik:
        linia_bez_n = linia.strip() # "123312" -> 123312
        x = int(linia_bez_n)
        liczby.append(x)

zadanie1(liczby)
zadanie2(liczby)
zadanie3(liczby)

