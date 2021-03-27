#Biblioteki numpy, pandas, xlrd, openpyxl

import pandas as pd
import numpy as np

#Ramki
serie = pd.Series([1, 3, 5, np.nan, 8, 8])        #np.nan to element nie bedacy liczba
print(serie)
seria = pd.Series([10, 12, 8, 14], index = ['A', 'B', 'C','D'])
print(seria)

#Ramka na podstawie slownika
data = {'Kraj' : ['Belgia', 'Indie', 'Brazylia'],
        'Stolica' : ['Bruksela', 'New Dehli', 'Brasilia'],
        'Populacja' : [1234567, 654213543, 34253]}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
################################################################################

daty = pd.date_range('20210327', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns= list('ABCD'))
print(df)

#ODCZYT LIKU CSV
df = pd.read_csv('dane.csv', header=0, sep=';', decimal=',')
print(df)
df.to_csv('zapis_dane.csv', index=False)     #zapis do pliku

import xlrd
import openpyxl

# #COŚ TU NIE DZIAŁA, DO PÓŹNIEJSZEGO SPRAWDZENIA
#ODCZYT PLIKU XLSX
xlsx = pd.ExcelFile("dane.xlsx")
df = pd.read_excel(xlsx, header=0)
print(df)
df.to.excel('zapis_dane.xlsx', sheet_name='Arkusz1')

#################################################################
seria = pd.Series([10, 12, 8, 14], index = ['A', 'B', 'C','D'])
data = {'Kraj' : ['Belgia', 'Indie', 'Brazylia'],
        'Stolica' : ['Bruksela', 'New Dehli', 'Brasilia'],
        'Populacja' : [1234567, 654213543, 34253]}

df = pd.DataFrame(data)
print(df)
print("")
print(seria['A'])
print(seria.A)
print("")
print(df[0:1])
print(df.iloc[[0][0]])
print("")
print(df['Populacja'])
print("")
print(df.loc[[0],["Kraj"]])
print(df.at[0,"Kraj"])
print("")
print("Kraj: " + df.Kraj)
print("")
print(df.sample())              #zwrocenie losowej wartosci
print("")
print(df.sample(2))             #zwrocenie 2 losowych wartosci
print("")
print(df.sample(frac=0.5))      #procentowe zwrocenie losowych wartosci
print("")
print(df.sample(10, replace=True))      #losowanie 10 elementow z powtorzeniami
print("")
print(df.head())                #zwraca poczatkowe elementy ramki (domyslnie 5 pierwszych)
print("")
print(df.head(2))
print("")
print(df.tail())                #zwraca ostatnie elementy ramki (domyslnie 5 ostatnich)
print("")
print(df.tail(2))
print("")
print(df.describe())
print("")
print(df.T)                     #transpozycja ramki (kolumny zamieniaja sie z wierszami
print("")

#filtrowanie, grupowanie agregowanie danych
print(seria[(seria > 9)])
print("")
print(seria.where(seria > 10))
print("")
print(seria.where(seria > 10, u'za małe wartości'))

#modyfikacja ramki
seria1 = seria.copy()
seria1.where(seria > 10, u'za małe wartości', inplace=True)
print(seria1)

print(seria[~(seria > 10)])     #wyswietlanie wartosci nie wiekszych niz 10
print("")
print(seria[(seria <13) & (seria > 8)])     #wyswietlanie elementow z przedzialu
print("")
print(df[df["Populacja"] > 12345666])
print("")
print(df[((df.Populacja > 1234) & (df.index.isin([0,2])))])
print("")

szukaj = ['Belgia', 'Brazylia']
print((df.isin(szukaj)))
print("")

seria['C'] = 15
print(seria)
seria['E'] = 16
print(seria)
print("")

#DODAWANIE DANYCH
df.loc[3] = 'dodano'
print(df)
print("")
df.loc[4] = ['Polska', 'Warszawa', 383453656]
print(df)

#USUWANIE DANYCH
new = df.drop([3])      #zapisanie edycji danych do nowego pliku
print(new)
print("")
df.drop([3], inplace=True)      #zmiana danych w oryginalnym pliku
print(df)
print("")
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka', 'Europa']      #dodawanie nowej kolumny
print(df)
print("")
print(df.sort_values(by='Kraj'))                #sortowanie
print("")
grouped = df.groupby(['Kontynent'])             #grupowanie
print(grouped.get_group('Europa'))
print("")
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))     #agregacje danych (np. sumowanie populacji kontynentow)
print("")
print(u"____________________ suma częściowa ________________")
tabela = pd.pivot_table(df, values=['Populacja'], index='Kontynent', columns=['Kraj'], aggfunc=np.sum, margins=True)
print(tabela.stack('Kraj'))
