
pictures = []
control_rows = []
control_cols = []

with open("dane_obrazki.txt") as file:
    for i in range(200):
        pic = []
        control_row = ''
        control_col = ''


        for j in range(20):
            line = file.readline().strip()
            pic.append(line[0:20])
            control_row += line[20]
        control_col = file.readline().strip()
        file.readline()

        pictures.append(pic)
        control_rows.append(control_row)
        control_cols.append(control_col)

# for i, pic in enumerate(pictures):
#     print("Ilosc wierszy", len(pic))
#     for row in pic:
#         print('Szerokosc', len(row), end=": ")
#         print(row)
#     print()

print("Zadanie 1")
counter = 0
max1 = 0 # maksymalna ilosc jedynek
for pic in pictures:
    counter0 = 0 # licznik zer
    counter1 = 0 # licznik jedynek
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

print("Zadanie 2")

first = True
licznik = 0
for pic in pictures:
    rozne = False
    for i in range(10):
        for j in range(10):
            a = pic[i][j]
            b = pic[i][j+10]
            c = pic[i+10][j]
            d = pic[i+10][j+10]
            if not(a == b == c == d):
                rozne = True
    if rozne == False:
        licznik += 1
        if first:
            print("Pierwszy obrazek rekurencyjny")
            for line in pic[:20]:
                print(line[:20])
            first = False
print('Liczba rekurencyjnych:', licznik)
