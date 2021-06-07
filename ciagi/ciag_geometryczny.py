def generuj_ciag(a1, q, ile):
    for x in range(1, ile+1):
        print("a{} = {}" .format(x, n_wyraz(x, a1, q)))

def n_wyraz(n, a1, q):
    return a1 * q**(n-1)

def suma(n, a1, q):
    if q == 1:
        return a1 * n
    else:
        return a1 * (1 - q ** n) / (1 - q)

#żródło https://www.matemaks.pl/ciag-geometryczny.html