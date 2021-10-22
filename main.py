#kodilla zadanie Katarzyna Kuich
#Lista zakupów
#Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
#Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
#W sumie kupuję 6 produktów.

print("\nZadanie 1")
print("Lista zakupow:")

#product list
lista= {'Piekarnia':['Chleb', 'Pączek', 'Bułki'],
'Warzywniak':['Marchew', 'Seler', 'Rukola']
}

#loop key 

for x in lista:
  print("Idę do ",x ,"kupuję tu następujące rzeczy:",lista[x])
  

count=0
for key,value in lista.items():
    #counter
    count=len(value)+count

print("W sumie kupuję ",count," produktów.")

#Zadanie 2
#Napisz program, który:

#Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
#W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
print("\nZadanie 2")
print("Liczby podzielne przez 5 oraz podniesione do potegi 3")
lista_5=[]
lista_szesciany=[]
for i in range(0,101):
  if i % 5==0:
    lista_5.append(i)
    lista_szesciany.append(i**3)
print("\nLiczby podzielne przez 5:",lista_5)
print("\nSześciany liczb podzielnych przez 5:",lista_szesciany)
