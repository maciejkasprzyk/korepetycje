def read_data(path, base):
    temps = []
    hours = []
    with open(path) as file:
        for line in file:
            hour , temp = line.split()
            hours.append(int(hour, base))
            temps.append(int(temp, base))
    return hours, temps # aby zrozumieć ten zapis trzeba poczytać o tuple


h1, t1 = read_data("dane_systemy1.txt", 2) # h - hours, t - temps
h2, t2 = read_data("dane_systemy2.txt", 4)
h3, t3 = read_data("dane_systemy3.txt", 8)
print(t1)
print(t2)
print(t3)

# zad 1
print("Zadanie2")
min1 = min(t1)
min2 = min(t2)
min3 = min(t3)
print(f"Min temp w stacji S1: {format(min1, 'b')}") # nietety w ten sposób możemy formatować tylko do postawy 2 ('b'), 8 ('o') i 16 ('x')
print(f"Min temp w stacji S2: {format(min2, 'b')}") # jeżeli musielibyś wypisać wynik np w podstawie trójkowej musimy napisać własną funkcję
print(f"Min temp w stacji S3: {format(min3, 'b')}")

# zad 2

licznik = 0
oczekiwana = 12
for i in range(len(h1)):
    if h1[i] != oczekiwana and h2[i] != oczekiwana and h3[i] != oczekiwana:
        licznik += 1
    oczekiwana += 24
print(f"Zadanie 2:\n{licznik}")

# zad 3
max1 = t1[0]
max2 = t2[0]
max3 = t3[0]

licznik = 1
for i in range(len(t1)):
    bylRekord = False
    if t1[i] > max1:
        max1 = t1[i]
        bylRekord = True
    if t2[i] > max2:
        max2 = t2[i]
        bylRekord = True
    if t3[i] > max3:
        max3 = t3[i]
        bylRekord = True
    if bylRekord:
        licznik += 1

print(f"Zadanie 3:\n{licznik}")

# zadanie 4
maxSkok = 0
for i in range (len(t1)):
    for j in range(i+1, len(t1)):
        rij = (t1[i] - t1[j]) * (t1[i] - t1[j])
        skok = rij // (j - i)
        # sprytnie zaokrąglamy w góre; mozna użyć do tego wbudowanej funkcji pythonowej, ale nie zawsze się pamięta składnię
        if skok * (j - i) < rij:
            skok += 1
        maxSkok = max(maxSkok, skok)

print(f"Zad 4\n{maxSkok}")
