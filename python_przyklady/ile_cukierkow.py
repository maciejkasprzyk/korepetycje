def pobierz_dodatnia():
    n = int(input())
    while n <= 0:
        print("Podaj liczbe jeszcze raz.")
        n = int(input())
    return n


print("Podaj liczbe cukierkow:")
cukierki = pobierz_dodatnia()
print("Podaj liczbe dzieci:")
dzieci = pobierz_dodatnia()

print(f"Dzieci dostaną {cukierki // dzieci} cukierków")
print(f"Tata dostanie {cukierki % dzieci} cukierków")
