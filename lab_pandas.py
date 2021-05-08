import pandas as pd

import xlrd
import openpyxl

#Zad1 Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

xlsx = pd.ExcelFile('pandas_imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)

#Zad2 Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
xlsx = pd.ExcelFile('pandas_imiona.xlsx')
df = pd.read_excel(xlsx)

#tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
top1000 = df[(df.Liczba > 1000)]
print(top1000)

#tylko rekordy gdzie nadane imię jest takie jak Twoje
marcin = df[(df.Imie == 'MARCIN')]
print(marcin)

#sumę wszystkich urodzonych dzieci w całym danym okresie,
babyBorn = 0
for n in df.Liczba:
    babyBorn = babyBorn + n
print('W całym danym okresie urodziło się %d dzieci' % babyBorn)

#sumę dzieci urodzonych w latach 2000-2005
babyBorn_2000_2005 = 0
years = df[(df.Rok >=2000) & (df.Rok <=2005)]

for n in years.Liczba:
    babyBorn_2000_2005 = babyBorn_2000_2005 + n
print('W latach 2000-2005 urodziło się %d dzieci' % babyBorn_2000_2005)


#sumę urodzonych chłopców i dziewczynek,
M = df[(df.Plec == 'M')].sum().Liczba
K = df[(df.Plec == 'K')].sum().Liczba
print('Urodziło się %d chłopców i %d dziwcząt' % (M, K))


#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),



#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,