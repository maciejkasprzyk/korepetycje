def pobierz_dodatnia(string):
    n = int(input(string))
    while n <= 0:
        print("Podaj liczbe jeszcze raz.")
        n = int(input())
    return n


cukierki = pobierz_dodatnia("Podaj liczbe cukierkow:\n")
dzieci = pobierz_dodatnia("Podaj liczbe dzieci:\n")

print(f"Dzieci dostaną {cukierki // dzieci} cukierków")
print(f"Tata dostanie {cukierki % dzieci} cukierków")
