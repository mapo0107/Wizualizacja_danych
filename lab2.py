#Marcin Polkowski
#Zadania lab2

#Zad1 - pobieranie danych z klawiatury i liczenie znakow - input i count
datainput = input(u"Wprowadź dowolny tekst: ")
datacount = datainput.count("a") + datainput.count("A")
print(u"Litera 'a' wsytąpiła:", datacount, "razy")

#Zad2 - pobieranie liczb + zadanie matematyczne - przy uzyciu readline i write
import sys as system
system.stdout.write(u"Podaj pierwszą liczbę całkowitą: ")
rl1 = system.stdin.readline()
system.stdout.write(u"Podaj drugą liczbę całkowitą: ")
rl2 = system.stdin.readline()
system.stdout.write(u"Podaj trzecią liczbę całkowitą: ")
rl3 = system.stdin.readline()
result = (int(rl1) ** int(rl2) + int(rl3))
print(u"Wynik działania matematycznego zwraca: ", result)

#Zad3 - pobieranie liczb, zwrot najwyzszej - petle zagniezdzone
in_a = input(u"Podaj liczbę całkowitą 'A': ")
in_b = input(u"Podaj liczbę całkowitą 'B': ")
in_c = input(u"Podaj liczbę całkowitą 'C': ")
#konieczne rzutowanie pobranych danych na int. domyslnie pobiera dane jako string
in_a = int(in_a)
in_b = int(in_b)
in_c = int(in_c)
if (in_a > in_b) & (in_a > in_c):
    print("Liczba 'A' = %d jest największa" %in_a)
elif (in_b > in_a) & (in_b > in_c):
    print(u"Liczba 'B' = %d jest największa" %in_b)
elif (in_c > in_a) & (in_c > in_b):
    print(u"Liczba 'C' = %d jest największa" % in_c)
elif (in_a == in_b) | (in_a == in_c) | (in_b == in_c):
    print(u"Nie ma jednej największej liczby")
else:
    print()

#Zad4 - zmienne int i float podnoszone do kwadratu - petla for
tab =[int(1), float(2.34), int(5), float(6.789)]
for index in range(4):
    print(tab[index] * tab[index])
print()
for index in range(4):
    print("%.2f" % (tab[index] * tab[index]))

#Zad5 - pobieranie 10 liczb, dodawanie liczb dodatnich - petla while
even_list = []
odd_list = []
for index2 in range(10):
    nr = input(u"Podaj 10 liczb całkowitych: ")
    if int(nr) % 2 == 0:
        even_list.append(nr)
    else:
        odd_list.append(nr)
print("Liczby parzyste:", even_list)
print("Liczby nieparzyste:", odd_list)