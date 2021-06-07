#Marcin Polkowski
#Zadania lab4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *

#Zad1 Tablica 15 wielokrotnosci liczby 3 - arange
print('Zad1')
table = np.arange(3, 46, 3)
print(table)

#Zad2 Tablica float, zapisanan w jej kopi jako int64 - astype
print('Zad2')
table2 = np.arange(1.0, 5, 0.3)
print(table2, table2.dtype)
table3 = table2.astype('int64')
print(table3, table3.dtype)

#Zad3 Funkcja dla n calkowitej zwraca tablice n*n zaczynajac od 1
print('Zad3')
n = input(u'Podaj liczbę całkowitą: ')
n = int(n)
table4 = np.arange(1, n*n+1, 1)
table4 = table4.reshape((n,n))
print(table4)

#Zad4 Funkcja potegowania liczby dla n i m - linspace
print('Zad4')
n = int(2)
m = int(4)          #??????????????????????????????????????????????????
n2 = int(n**m)
m2 = int(m*(n**2))
table5 = np.logspace(n, n**m, num=m+1)
print(table5)

#Zad5 Wektor, odwrocenie go i wrzutka na macierz
print('Zad5')
m = input(u'Podaj długość wektora: ')
m = int(m)
array = np.arange(1, m+1)
array = array[::-1]
matrix = np.diag([a for a in (array)],)
print(matrix)

#Zad6 Wykreslanka macierzowa
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.
print('Zad6')
horizontal = np.array(list('NICRAM'))   #tutaj slowo jest wspak, czyli NICRAM
vertical = np.array(list('MARCIN'))
diagonal = np.array(list('MARCIN'))

macierz = np.diag(diagonal)
macierz[:, 0] = vertical
macierz[0,:] = np.flip(horizontal)      #a tutaj przy urzyciu np.flip odwracamy NICRAM i daje nam MARCIN

print(macierz)

# Zad7.
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
print('Zad7')
def macierz(n):
    macierz = np.diag(np.ones(n), k=0).astype(np.int)       #rzutwanie na int, zeby wartosci w macierzy byly bez kropek
    np.fill_diagonal(macierz, 2)

    for x in range(1, n):
        np.fill_diagonal(macierz[x:, :], (x + 1) * 2)
        np.fill_diagonal(macierz[:, x:], (x + 1) * 2)

    return macierz

n = input('Podaj wymiar macierzy n*n: ')
n = int(n)
macierz = macierz(n)
print(macierz)



# Zadanie 8
# Napisz funkcję, która:
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)
print('Zad8')
def kierunek(tablica, kierunek):
    wiersze = tablica.shape[0]
    kolumny = tablica.shape[1]

    if kierunek == 'poziom':
        # jezeli parzysta liczba wierszy to podziel tablice
        if wiersze % 2 == 0:
            print(u"Tablica dzieli się poziomo:")
            temp1 = tablica[0:int(wiersze / 2)]
            temp2 = tablica[int(wiersze / 2):, :]

        # jezeli nie pozostaw tablice bez zmian i zwroc komunikat
        else:
            print(u"Tablica NIE dzieli się poziomo!")
            return

    elif kierunek == 'pion':
        # jezeli parzysta liczba kolumn to podziel tablice
        if kolumny % 2 == 0:
            print(u"Tablica dzieli się pionowo:")
            temp1 = tablica[:, 0:int(kolumny / 2)]
            temp2 = tablica[:, int(kolumny / 2):]

        # jezeli nie pozostaw tablice bez zmian i zwroc komunikat
        else:
            print(u"Tablica NIE dzieli się pionowo!")
            return

    else:
        print("Nieznany argument, ustaw 'piono' lub 'poziom' ")
        return

    # wydruk podzielonych tablic
    print(temp1)
    print(temp2)
#tablice testowe
tab1 = np.arange(25).reshape((5,5))
tab2 = np.arange(12).reshape((2,6))
tab3 = np.arange(15).reshape((5,3))
tab4 = np.arange(10).reshape((2,5))

#sprawdzanie czy tablice sa podzielne w pionie i poziomie
print('Tab1')
kierunek(tab1, 'pion')
kierunek(tab1, 'poziom')
print('\nTab2')
kierunek(tab2, 'pion')
kierunek(tab2, 'poziom')
print('\nTab3')
kierunek(tab3, 'pion')
kierunek(tab3, 'poziom')
print('\nTab4')
kierunek(tab4, 'zly_argument')

# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
print('Zad9')
def ciag(n):
    ciag = np.ones(n*n).astype(int)

    for x in range(2, n*n):
      ciag[x] = ciag[x-2] + ciag[x-1]

    ciag = ciag.reshape(n, n)
    print(ciag)

n = input('Podaj wymiar macierzy n*n: ')
n = int(n)
ciag = ciag(n)
