def poprawne_zdanie(napis):
    ostatni_znak = napis[len(napis) - 1]
    if ostatni_znak not in ['?','.', '!']:
        return False
    # print(napis[-1:])
    return True

print(poprawne_zdanie("Zdanie"))
print(poprawne_zdanie("Zdanie."))



napis = 'Ala ma kota'

for i in range(len(napis)):
    znak = napis[i]
    print(znak)