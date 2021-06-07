#Marcin Polkowski
#Zadania lab_pandas
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
print('Urodziło się %d chłopców i %d dziewcząt' % (M, K))

#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
M = df[(df.Plec == 'M')]
K = df[(df.Plec == 'K')]

M_rok = M.groupby('Rok') # w tym konkretnie przypadku nie ma sansu grupowac, poniewaz w importowanym plik jest to juz pogrupowane wedglug rocznika, ale w inne sytuacji warto z tej funkjci skorzystac
K_rok = K.groupby('Rok')
print(M)
print(M_rok)

#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
female = df[(df.Plec == 'K')].groupby('Imie').Liczba.sum().sort_values()[-1:]
male = df[(df.Plec == 'M')].groupby('Imie').Liczba.sum().sort_values()[-1:]
print(female)
print(male)

# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
data = pd.read_csv('pandas_zamowienia.csv', header=0, sep=";", decimal='.')

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print(data.Sprzedawca.unique())
print('\n')

# 5 najwyższych wartości zamówień
print(data.sort_values(by='Utarg', ascending=False).head(5))
print('\n')

# ilość zamówień złożonych przez każdego sprzedawcę
il_zamowien = data.groupby('Sprzedawca').size()
print(il_zamowien)
print('\n')

# sumę zamówień dla każdego kraju
suma_zamowien = data.groupby('Kraj').Utarg.sum()
print(suma_zamowien)
print('\n')

# sumę zamówień dla roku 2005, dla sprzedawców z Polski
suma_zamowien_2005 = data[((data['Kraj'] == 'Polska') & (data['Data zamowienia'] >= '2005-01-01') & (data['Data zamowienia'] <= '2005-12-31'))].Utarg.sum()
print(suma_zamowien_2005)
print('\n')

# średnią kwotę zamówienia w 2004 roku,
srednia_zamowien_2004 = data[(data['Data zamowienia'].str[:4] == '2004')].Utarg.mean()
print(srednia_zamowien_2004)
print('\n')

# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
zamówienia_2004 = data[((data['Data zamowienia'].str[:4] == '2004'))]
zamówienia_2005 = data[((data[ 'Data zamowienia'].str[:4] == '2005'))]
zamówienia_2004.to_csv('zamówienia_2004.csv', index=False)
zamówienia_2005.to_csv('zamówienia_2005.csv', index=False)
