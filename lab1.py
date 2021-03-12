#Marcin Polkowski
#Zadania lab1

#Zad1 - dwie zmienne
string1 = 'Marcin'
string2 = 'Polkowski'
integer1 = int(1)
integer2 = int(2)
float1 = float(1.1)
float2 = float(2.22)
complex1 = complex(3,4)
complex2 = complex(3j+3j)

print("Zmienne string to: %s, %s" %(string1, string2))
print("Zmienne int to: %d, %d" %(integer1, integer2))
print("Zmienne float to: %.1f, %.2f " %(float1, float2))
print("Zmienne complex to: {}, {} " .format(complex1, complex2))
print("Zmienna complex1: {}, real part: {}, imaginary part: {}" .format(complex1, complex1.real, complex1.imag))

#Zad2 - operatory przyrostkowe
op1 = 1
op1 += 1
print(op1)
op2 = 2
op2 -= 2
print(op2)
op3 = 3
op3 *= 3
print(op3)
op4 = 4
op4 /= 4.444
print(op4)
op5 = 5
op5 **= 5
print(op5)
op6 = 6
op6 %= 6
print(op6)

#Zad3 - liczenie wyrazenia
from math import *
print(exp(10))
print(log(5 + sin(8) ** 2) ** (1 / 6))
#dwoch pozostalych zadan matematycznych niestety nie rozumiem

#Zad4 - zmiana wielkosci liter - capitalize
imie = "MARCIN"
naziwsko = "POLKOWSKI"
print(imie.capitalize(), naziwsko.capitalize())

#Zad5 - zlicznie slow - count
lyrics = "Ring ding ding daa baa Baa aramba baa bom baa barooumba Wh-wha-what's going on-on? Ding, ding This is the Crazy Frog Ding, ding Bem, bem!" \
         "Ring ding ding ding ding ding Ring ding ding ding bem bem bem Ring ding ding ding ding ding Ring ding ding ding baa baa Ring ding ding ding ding ding" \
         "Ring ding ding ding bem bem bem Ring ding ding ding ding ding This is the Crazy Frog Breakdown! Ding, ding Br-br-break it, br-break it" \
         "Dum dum dumda dum dum dum Dum dum dumda dum dum dum Dum dum dumda dum dum dum Bem, bem! Dum dum dumda dum dum dum Dum dum dumda dum dum dum Dum dum dumda dum dum dum" \
         "This is the Crazy Frog A ram me ma bra ba bra bra rim bran Dran drra ma mababa baabeeeaaaaaaa! Ding, ding This is the Crazy Frog Ding, ding Da, da" \
         "Ring ding ding ding ding ding  Ring ding ding…"
ring = lyrics.count("Ring") + lyrics.count("ring")
ding = lyrics.count("Ding") + lyrics.count("ding")
print("Ring wystapilo: %d \nDing wystapilo: %d" %(ring, ding))

#Zad6 - zabawa indeksami lancucha znakow - len (od lenght)
chain = "abc def ghi jkl mno prsq tuv wxyz"
print("Drugi znak lancucha to:", chain[1] + ", "  + "natomiast ostatni znak lancucha to:", chain[len(chain)-1])
print("Uwaga! Spacje tez sa indeksowane!")
indexb = chain.index('b')
indexz = chain.index('z')
#print(indexb, indexz)
print("Litera 'b' ma index:", indexb)
print("Litera 'z' ma indeks:", indexz)

#Zad7 - dzielenie na wyrazy - split
chain2 = "abc def ghi jkl mno prsq tuv wxyz"
split = chain2.split()
print(split)
print("Drugi wyraz to:", split[1] + ", " + "natomiast ostatni to:", split[len(split)-1])

#Zad8 - formatowanie wyswietlania zmiennych
string3 = 'ABCDEFGHIJKLMNPPRSQTUVWXYZ'
integer3 = 3
float3 = 987.654321
hex = 0xABCD1234
print(string3, "jest zmienna typu", type(string3))
print(int(integer3), "jest zmienna typu",  type(integer3))
print(float(float3), "jest zmienna typu",  type(float3))
#W przeciwienstwie do powyzszych zmiennych, przy hex musimy zadeklarowac wlasciwy operator (%x)
print("%x" % hex, "jest zmienna typu", type(hex))
#Jesli tego nie zrobimy to zmienna hex przekonwertuje sie do dec jak ponizej
print("Ciekawostka: ", hex, "jest przekonwertowane z %x z HEX na DEC" % hex)

# #Zad9 - odwrocona lista i dodawanie - reverse i append
tab = ["motocross", "rallycross", "tenis", u"łyżwy"]
print(tab)
tab.reverse()
print(tab)
tab.append(u"piłka nożna")
tab.append(u"piłka ręczna")
tab.append("skoki narciarskie")
print(tab)

# #Zad10 - slownik skrotow
dictionary = {"nr": "numer", "pkt": "punkt", "wyd.": "wydanie", "tj.": "to jest", "itd.": "i tak dalej", "cd.": u"ciąg dalszy nastąpi"}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary["itd."])
