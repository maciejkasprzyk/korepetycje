
pictures = []
with open("dane_obrazki.txt") as file:
    for _ in range(200):
        pic = []
        for i in range(21):
            line = file.readline()
            pic.append(line.strip())
        file.readline()
        pictures.append(pic)

# sprawdzmy czy poprawnie wczytalismy
# for i, pic in enumerate(pictures):
#     print("Ilosc wierszy", len(pic))
#     for line in pic:
#         print('Szerokosc', len(line), end=": ")
#         print(line)
#     print()
# koniec wypisywania


# --------------- Zadanie 1
print("Zadanie 1")
counter = 0
max1 = 0
for pic in pictures:
    counter0 = 0
    counter1 = 0
    for i in range(20):
        for j in range(20):
            if pic[i][j] == '0':
                counter0 += 1
            else:
                counter1 += 1
    if counter1 > counter0:
        counter += 1
    max1 = max(max1, counter1)

print("Liczba rewersow", counter)
print("Max czarnych pikseli", max1)
# --------------- koniec zadania1


# --------------- Zadanie 2
print("Zadanie 2")

# test = [i for i in range(21)]
# print(test[:10])
# print(test[10:20])

counter = 0
first = True

for pic in pictures:
    upper_half = pic[:10]
    lower_half = pic[10:20]

    part1 = []
    part2 = []
    for line in upper_half:
        part1.append(line[0:10])
        part2.append(line[10:20])
    part3 = []
    part4 = []
    for line in lower_half:
        part3.append(line[0:10])
        part4.append(line[10:20])

    if part1 == part2 == part3 == part4:
        counter += 1
        if first:
            print("Pierwszy obrazek rekurencyjny")
            for line in pic[:20]:
                print(line[:20])
            first = False
print('Liczba rekurencyjnych:', counter)

# --------------- koniec zadania2

# --------------- zadanie 3 i 4
zad4 = []

poprawne = 0
naprawialne = 0
nienaprawiane = 0

for picID, pic in enumerate(pictures):

    row_errors = 0
    row = -999
    for i in range(20):
        counter1 = 0
        for j in range(21):
            if pic[i][j] == '1':
                counter1 += 1
        if counter1 % 2 == 1:
            row_errors += 1
            # do zadania 4
            row = i

    col_errors = 0
    col = -999
    for i in range(20):
        counter1 = 0
        for j in range(21):
            if pic[j][i] == '1':
                counter1 += 1
        if counter1 % 2 == 1:
            col_errors += 1
            # do zadania 4
            col = i

    if row_errors == col_errors == 0:
        poprawne += 1
    elif row_errors <= 1 and col_errors <= 1:
        naprawialne += 1
        # do zad 4
        if row_errors == 1 and col_errors == 1:
            zad4.append((picID + 1, row + 1, col + 1))
        if row_errors == 0 and col_errors == 1:
            zad4.append((picID + 1, 21, col + 1))
        else:
            zad4.append((picID + 1, row + 1, 21))

    else:
        nienaprawiane += 1

print("poprawne", poprawne)
print("naprawialne", naprawialne)
print("nienaprawialne", nienaprawiane)

for x in zad4:
    print(x)



