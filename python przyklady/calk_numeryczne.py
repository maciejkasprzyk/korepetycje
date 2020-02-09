def f(x):
    return x**2

p = 1
q = 4

N = 100000
podstawa = (q-p)/N
lewy_bok = p
pole = 0
for _ in range(N):
    pole += (f(lewy_bok) + f(lewy_bok+podstawa)) * podstawa / 2
    lewy_bok += podstawa

print(pole)


def F(x):
    return x**3/3

print(F(q)-F(p))
