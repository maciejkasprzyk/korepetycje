slowa = []
with open("sygnaly.txt") as plik:
    for linia in plik:
        slowa.append(linia.strip())

# zadanie 1
przekaz = ""
for i in range(39,len(slowa),40):
    przekaz += slowa[i][9]
print(przekaz)

# zadanie 2
maks = 0
maks_indeks = 0
for i in range(len(slowa)):
    slowo = slowa[i]
    tablica = [0] * 100
    licznik = 0

    for litera in slowo:
        if(tablica[ord(litera)] == 0):
            tablica[ord(litera)] = 1
            licznik += 1
    if licznik > maks:
        maks = licznik
        maks_indeks = i
print(slowa[maks_indeks], maks)

# zadanie 3

for slowo in slowa:
    minimum = 100
    maksimum = 0
    for litera in slowo:
        kod = ord(litera)
        minimum = min(minimum, kod)
        maksimum = max(maksimum, kod)
    if maksimum - minimum <= 10:
        print(slowo)
