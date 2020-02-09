def polacz(lewa_lista, prawa_lista):

    if len(lewa_lista) == 0:
        return prawa_lista
    if len(prawa_lista) == 0:
        return lewa_lista

    indeks_lewej = indeks_prawej = 0
    polaczona_lista = []
    while True:
        if lewa_lista[indeks_lewej] <= prawa_lista[indeks_prawej]:
            polaczona_lista.append(lewa_lista[indeks_lewej])
            indeks_lewej += 1
        else:
            polaczona_lista.append(prawa_lista[indeks_prawej])
            indeks_prawej += 1

        if indeks_prawej == len(prawa_lista):
            # koniec listy prawej
            polaczona_lista += lewa_lista[indeks_lewej:]
            break
        elif indeks_lewej == len(lewa_lista):
            # koniec listy lewej
            polaczona_lista += prawa_lista[indeks_prawej:]
            break

    return polaczona_lista

def merge_sort(list):
    if len(list) <= 1:
        return list

    srodek = len(list) // 2
    lewa, prawa = list[:srodek], list[srodek:]
    return polacz(merge_sort(lewa), merge_sort(prawa))

print(merge_sort([3,5,7,2,1]))

