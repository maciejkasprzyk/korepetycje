# zadanie 1
print("Zadanie 1")
with open("dane_6_1.txt") as plik:
    slowa = [linia.strip() for linia in plik]
k = 107
k = k % (26)
for slowo in slowa:
    nowe = ""
    for litera in slowo:
        kod = (ord(litera) + k)
        if kod > ord('Z'):
            kod -= 26
        nowe += chr(kod)
    print(nowe)

# zadanie 2
print("Zadanie 2")

with open("dane_6_2.txt") as plik:
    dane = [linia.split() for linia in plik]

for slowo, k in dane:
    k = int(k) % 26
    for litera in slowo:
        kod = ord(litera) - k
        if kod < 65:
            kod += 26
        print(chr(kod), end="")
    print()



# zadanie 3
print("Zadanie 3")
with open("dane_6_3.txt") as plik:
    slowa = [linia.split() for linia in plik]

for s1, s2 in slowa:
    k = ord(s1[0]) - ord(s2[0])
    if k < 0:
        k += 26
    for i in range(1, len(s1)):
        x = ord(s1[i]) - ord(s2[i])
        if x < 0:
            x += 26
        if x != k:
            print(s1)
            break

