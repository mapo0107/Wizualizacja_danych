#cwiczenia 2021.03.14
#paczka numpy

import numpy as np

#sposoby na tworzenie tablic
# a = np.arange(2)
# print(a)
# print(type(a))
# print(a.dtype)
#
# a = np.array([0, 1, 2])
# print(a)
# print(type(a))
# print(a.dtype)
#
# a = np.arange(1, 10, 1)     #el poczatkowy, el koncowy, krok
# print(a)
# print(type(a))
# print(a.dtype)
#
# a = np.arange(2, dtype='int64')     #rzutowanie na typ int64
# print(a)
# print(type(a))
# print(a.dtype)
#
# b = a.astype('float')       #rzutowanie na float
# print(b)
# print(type(b))
# print(b.dtype)
#
# print(b.shape)          #zwraca ilosc el dla wymiarow tablicy
# print(a.ndim)           #zwraca ilosc wymiarow tablicy

#################

# m = np.array([np.arange(2), np.arange(2)])
# print(m)
# print(type(m))

# zero = np.zeros((5,5))
# jedynka = np.ones((4,4))
# print(zero)
# print(jedynka)
#
# print(zero.dtype)
# print(jedynka.dtype)

# pusta = np.empty((2,2))
# print(pusta)
# print(pusta.dtype)
#
# poz_1 = pusta[1,1]
# poz_2 = pusta[0,1]
# print(poz_1)
# print(poz_2)
#
# macierz = np.array([[1,2], [3, 4], [5,6]])
# print(macierz)
#
# liczby = np.arange(1, 2, 0.1)       #skok o 0.1
# print(liczby)
# print(len(liczby))
#
# liczby = np.linspace(1, 2, 5)       #ostanti paramert okresla ile liczb ma sie zmiescic w przedziale
# print(liczby)
#
# liczby = np.linspace(1, 2, 5, endpoint=False)
# print(liczby)
#
# z = np.indices((5,3))
# print(z)
#
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
#
# mat_diag1 = np.diag([a for a in range(5)], -1)
# print(mat_diag1)
#
# m = np.fromiter(range(5), dtype='int32')
# print(m)

# marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S1')
# print(mar)
# mar = np.frombuffer(marcin, dtype='S2')
# print(mar)
#
# marcin = 'Marcin'
# mar_3 = np.array(list(marcin))
# print(mar_3)
# mar_4 = np.array(list(marcin), dtype='S1')
# print(mar_4)
# mar_5 = np.array(list(b'Marcin'))           #wyswietlone beda kody ASCI napisu
# print(mar_5)
# mar_6 = np.fromiter(marcin, dtype='S1')
# print(mar_6)
# mar_7 = np.fromiter(marcin, dtype='U1')
# print(mar_7)
#
# mat = np.ones((2,2))
# mat1 = np.ones((2,2))
# wynik = mat + mat1
# print(wynik)
# wynik = mat - mat1
# print(wynik)
# wynik = mat * mat1
# print(wynik)
# wynik = mat / mat1
# print(wynik)

##########################
# cięcie tablicy

a = np.arange(10)
print(a)
s = slice(2, 7, 1)  #start, stop, step
print(a[s])         #wyswietlanie elementow wycietych
s = range(2, 7, 1)
print(a[s])
print(a[2:7:1])
print(a[2:])
print(a[2:5])

#sposoby cięcia macierzy
mat = np.arange(25)
print(mat)
mat = mat.reshape((5,5))    #definiujemy rozmiar n x m macierzy
print(mat)
print(mat[1:])
print(mat[:, 1])
print(mat[:, 1:2])
print(mat[2:6, 1:3])
print(mat[:, range(2,6,2)])