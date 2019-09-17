def czy_artmetyczny(ciag):
    r = ciag[1] - ciag[0]
    i = 0
    while i < len(ciag) - 1:
        if ciag[i + 1] - ciag[i] != r:
            return False
        i += 1
    return True


def czy_szescian(liczba):
    i = 1
    szescian = 1
    while szescian < liczba:
        szescian = i ** 3  # i * i * i
        i += 1

    if szescian == liczba:
        return True
    return False


ciagi = []

with open("ciagi.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        n = int(line.strip())

        line = file.readline()
        if not line:
            break
        ciag = [int(x) for x in line.split()]
        ciagi.append(ciag)

print("zadanie 1")
maxiumum = 0
licznik = 0
for ciag in ciagi:
    if czy_artmetyczny(ciag):
        licznik += 1
        maxiumum = max(maxiumum, ciag[1] - ciag[0])

print(f"licznik: {licznik}\nmaximum: {maxiumum}")

print("zadanie 2")
for ciag in ciagi:
    maxi = 0
    for x in ciag:
        if czy_szescian(x):
            maxi = max(maxi, x)
    if maxi != 0:
        print(maxi)

print("zadanie 3")

bledne = []
with open("bledne.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        n = int(line.strip())

        line = file.readline()
        if not line:
            break
        ciag = [int(x) for x in line.split()]
        bledne.append(ciag)

# 5 4 5 6 7 8

for ciag in bledne:
    r = []
    i = 0
    while i < len(ciag) - 1:
        r.append(ciag[i + 1] - ciag[i])
        i += 1

    if r[0] != r[1] and r[1] == r[2]:
        print(ciag[0])
        continue
    if r[0] != r[2] and r[1] != r[2] and r[3] == r[2]:
        print(ciag[1])
        continue

    i = 0
    while i < len(r):
        if r[i] != r[0]:
            print(ciag[i + 1])
            break
        i += 1
