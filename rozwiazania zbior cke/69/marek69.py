def main():
    genotyp = []
    with open ("dane_geny.txt") as plik:
        for linia in plik:
            genotyp.append(linia.strip())

    #zad.4
    silnie_odp = 0
    odp = 0
    for i in range (len(genotyp)-1):
        if genotyp[i] == genotyp[i][::-1]:
            silnie_odp += 1

        gen = genotyp[i]
        odwr_gen = genotyp[i][::-1]
        gen += 'C'
        odwr_gen += 'C'
        for x in range (len(gen)-1):
            if gen[x] == 'A' and gen[x+1] == 'A':
                pocz = x
                for y in range (i,len(gen)-1):
                    if gen[y] == 'B' and gen[y+1] == 'B':
                        koniec = y

main()

