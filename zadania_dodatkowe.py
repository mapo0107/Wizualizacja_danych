#Zadanie WD#001


#===================================================================================================

#Zadanie WD#002
#Ponieważ drugi argument w "range" jest arg-1, to właściwy zapis powinien wyglądać jak poniżej
#Tj. jeśli chcemy sprawdzić to w zakresie od 100 do 200 włącznie powinniśmy zapisać 201
for a in range(100, 201):
    if a % 11 == 0 and a % 15 != 0:
        print(a)
#Poniżej dowód powyższej tezy dla liczb od 100 do 200 podzielnych przez 10
for b in range(100, 200):
    if b % 10 == 0:
        print(b)
print('Liczba 200 nie jest zwracana w wynikach.')

for c in range(100, 201):
    if c % 10 == 0:
        print(c)
print(u'A w tym przypadku liczba 200 jest już zwracana w wynikach.')

#===================================================================================================

#Zadanie WD#003





#===================================================================================================

#Zadanie WD#004
#inny sposób na sumowanie :)
numbers1 = [5, 2]
numbers2 = [-5, 2]
numbers3 = [5, -2]
numbers4 = [5.0, -2]
numbers_sum1 = sum(numbers1)
numbers_sum2 = sum(numbers2)
numbers_sum3 = sum(numbers3)
numbers_sum4 = sum(numbers4)
print(numbers_sum1,'|',numbers_sum2,'|',numbers_sum3,'|',numbers_sum4)