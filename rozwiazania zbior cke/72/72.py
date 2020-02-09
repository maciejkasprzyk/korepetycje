napisy = []
with open("napisy.txt") as plik:
    for linia in plik:
        napisy.append(linia.split())

print("zad 72.1")

pierwszy = True
licznik = 0
for a,b in napisy:
    if len(a) * 3 <= len(b) or len(a) >= len(b) * 3:
        licznik += 1
        if pierwszy:
            print(a,b)
            pierwszy = False
print(licznik)

print("zad 72.2")

for a,b in napisy:
    if b[:len(a)] == a:
        print(a,b, b[len(a):])

print("zad 72.3")

def dl_koncowki(a, b):
    licznik = 0
    for i in range(min(len(a), len(b))):
        if a[len(a)-1-i] == b[len(b)-1-i]:
            licznik += 1
        else:
            break
    return licznik

maxx = 0
for a,b in napisy:
    maxx = max(maxx, dl_koncowki(a,b))
print(maxx)

for a,b in napisy:
    if dl_koncowki(a, b)== maxx:
        print(a,b)

print([i for i in range(5,-1,-1)])
