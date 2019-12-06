# import sys
# sys.stdout = open("wyniki.txt", mode='w')

lista = []
with open("liczby.txt") as plik:
    for linia in plik:
        lista.append(linia.strip())

suma = 0
for liczba in lista:
    zera = 0
    for cyfra in liczba:
        if cyfra == '0':
            zera += 1
    if zera > len(liczba) - zera:
        suma += 1
print(suma)

przez2 = 0
for liczba in lista:
    if liczba[len(liczba) - 1] == '0':
        przez2 += 1
print(przez2)

przez8 = 0
for liczba in lista:
    io = len(liczba)
    if liczba[io-1] == liczba[io-2] == liczba[io-3] == '0':
        przez8 += 1
print(przez8)

# s8 = 0
# for liczba in lista:
#     if int(liczba,2) % 8 == 0:
#         s8 += 1
# print(s8)



imin, min = 0, lista[0]

for i in range(len(lista)):
    liczba = lista[i]

for i, liczba in enumerate(lista):
    # print(i,liczba)
    if(len(liczba) < len(min)):
        imin, min = i, liczba
    elif len(liczba) == len(min):
        for j in range(len(liczba)):
            if min[j] != liczba[j]:
                if min[j] == '1':
                  imin, min = i, liczba
                else:
                    break
print(imin + 1)


imaks, maks = 0, lista[0]
for i, liczba in enumerate(lista):
    # print(i,liczba)
    if(len(liczba) > len(maks)):
        imaks, maks = i, liczba
    elif len(liczba) == len(maks):
        for j in range(len(liczba)):
            if maks[j] == '1' and liczba[j] == '0':
                break
            if maks[j] == '0' and liczba[j] == '1':
                imaks, maks = i, liczba
print(imaks + 1)
