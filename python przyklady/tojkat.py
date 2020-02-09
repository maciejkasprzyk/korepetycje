


def czy_mozna_zbudowac_trojkat(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def trojkat(lista):
    wynik = 0
    for i in range(len(lista) - 2):
        print(lista[i], lista[i+1], lista[i+2])

        if czy_mozna_zbudowac_trojkat(lista[i], lista[i + 1], lista[i + 2]):
            wynik = wynik + 1
    return wynik


lista = [2, 3, 3, 1, 1, 7, 7, 3]
print(len(lista))
print(trojkat(lista))
