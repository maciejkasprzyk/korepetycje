
class P():
    def __init__(self,id,nazwa,marka,zapach,cena):
        self.id = id
        self.nazwa = nazwa
        self.marka = marka
        self.zapach = zapach
        self.cena = int(cena)
        self.sklad = []

    def __str__(self):
        return f"{self.nazwa}, {self.marka}, {self.zapach}, {self.cena}, {self.sklad}"


with open('marki.txt') as plik:
    plik.readline()
    marki = [linia.strip().split('\t')[1] for linia in plik]
print(marki)

perfumy = []
with open('perfumy.txt') as plik:
    plik.readline()
    for linia in plik:
        id, nazwa, id_marki, zapach, cena = linia.strip().split('\t')
        indeks = int(id_marki[2:]) - 1
        perfumy.append(P(id, nazwa, marki[indeks], zapach, cena))


with open('sklad.txt') as plik:
    plik.readline()
    for linia in plik:
        id_perfum , skladnik = linia.strip().split('\t')
        indeks = int(id_perfum[2:]) - 1
        perfumy[indeks].sklad.append(skladnik)

for p in perfumy:
    print(p)

print("zad 6.1")
for p in perfumy:
    for s in p.sklad:
        if s == 'absolut jasminu':
            print(p.nazwa)

print("zad 6.2")
dict = {}
for p in perfumy:
    if p.zapach in dict:
        dict[p.zapach] = min(dict[p.zapach],p.cena)
    else:
        dict[p.zapach] = p.cena

for p in perfumy:
    if p.cena == dict[p.zapach]:
        print(p.zapach,p.cena,p.nazwa)

print("zad 6.3")
zle_marki = set()
for p in perfumy:
    for skladnik in p.sklad:
        if 'paczula' in skladnik:
            zle_marki.add(p.marka)

dobre_marki = set()
for p in perfumy:
    if p.marka not in zle_marki:
        dobre_marki.add(p.marka)

for m in sorted(dobre_marki):
    print(m)

print("zad 6.4")
wynik = []
for p in perfumy:
    if p.marka == 'Mou De Rosine' and p.zapach == 'orientalno-drzewna':
        wynik.append((p.cena*0.85,p.nazwa))
wynik = sorted(wynik)
for cena , nazwa in wynik:
    print(nazwa,cena)

print("zad 6.4")
