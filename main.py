# import sys as system
# print(system.version)
#
# napis = "Ala \nma \nkota"
# print(napis)

# liczba = 4
# liczba2 = 4.5
# zespolona = 3 + 2j
# print(liczba)
# print(liczba2)
# print(zespolona)
# print(type(liczba))

# a, b, c = 2, 3.4, "s"
# print(a, b, c)

#nazwa zmiennej nie moze sie zaczynac od liczby, ale moze ja uwzgledniac
#zmienna wielkorywazowa oddzielana jest podkreslnikiem np. liczba_zespolona

# napis = "test"
# napis2 = "qwerty"
# print(napis, napis2)        #oddziela zmienne spacja
# print(napis + napis2)       #laczy zmienne w lancuch

# a = 20
# b = 3
# c = 6
#
# dzielenie = a / c
# dodawanie = a + b
# dzielenie_calkowite = b // c
# reszta = b % c
# potegowanie = a ** c
#
# print(dzielenie)
# print(dodawanie)
# print(dzielenie_calkowite)
# print(reszta)
# print(potegowanie)
#
# print(pow(6,3))     #6 do potegi 3

#a += 1 jest rownowazne a = a + 1


# from math import *
# a = 20
# b = 3
# c = 6
#
# dzielenie = a / c
# dodawanie = a + b
# dzielenie_calkowite = b // c
# reszta = b % c
# potegowanie = a ** c
#
# print(dzielenie)
# print(dodawanie)
# print(dzielenie_calkowite)
# print(reszta)
# print(potegowanie)
#
# print(pow(6,3))
#
# d = 0.555
# print(round(d))     #funkcja zaokraglajaca
# print(round(d,2))   #funkcja zaokraglajaca do dwoch miejsc po przecinku
# print(pi)           #stala wartosc pi
# print(sqrt(9))      #pierwiastkowanie


# print(u"światłowód")       #formatownie polskich znakow poprzez dodanie u
#
# print("wynik dzialania a = %(zm)d" % {'zm':12})         #int
# print("wynik dzialania a = %(zm)f" % {'zm':1.23})       #float
# print("wynik dzialania a = %(zm).2f" % {'zm':1.23})     #float do dwoch miejsc po przecinku

# specjalizacja = "isi"
# grupa = 2
# print("nasza specjalizacja to %s, grupa numer %d" %(specjalizacja, grupa))
#
#
# a = 3
# b = 7
# z = 3 - 7
# print("wynik dzialania %(z1)d - %(z2)d = %(z3)d" % {'z1' : a, 'z2' : b, 'z3' : z})


#KONTENERY DANYCH
# lista = [3, 4, 5, 3.14, 's',
#          6, 7]
# print(lista)
#
# lista.append(6)         #dodanie elementu do lancucha na jego koncu
# lista.append('s3')
# print(lista)
#
# lista.insert(4, 'ABC')     #wstawiamy w indeksie 4 wartosc ABC
# print(lista)
#
# lista.extend(('X', 'Y', 'Z'))
# print(lista)
#
# lista.pop(1)            #usuwanie wartosci przypisanej indeksowi 1
# print(lista)
#
# lista.pop()            #usuwanie wartosci przypisanej indeksowi koncowemu
# print(lista)
#
# lista.remove(6)         #usuwanie elementu o danej wartosci. jesli jest wiecej to usuwa pierwszy
# print(lista)
#
# del lista[5]            #usuwa wartosc z indeksu 5
# print(lista)
#
# lista.reverse()
# print(lista)
#
# lista2 = [6, 1, 3, 9, 5, 4]
# print(lista2)
# lista2.sort()
# print(lista2)


# slownik = {3:'s', 4: 5, 'a': 3.1}       #klucze 3, 4, 5 przyjmuja wartosci po :
# print(slownik)
# print(slownik[3])
#
# slownik2 = {3:'s', 4: 5, 'a': 3.1, 3: 222}       #klucze 3, 4, 5, 3 przyjmuja wartosci po :
# print(slownik2)
# print(slownik2[3])                      #klucz nie jest unikalny i zrwacany jest ostatni, czyli w tu wartosc 222
#
# slownik['klucz'] = 'wartosc'
# slownik[6] = 12
# print(slownik)
#
# slownik.pop(6)
# print(slownik)
#
# del slownik[3]
# print(slownik)
#
# print(slownik.keys())           #sprawdza klucze w slowniku
# print(slownik.values())         #sprawdza wartosci kluczy

#del slownik             #usuwa caly slownik



#WCZYTYWANIE DANYCH INSTRUKCJI WARUNKOWYCH I INSTRUKCJI ITERACYJNYCH
#WCZYTYWANIE DANYCH Z KONSOLI

# napis = input("Wprowadz tekst: ")
# print(napis)
# print(type(napis))
# napis = int(napis)          #rzutowanie na tym int
# print(type(napis))


# import sys as system
#
# system.stdout.write("Wpisz liczbe: ")
# liczba = system.stdout.readline()
# system.stdout.write(liczba)
# print(type(liczba))




#INSTRUCKAJ WARUNKKOWA
#
# if warunek:
#     instrukcje1
#     instrukcje2
# elif warunek2:
#     instrukcja3
# else:
#     instrukcja4

# a == b          #operator rownosci
# a != b          #operator roznosci
# >
# <
# >=
# <=
#&
# |



# a = input ("Podaj a: ")
# b = input ("Podaj b: ")
#
# a = int(a)
# b = int(b)
#
# if a > b:
#     print("Liczba " + str(a) + " jest wieksza")
# elif a < b:
#     print("Liczba " + str(b) + " jest wieksza")
# else:
#     print("Liczby sa rowne")



# a = input ("Podaj a: ")
# b = input ("Podaj b: ")
#
# a = int(a)
# b = int(b)
#
# if a == b:
#     print("Liczby sa rowne")
# else:
#     print("Liczby sa rozne")



# a = input ("Podaj a: ")
# b = input ("Podaj b: ")
# c = input ("Podaj c: ")
# d = input ("Podaj d: ")
#
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
#
# if (a > b) & (c > d):
#     print("Liczba a jest wieksza od b i liczna c jest wieksza od d")
# else:
#     print("Liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od d")


#PETLE
#
# for licznik in sekwencja:
#     instrukcja1
#     instrukcja2
# else:
#     instrukcja3


# for x in range(1,6,1):
#     print(x)
#
# while warunek:
#     instrukcje
# else:
#     instrukcje



# z = 0
# while z != 10:
#     print(z)
#     z += 1
# else:
#     print("zostalo wyswietlonych " + str(z) + " liczb")
#     print("zostalo wyswietlonych", z, "liczb")




# break
#
#
# if warunek:
#     if warunek2:
#         instrukcje      # wykonuje instrukcje po spelnieniu obydwu warunkow
#
#     instrukcje          #wykonuje instruckje po spelnieniu tylko pierwszego warunku