
def binarne(lista, lewy ,prawy, szukana):
    if lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == szukana:
            return srodek
        if lista[srodek] < szukana:
            return binarne(lista,srodek + 1, prawy, szukana)
        else:
            return binarne(lista, lewy, srodek -1, szukana)
    return -1

def main():
    lista = [1,3,4,5,6,10,12,15,17,20,25,27,30]
    print(binarne(lista, 0, len(lista), 3))

if __name__ == '__main__':
    main()
