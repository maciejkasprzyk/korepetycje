def nwd(a,b):
    reszta = a % b
    if reszta == 0:
        return b
    a = b
    b = reszta
    return nwd(a,b)

