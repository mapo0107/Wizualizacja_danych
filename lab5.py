import numpy as np

#Zad1 Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
print("Zad1")
a = np.array([0, 1, 2])
b = np.array([4, 2, 5])
print("Pierwsza macierz:     ", a)
print("Druga macierz:        ", b)
print("Mnożenie macierzy:    ", a*b)


#Zad2 Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
print("\nZad2")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Macierz 3x3:\n", a)
print("Najmniejszy wiersz:", a.min(axis=0))
print("Najmniejsza kolumna:", a.min(axis=1))
print("Największy wiersz:", a.max(axis=0))
print("Największa kolumna:", a.max(axis=1))

b = np.array([[5, 6, 7, 8], [1, 2, 3, 4], [9, 10, 11, 12], [13, 14, 15, 16]])
print("\nMacierz 4x4:\n", b)
print("Najmniejszy wiersz:", b.min(axis=0))
print("Najmniejsza kolumna:", b.min(axis=1))
print("Największy wiersz:", b.max(axis=0))
print("Największa kolumna:", b.max(axis=1))


#Zad3 Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
print("\nZad3")
a = np.array([0, 1, 2])
b = np.array([4, 2, 5])
print("Iloczyn macierzy z zad1:", np.dot(a, b))


#Zad4 Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
print("\nZad4")
a = np.array([5, 2, 6])
b = np.array([1.5, 2.2, 0.1])
print("Mnożenie macierzy dwóch róźnych typów liczb:", a*b)


#Zad5 Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
print("\nZad5")
a = np.array([[1, 2], [3, 4], [5, 6]])
a = np.sin(a)
print("Sinus macierzy pod zmienną 'a':\n", a)


#Zad6 Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
print("\nZad6")
b = np.array([[1, 2], [3, 4], [5, 6]])
b = np.cos(b)
print("Cosinus macierzy pod zmienną 'b':\n", b)


#Zad7 Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
print("\nZad7")
print("Dodawanie macierzy z zad 5 i 6:\n", np.add(a,b))


#Zad8 Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
print("\nZad8")


#Zad9 Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
print("\nZad9")


#Zad10 Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
print("\nZad10")
print("Mamy 5 możliwość, ponieważ występują następujące dzielniki liczby 81: 1, 3, 9, 27, 81\n")
a = np.arange(81).reshape(9,9)
print("Macierz w formacie 9x9:\n", a)
a = a.reshape(1,81)
print("Macierz w formacie 1x81:\n", a)
a = a.reshape(3,27)
print("Macierz w formacie 3x27:\n", a)
a = a.reshape(27,3)
print("Macierz w formacie 27x3:\n", a)
a = a.reshape(81,1)
print("Macierz w formacie 81x1:\n", a)

#Zad11 Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
print("\nZad11")
