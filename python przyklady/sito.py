
def main():
    sito = [True for _ in range(10**6)]

    pierwsze = []
    for i in range (2,10**6):
        if sito[i]:
            pierwsze.append(i)
            for j in range(i,10**6,i):
                sito[j] = False

    print(pierwsze)
    print(len(pierwsze))
main()
