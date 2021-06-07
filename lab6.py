# Marcin Polkowski
# Zadania lab6
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd

# Zadania do wykresów z Pandas
# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

imiona = pd.ExcelFile('pandas_imiona.xlsx')
data = pd.read_excel(imiona, header=0)
data = data.groupby(['Rok']).agg({'Liczba':'sum'})
liniowy = data.plot()
plt.ylabel('Liczba dzieci')
plt.title(u"Liczba urodzonych dzieci wg. rocznika")
plt.show()

# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

imiona = pd.ExcelFile('pandas_imiona.xlsx')
data = pd.read_excel(imiona, header=0)
data = data.groupby(['Plec']).agg({'Liczba':'sum'})
slupkowy = data.plot.bar()
plt.legend(loc="center")
plt.ylabel("Liczba narodzin")
plt.title("Porównanie narodzin chłopców i dziewczynek")
plt.show()


# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

imiona = pd.ExcelFile('pandas_imiona.xlsx')
data = pd.read_excel(imiona, header=0)
data = data[data['Rok'] > 2013].groupby(['Plec']).agg({'Liczba':'sum'})
kolowy = data.plot.pie(subplots=True, autopct='%.0f %%', fontsize=15)
plt.ylabel(' ')
plt.title("Wartości % narodzin chłopców i dziewcząt > 2013 roku")
plt.show()

# Zadania do matplotlib
# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

x = np.arange(1, 21, 1)
y = (1/x)
plt.plot(x, y, label='y = 1/x')
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.legend()
plt.title('Wykres f(x) = 1/x dla x w przedziale [1,20]')
plt.show()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

x = np.arange(1, 21, 1)
y = (1/x)
plt.plot(x, y,'g>:', label='y = 1/x') #wystarczylo dodac 'g>:'
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.legend()
plt.title('Wykres f(x) = 1/x dla x w przedziale [1,20]')
plt.show()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

x = np.arange(0, 31, .1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x) cos(x)')
plt.legend(loc='center')
plt.show()

# Zadanie 4
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy,
# gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, dodaj paletę kolorów c na przykładzie listingu 6
# a parametr s niech będzie wartością absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y.

data = pd.read_csv('iris.data', header=0, sep=",", decimal=".", usecols=['sepal length', 'sepal width'])
data = {'a': data['sepal length'],
        'b': data['sepal width'],
        'c': np.random.randint(1, 10, len(data.index))}
data['d'] = np.abs(data['a'] - data['b']) * 10
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.show()

# Zadanie 5
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji dotyczącej wprowadzenia do pandas.

imiona = pd.ExcelFile('pandas_imiona.xlsx')
data = pd.read_excel(imiona, header=0)

# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.

plt.subplot(1, 3, 1)
slupkowy = data.groupby('Plec').Liczba.sum()
slupkowy.plot.bar()
plt.title(u'Liczna narodzin w całym okresie', fontsize=10)
plt.xlabel('Płeć', fontsize=10)
plt.ylabel(u'Ilość narodzin', fontsize=10)

# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna.
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.

plt.subplot(1, 3, 2)
female = data[data.Plec == 'K'].groupby('Rok').sum()
male = data[data.Plec == 'M'].groupby('Rok').sum()
plt.plot(male, label=u'Mężczyźni')
plt.plot(female, label='Kobiety')
plt.title(u'Liczba narodzin wg płci', fontsize=10)
plt.xlabel('Rok', fontsize=10)
plt.ylabel(u'Ilość narodzin', fontsize=10)

# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

plt.subplot(1, 3, 3)
slupkowy2 = data.groupby('Rok').Liczba.sum()
slupkowy2.plot.bar()
plt.title(u'Ilość narodzin wg roku', fontsize=10)
plt.xlabel('Rok', fontsize=10)
plt.ylabel(u'Ilość narodzin', fontsize=10)

plt.show()

# Zadanie 6
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień.
# Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu. Przetestuj ten atrybut na wykresie.

data = pd.read_csv('pandas_zamowienia.csv', header=0, sep=";", decimal='.', parse_dates=['Data zamowienia'])
seller = data.groupby('Sprzedawca').Utarg.sum()         #liczymy sume zamowuen grupowane wg sprzedawcy
kolowy = seller.plot.pie(subplots=True, autopct='%.2f%%', fontsize=14, figsize=(6, 6), startangle=90, shadow=True, explode=(seller == max(seller)) * 0.2 )  #explode i shadow
plt.title(u'Procentowy udział w sprzedarzy', fontsize=20)
plt.show()