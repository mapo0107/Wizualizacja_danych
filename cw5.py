import numpy as np
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
# c = a - b
# print(c)
# print(b ** 2)
# a += b
# print(a)
# a -= b
# print(a)
##############################################
# a = np.arange(12).reshape(3,4)
# print(a)
# print(a.sum()) # suma wszystkich elementow macierzy
# print(a.sum(axis=0))    #suma kolumn
# print(a.sum(axis=1))    #suma wierszy
#
# print(a.min(axis=1))    #minimalna wartosc z kazdego wiersza
#
# print(a.cumsum(axis=1))     #suma skumulowana

##############################################

# a = np.arange(3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a.dot(b))         #mnozenie macierzy
# print(np.dot(a, b))     #mnozenie macierzy

##############################################

# a = np.ones(3, dtype='int32')
# print(a.dtype, a)
# b = np.linspace(0, np.pi, 3)
# print(b.dtype, b)
# c = a + b
# print(c.dtype, c)
# d = np.exp(c+1j)
# print(d.dtype, d)

##############################################
#dzialania matematyczne na tablicach
# a = np.arange(3)
# print(a)
# print(np.exp(a))
# print(np.sqrt(a))
# c = np.array([2., -1., 4.])
# print(c)
# print(np.add(a, c))


##############################################
#iteracja
# a = np.arange(6).reshape(3,2)
# print(a)
# for b in a:
#     print(b)
#     print('')
#
# a = np.arange(6).reshape(3,2)
# print(a)
# for b in a.flat:        #splaszczenie macierzy do jednego wymiaru
#     print(b)
#     print('')

##############################################
a = np.arange(6)
print(a)
print(a.shape)          #wyswietlenie rozmiaru tablicy
print('')
b = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(b)
print('')
c = a.reshape((2,3))        #przeksztalcenie macierzy
print(c)
print(c.shape)
print('')
d = c.reshape((3,2))
print(d)
print(d.shape)
print('')
e = d.ravel()       #splaszczenie macierzy podobnie jak d.flat
print(e)
e = c.T     #transpozycja macierzy
print(e)