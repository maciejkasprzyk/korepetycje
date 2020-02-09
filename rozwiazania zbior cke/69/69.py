dane = []
with open("dane_geny.txt") as plik:
    for linia in plik:
        dane.append(linia.strip())
print(dane)

print("zadanie 69.1")

zlicz = [0] * 501

for genotyp in dane:
    zlicz[len(genotyp)] += 1

suma = 0
for x in zlicz:
    if x != 0:
        suma += 1
print(suma)
print(max(zlicz))

print("zadanie 69.2")

# BCDDC

licznik = 0

for genotyp in dane:
    geny = []
    i = 0
    while i < len(genotyp) - 1:
        if genotyp[i:i + 2] == 'AA':
            for j in range(i + 2, len(genotyp) - 1):
                if genotyp[j:j+2] == 'BB':
                    geny.append(genotyp[i:j+2])
                    i = j + 2
                    break
            j += 1
        i += 1
    for gen in geny:
        if "BCDDC" in gen:
            licznik += 1
            break
print("suma: ", licznik)

print("zadanie 69.3")

maksymalna_liczba_genow = 0
najdluzszy_gen = 0
for genotyp in dane:
    geny = []
    i = 0
    while i < len(genotyp) - 1:
        if genotyp[i:i + 2] == 'AA':
            for j in range(i + 2, len(genotyp) - 1):
                if genotyp[j:j+2] == 'BB':
                    geny.append(genotyp[i:j+2])
                    najdluzszy_gen = max(najdluzszy_gen, j + 2 - i)
                    i = j + 2
                    break
            j += 1
        i += 1
    maksymalna_liczba_genow = max(maksymalna_liczba_genow,len(gen))

print(maksymalna_liczba_genow)
print(najdluzszy_gen)

print("zadanie 69.4")

palindorymy = 0
for genotyp in dane:
    if genotyp == genotyp[::-1]:
        palindorymy += 1
print("silnie oporne", palindorymy)

oporne = 0

for k,genotyp in enumerate(dane):
    geny = []
    geny_od_konca = []
    i = 0
    while i < len(genotyp) - 1:
        if genotyp[i:i + 2] == 'AA':
            for j in range(i + 2, len(genotyp) - 1):
                if genotyp[j:j+2] == 'BB':
                    geny.append(genotyp[i:j+2])
                    i = j + 2
                    break
            j += 1
        i += 1

    i = 0
    genotyp = genotyp[::-1]
    while i < len(genotyp) - 1:
        if genotyp[i:i + 2] == 'AA':
            for j in range(i + 2, len(genotyp) - 1):
                if genotyp[j:j+2] == 'BB':
                    geny_od_konca.append(genotyp[i:j+2])
                    i = j + 2
                    break
            j += 1
        i += 1

    if geny == geny_od_konca:
        # print(k)
        oporne += 1


print("oporne", oporne)
