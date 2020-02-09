liczby = []
with open("przyklad.txt") as plik:
    for linia in plik:
        liczby.append(int(linia.strip()))

print(liczby)

print("zad 4.1")
licznik =0
for liczba in liczby:
    while liczba >= 3:
        liczba /= 3
    if liczba == 1:
        licznik +=1
print(licznik)

print("zad 4.2")
def silnia(n):
    if n == 0:
        return 1
    return silnia(n-1)*n

for liczba in liczby:
    liczba2 = liczba
    suma = 0
    while liczba > 0:
        ostatnia = liczba % 10
        suma += silnia(ostatnia)
        liczba //= 10
    if liczba2 == suma:
        print(liczba2)

print("zad 4.3")

def nwd(a,b):
    while(b > 0):
        a,b = b, a-b
    return a

def nwd_ciag(ciag):
    nwd_akt = ciag[0]
    for i in range(1,len(ciag)):
        nwd_akt = nwd(nwd_akt, ciag[i])
    return nwd_akt


maks = 0
for i in range(len(liczby)):
    for j in range(i,len(liczby)):
        podciag = []
        for k in range(i,j+1):
            podciag.append(liczby[k])
        akt_nwd = nwd_ciag(podciag)
        maks = max(akt_nwd,maks)
print(maks)
