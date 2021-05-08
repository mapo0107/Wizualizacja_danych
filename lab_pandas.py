import pandas as pd
import numpy as np
import xlrd
import openpyxl

#Zad1 Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

xlsx = pd.ExcelFile('pandas_imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)