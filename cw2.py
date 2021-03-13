# break
#
#
# if warunek:
#     if warunek2:
#         instrukcje      # wykonuje instrukcje po spelnieniu obydwu warunkow
#
#     instrukcje          #wykonuje instruckje po spelnieniu tylko pierwszego warunku

# lista = [1,2,3,4,5,6,4]
# print("Podaj liczbe. Powornam czy roznica jej z liczba z listy = 0")
# liczba = input("wpisz liczbe: ")
# licznik = 0
#
# while licznik < len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print(liczba, "-", str(lista[licznik]),  "= 0")
#         break
#     else:
#         print(lista[licznik])
#         licznik += 1




# try:
#     instrukcja badz blok instrukcji
# except nazwa błedu:
#
# l1 = input("Podaj 1 liczbe: ")
# l2 = input("Podaj 2 liczbe: ")
# l1 = int(l1)
# l2 = int(l2)
#
# try:
#     wynik = l1 / l2
#     print(wynik)
# except ZeroDivisionError:
#     print("Nie dzieli sie przez zero!")



#mozliwa skladnia
# lista = []
# for element in zakres:
#     if warunek_na_element:
#         lista.append("cos sie dzieje z elementem", element)
#
# lista2 = ["cos sie dzieje z elementem" element for element in zakres if warunke_na_element]

# lista = []
# for x in range(10):
#     if x <10:
#         lista.append(x**2)
# print(lista)
# lista2 = [x**2 for x in range(10)]
# print(lista2)
#
# lista3 = []
# for y in range(6):
#     lista3.append(3**y)
# print(lista3)
# lista4 = [3**y for y in range(6)]
# print(lista4)
#
#

########################################################

#cos tu nie dziala do dokladniejszego sprawdzenia pozniej
# lista = [0,1,2,3,4,5,6,7,8,9,0]
# lista_parzyste = []
#
# for a in lista:
#      if a % 2 == 0:
#      lista_parzyste.append(a)
# print(lista_parzyste)
#
#
# parzyste = [b for b in lista if b % 2 == 0]
# print(parzyste)


###############

# skroty = {"PZU": "Panstowy zaklad ubezpieczen,",
#           "ZUS": "Zaklad ubezpieczen spolecznych",
#           "PKO": "Polska kasa osczednosciowa"}
#
# slownik_odwrocone = {}
# print(skroty)
# for key, value in skroty.items():
#     slownik_odwrocone[value] = key
# print(slownik_odwrocone)
#
# odwrocone = {value: key for key, value in skroty.items()}
# print(odwrocone)

###########################

#FUNKCJE

#def nazwa_funkcji(arg_pozycyjne, arg_domyslny = wartosc_domyslna, *arg, **arg):
#   instrukcje
#   return wartosc

# from math import *
# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("brak pierwiastow")
#         return 0
#     if delta == 0:
#         print("jeden pierwiastek")
#         x = (-b)/(2 * a)
#         return x
#     else:
#         print("dwa pierwiastki")
#         x1 = (-b - sqrt(delta))/(2 * a)
#         x2 = (-b + sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(rownanie_kwadratowe(6,1,3,))
# print(rownanie_kwadratowe(1,2,1,))
# print(rownanie_kwadratowe(1,4,1,))




# from math import *
# def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
# #wywolanie dla arg domyslnych
# print(dlugosc_odcinka())
#
# #wywolanie dla wlasnych wartosiowac
# print(dlugosc_odcinka(1,2,3,4))
#
# #wywolanie dla wartosci mieszanych w kolejnosci i poza kolejnoscia
# print(dlugosc_odcinka(2,2, y2=2, x2=1))
#
# #wartosci w innej kolejnosci
# print(dlugosc_odcinka(x2=5, y2=6, x1=2, y1=2))
#
# #wartosci dla dwoch argumentow domyslnych i dla dwod podanych przez nas
# print(dlugosc_odcinka(y2=5, x2=5))



##########
#from math import *
# def ciag (*liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for a in liczby:
#             suma += a
#             return suma
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8,9))

#Cos tu nie dzila, do pozniejszego sprawdzenia
# def to_lubie(**rzeczy):
#     for cos in rzeczy:
#     print("to jest")
#     print(cos)
#     print("co lubie")
#     print(rzeczy[cos])
#
# print(to_lubie(slodycze = "czekolada", rozrywka = ["gry", "filmy"]))
#

##########

plik = open(nazwa, tryb, bufor, system kodowania)