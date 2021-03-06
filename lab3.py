#Marcin Polkowski
#Zadania lab3 - Python comprehension i funkcje

#Zad1 - zbiory
A = [1 - x for x in range(1, 11)]
B = [4 ** x for x in range(8)]
C = [x for x in B if x % 2 == 0]
print('Zad1')
print(u'Zbiór A: ', A, u'Zbiór B: ', B, u'Zbiór C: ', C)

#Zad2 - losowanie elementow -> lista1 -> lista2 tylko parzystych
from random import *

list1 = []
for element in range (10):
    random_nr = randrange(0,999)
    (list1.append(random_nr))
even_list = [x for x in list1 if x % 2 == 0]
print('Zad2')
print(even_list)

#Zad3 - slownik produktow spozywczych
product_list = {'czekolada' : 'szt', 'cukierki' : 'kg', 'pączek' : 'szt', 'mleko' : 'litr', 'chleb' : 'szt'}
product_list1 = [keys for keys, values in product_list.items()]
product_list2 = [keys for keys, values in product_list.items() if values == 'szt']
print('Zad3')
print('Wszystkie produkty:', product_list1)
print('Produkty których wartości to sztuki: ',product_list2)

#Zad4 - funkcja sprawdzajaca czy trojkat jest prostokatny
print('Zad4')
def trojkat(a, b, c):
    bok = [float(a), float(b), float(c)]
    bok.sort()
    for x in bok:
        if x < 0:
            print(u'Wprowadzono błędne dane')
            return 0
    if bok[2]**2 == bok[1]**2 + bok[0]**2:
        print(u'Trójkąt jest prostokątny')
    else:
        print(u'Trójkąt nie jest prostokątny')
    return 1

print(u"Podaj długości boków trójkąta:\n")
a = input("A: ")
b = input("B: ")
c = input("C: ")
trojkat(a, b, c)

#Notatki pomocnicze :)
# bok = [int(3), int(1), int(2)]
# print(bok)
# bok.sort()
# print(bok)
# print(bok[0])
# print(bok[1])
# print(bok[2])

#Zad5 - liczneie pola trapezu // (1/2) * (a+b) * h
print('Zad5')
def trapez(a, b, h):
    wymiar = [float(a), float(b), float(h)]
    for x in wymiar:
        if x <= 0:
            print(u'Wprowadzono błędne dane')
            return 0
    a = float(a)
    b = float(b)
    h = float(h)
    pole = (a + b) * h * 0.5
    print(pole)

print(u"Podaj wymiary trapezu:\n")
a = input("A: ")
b = input("B: ")
h = input("H: ")
trapez(a, b, h)


#Zad6 - iloczyn elementow ciagu
def ciag(list = [], a = 1, b = 4, ile = 10):
    x = 1
    for index in range(0, ile):     #alternatywnie "ile-1" w zaleznosci od interpretacji zadania
        x = x*b
        list.insert(index, x)
    list.insert(0, a)
    return list
print('Zad6')
print(ciag())

#CIAG DZIALAJACY JAKO "NIE FUNKCJA"
# list = []
# a = 1
# b = 4
# ile = 10
# x = 1
# for index in range(0, ile):
#     x = x*b
#     list.insert(index, x)
# list.insert(0, a)
# print(list)

#Zad7 - zad6 z operatorem *
def ciag(*arguments):
    if len(arguments) == 1:
        return 0
    else:
        list = []
        x = 1
        for index in range(0, arguments[3]):     #alternatywnie "ile-1" w zaleznosci od interpretacji zadania
            x = x*arguments[2]
            list.insert(index, x)
        list.insert(0, arguments[1])
        return list
print('Zad7')
print(ciag(1, 1, 4, 10))       #1 el na liscie, a, b, ile


#Zad8 - funkcja z operatorem **
def product_list(**items):
    products = len(items.keys())
    price = sum(items.values())
    return products, price
print('Zad8')
total_price = product_list(czekolada=2.5, cukierki=3, pączek=1.5, mleko=4, chleb=3.5)
print(total_price)

#DZIALAJACY JAKO "NIE FUNKCJA"
# product_list = {'czekolada': 2.5, 'cukierki': 3, 'pączek': 1.5, 'mleko': 4, 'chleb': 3.5}
# print(u'Ilość przedmiotów: ', len(product_list.keys()))
# print('Ich cena: ', sum(product_list.values()))


#Zad9 - ciagki arytmetyczne i geometryczne
#Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

from ciagi import *
print('Zad9')
#arytmetyczny
print('Wygenerowany ciąg arytmetyczny 1')
ciag_arytmetyczny.generuj_ciag(2, 22, 5)
print('Wygenerowany ciąg arytmetyczny 2')
ciag_arytmetyczny.generuj_ciag(98, 8, 15)
print(u'Suma ciągu arytmetycznego')
arytmetyczny = [11, 8, 5, 2, -1]
print(ciag_arytmetyczny.suma(len(arytmetyczny), arytmetyczny[0], arytmetyczny[1] - arytmetyczny[0]))

#geometryczny
print('Wygenerowany ciąg geometryczny 1')
ciag_geometryczny.generuj_ciag(2, 22, 5)
print('Wygenerowany ciąg geometryczny 2')
ciag_geometryczny.generuj_ciag(98, 8, 15)
print(u'Suma ciągu geometrycznego')
geometryczny = [11, 8, 5, 2, -1]
print(ciag_geometryczny.suma(len(geometryczny), geometryczny[0], geometryczny[1] / geometryczny[0]))

#Zad10 - liczby podzielne przez 4, zapisane do pliku
print('Zad10 - zapisuje dane do pliku')
from random import *

list = []
for number in range (20):
    random_nr = randrange(0,999)
    (list.append(random_nr))
list = [x for x in list if x % 4 == 0]

file = open('lab3.txt', 'w+')
file.write('Liczby podzielne przez 4:\n')
for number in list:
    file.writelines('[' + str(number) + ']')
file.close()

#Zad11 - odczyt pliku i wyswietlenie zawartosci w konsoli
print('Zad11')
file = open('lab3.txt', 'r')
list = file.readlines()
for number in list:
    print(number)
file.close()