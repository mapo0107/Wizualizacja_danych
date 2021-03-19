#Marcin Polkowski
#Zadania lab4
import numpy as np
from math import *

# #Zad1 Tablica 15 wielokrotnosci liczby 3 - arange
# print('Zad1')
# table = np.arange(3, 46, 3)
# print(table)
#
# #Zad2 Tablica float, zapisanan w jej kopi jako int64 - astype
# print('Zad2')
# table2 = np.arange(1.0, 5, 0.3)
# print(table2, table2.dtype)
# table3 = table2.astype('int64')
# print(table3, table3.dtype)
#
# #Zad3 Funkcja dla n calkowitej zwraca tablice n*n zaczynajac od 1
# print('Zad3')
# n = input(u'Podaj liczbę całkowitą: ')
# n = int(n)
# table4 = np.arange(1, n*n+1, 1)
# table4 = table4.reshape((n,n))
# print(table4)

#Zad4 Funkcja potegowania liczby dla n i m - linspace
# print('Zad4')
# n = int(2)
# m = int(4)          ??????????????????????????????????????????????????
# n2 = int(n**m)
# m2 = int(m*(n**2))
# table5 = np.logspace(n, n**m, num=m+1)
# print(table5)

#Zad5 Wektor, odwrocenie go i wrzutka na macierz
# m = input(u'Podaj długość wektora: ')
# m = int(m)
# array = np.arange(1, m+1)
# array = array[::-1]
# matrix = np.diag([a for a in (array)],)
# print(matrix)

#Zad6 Wykreslanka macierzowa
horizontal = 'Marcin'
vertical = 'Martinez'
diagonal = 'Martinski'
h_lenght = len(horizontal)
v_lenght = len(vertical)

#h_matrix = np.array(list(horizontal))
h_matrix = h_matrix.reshape((v_lenght, h_lenght))
#v_matrix = np.array(list(vertical))
v_matrix = v_matrix.reshape((v_lenght,h_lenght))
print(h_matrix)
print(v_matrix)

matrix = h_matrix + v_matrix
print(matrix)