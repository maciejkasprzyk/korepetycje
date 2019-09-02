
def nwd(a, b):
    while b:
        a, b = b, a%b
    return a
  

def main():
    numbers = []
    file = open("liczby.txt")
    for line in file:
        numbers.append(int(line.strip()))
    file.close()

    out = open("wyniki60.txt", "w")

    # zadanie 1
    out.write("Zadanie 1:\n")
    licznik = 0
    last = 0
    lastButOne = 0
    for number in numbers:
        if number < 1000:
            licznik += 1
            lastButOne = last
            last = number
    out.write(f"Jest {licznik} liczb < 1000. Dwie ostatnie to {lastButOne}, {last}.\n")

    # zadanie 2
    out.write("Zadanie 2\n")
    for number in numbers:
        # print(number)
        dividers = []
        for divider in range(1,number+1):
            if number % divider == 0:
                dividers.append(divider)

        if len(dividers) == 18:
            out.write(f"{number}: {dividers}\n")

    # zadanie 3
    out.write("Zadanie 3\n")
    maximum = 0
    for a in numbers:
        maxNwd = 1
        for b in numbers:
            if a != b:
                maxNwd = max( maxNwd, nwd(a,b) )
        if maxNwd == 1:
            maximum = max(maximum, a)     
    out.write(f"{maximum}\n")
    out.close()


if __name__ == '__main__':
    main()