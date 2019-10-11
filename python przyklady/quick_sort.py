def quick_sort(lista, lewy, prawy):
    if lewy < prawy:


        # pi - pivot indeks
        pi = (lewy + prawy) // 2 # pivot najlepiej byloby wybirac losowa, ja zawsze bede bral element na srodku
        # umieszczamy pivot na koncu tablicy
        lista[pi], lista[prawy] = lista[prawy], lista[pi]
        pi = prawy

        # wprowadzamy zmienne pomocnicze
        l, p = lewy, prawy - 1

        while l <= p:
            # idz l dopki jest mniejszy niz pivot
            while lista[l] < lista[pi]:
                l += 1
            # idz p dopoki jest wiekszy badz rowny l i p jest wiekszy bardz rowny pivotovi
            # innaczej: idz dopoki nie mniesz lewego lub p nie bedzie mniejszy niz pivot (prawo demorgana)
            while l <= p and lista[p] >= lista[pi]:
                p -= 1
            if l <= p: # nie minely sie
                lista[l], lista[p] = lista[p], lista[l]
            else: # minely sie
                lista[l],lista[pi] = lista[pi], lista[l]
                pi = l

        quick_sort(lista, lewy, pi - 1)
        quick_sort(lista, pi + 1 , prawy)

def posortuj(lista):
    quick_sort(lista,0,len(lista) - 1)

lista = [3,5,7,2,1]
posortuj(lista)

print(lista)
