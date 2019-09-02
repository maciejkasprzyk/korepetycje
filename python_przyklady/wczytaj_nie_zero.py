dzielna = int(input("Podaj dzielna:\n"))
dzielnik = int(input("Podaj dzielnik:\n"))
while dzielnik == 0:
    print("Nie wolno dzielić przez zero. Podaj dzielnik jeszcze raz:")
    dzielnik = int(input())

print(f"Iloraz to : {dzielna / dzielnik}")

iloraz = dzielna / dzielnik
print(iloraz)
