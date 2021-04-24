import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#prosty wykres liniowy
plt.plot([1, 2, 3, 4])
plt.ylabel("liczby")
plt.show()

#przekazemy dwa wektory, pierwszy dla osi x, drugi dla osi y
#przekazany zostanie dodatkowy parametr typu string, okreslajacy styl wykresu
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')  #ro- kolor czerwony, punktorem kropka, linia ciagla
#mozemy okreslic liste parametrow (xmin, xmax, ymin, ymax) dzieki funkcji axis
plt.axis([0, 6, 0, 20])
plt.show()

#ustawiamy rozne kolory dla poszczegolnych elementow nakladajacycg na siebie dwa wykresy
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
plt.axis([0, 6, 0, 20])
plt.show()

#wektor bazowy za pomoca funkcji arange
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label='kwadratowa')
plt.plot(x, x**3, label='szescienna')

#etykiety osi
plt.xlabel("etykieta x")
plt.ylabel("etykieta y")

#tytul wykresu
plt.title("Prosty wykres")

#pokazanie legendy
plt.legend()
plt.show()

##########################################

x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend()
plt.show()

##########################################
#Dane w spostaci slownika (moze byc rowniez Pandas DataFrame)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] +10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# 'a' jest rownowazny data['a']. Parametr c bedzie odpowiedzialny za kolor
#i przekazywany w postaci wektora wartosci koloru dla kazdej kolejnosci wartosci wektora
#parametr s to scale - okresla rozmiar, w tym przypadku punktu, dal kazdej kolejnej
#wartosci wektora wykresu
print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('wartosci A')
plt.ylabel('wartosci B')
plt.show()
##########################################

#subplot(nrows, ncols, index)

x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2* np.pi * x1)
y2 = np.cos(2* np.pi * x2)

#grid 2x1 (czyli 2 wiersze, 1 kolumna)
plt.subplot(2, 1, 1)
plt.plot(x1, y1, "-")
plt.title("Dwa wykresy")
plt.ylabel("sin(x)")
#definiujemy wykres o indeksie 2
plt.subplot(2, 1, 2)
plt.plot(x2, y2, "r-")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.show()

#grid 3x2 (3 wiersze, 2 kolumny), definiujemy wykres o indeksie 1
plt.subplot(3, 2, 1)
plt.plot(x1, y1, "-")
plt.ylabel("sin(x)")

#wykres o indeksie 4
plt.subplot(324)    #3 wiesze, 2 kolumny, 4 indeks
plt.plot(x2, y2, "r-")
plt.ylabel("cos(x)")

#wykres o indeksie 5
plt.subplot(325)    #3 wiesze, 2 kolumny, 5 indeks
plt.plot(x2, y2, "g-")
plt.ylabel("cos(x)")
plt.show()

#wykres slupokowy       COS TU NIE DZIALA ZE SLUPKAMI
etykieta = ['kobiety', 'Mezczyzni']
wartosci = [345, 435]

rozmiar_wykresu = plt.figure(figsize=(8,10)) # definiowanie obiektu z wielkoscia wykresu, obiekt przekazuje
plt,bar(etykieta, wartosci, figure=rozmiar_wykresu)

plt.xticks(rotation=45)
plt.xlabel("Płęć")
plt.ylabel("Ilość narodzin")
plt.show()

################################################################
#HISTOGRAM
x = np.random.randn(10000)

plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Wartosci')
plt.ylabel('Prawdopodobienstwo')
plt.title('Histogram')
#wyswietlenie siatki
plt.grid()
plt.show()

################################################################
zawodnicy = ["AAAAAA", "BBBBBB", "CCCCCCCC", "DDDDDD"]
bramki = [22, 33, 44, 55]

#pierwsza wersja wykresu
wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy, autopct=lambda pct:
                                                                     "{:.1f}%".format(pct), textprops=dict(color='black'))
plt.setp(autotexts, size=14, weight="bold")
plt.title("Pierwsza wersja")
plt.legend(title="Zawodnicy")
plt.show()
################################################################

#wykres liniowy serii danych
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()

#wykres z ramki danych
data = {'Kraj': ['aaaaa', 'bbbbb', 'ccccc', 'dddddd', 'eeeeeee'],
        'Stolica' : ['FFFFFF', 'GGGGGGG', 'HHHHHHHH', 'IIIIIIII', 'JJJJJJJJJ'],
        'Kontynent' : ['Euroa', 'Azja', 'Afryka', 'Europa', 'Europa'],
        'Populacja' : [123456786, 5244546, 54365, 245678, 987653]}

df = pd.DataFrame(data)
grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel("MLD")
wykres.set_xlabel("Kontynent")
wykres.legend()
plt.xticks(rotation=0)
plt.title("Populacja z podzialem na kontynenty")
plt.savefig('wykres.png')
plt.show()

#wykres