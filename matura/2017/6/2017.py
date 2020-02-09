with open("dane.txt") as plik:
    obrazek = [[int(x) for x in linia.split()] for linia in plik]

maksimum = max([max(wiersz) for wiersz in obrazek])
minimum = min([min(wiersz) for wiersz in obrazek])

print(maksimum,minimum)


suma = 0
for wiersz in obrazek:
    for i in range(320):
        tyl = 319 - i
        if wiersz[i] != wiersz[tyl]:
            suma += 1
            break
print(suma)

for wiersz in obrazek:
    wiersz.append(128)
    wiersz.insert(0,128)
obrazek.append([128 for _ in range(322)])
obrazek.insert(0,[128 for _ in range(322)])

def f(x,y):
    if abs(x-y) > 128:
        return True
    return False

kontrastowe = 0
for i in range(1,201):
    for j in range(1,321):
        if f(obrazek[i][j],obrazek[i+1][j]):
            kontrastowe += 1
        elif f(obrazek[i][j],obrazek[i-1][j]):
            kontrastowe += 1
        elif f(obrazek[i][j],obrazek[i][j-1]):
            kontrastowe += 1
        elif f(obrazek[i][j],obrazek[i][j+1]):
            kontrastowe += 1
print(kontrastowe)

for j in range(320):
    for i in range(200):
        pass
