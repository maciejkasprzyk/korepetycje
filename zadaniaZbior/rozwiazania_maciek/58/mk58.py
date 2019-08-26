def wczytaj_dane(path):
    temps = []
    hours = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            temp , hour = line.split()
            print (temp + " " + hour)
            


wczytaj_dane("dane_systemy1.txt")