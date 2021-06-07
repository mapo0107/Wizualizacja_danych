def generuj_ciag(a1, r, ile):
    for x in range(1, ile+1):
        print("a{} = {}" .format(x, n_wyraz(x, a1, r)))

def n_wyraz(n, a1, r):
    return a1+(n-1)*r

def suma(n, a1, r):
    return (2*a1+(n-1)*r)/2*n

#źródło https://www.matemaks.pl/ciag-arytmetyczny.html


