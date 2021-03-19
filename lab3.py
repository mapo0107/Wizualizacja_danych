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

#Zad5 - liczneie pola trapezu


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


#Zad10 - liczby podzielne przez 4, zapisane do pliku
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
file = open('lab3.txt', 'r')
list = file.readlines()
for number in list:
    print(number)
file.close()