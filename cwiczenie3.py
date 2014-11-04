"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sprawozdanie I
Zadanie 3: Funkcja kwadratowa i miejsca zerowe
"""
from math import sqrt
from array import *
def kwadratowa(a,b,c,x):
    return a*x**2+b*x+c
def miejsca_zerowe(a,b,c):
    delta=float(b**2-4*a*c)
    if delta>0:
        x1=(-float(b)+sqrt(delta))/(2.0*float(a))
        x2=(-float(b)-sqrt(delta))/(2.0*float(a))
        return x1, x2
    if delta==0:
        x0=(-float(b))/(2.0*float(a))
        return x0
    if delta<0:
        print "Brak rozwi�za� w zbiorze liczb naturalnych"

a=input("Prosz� wpisa� warto�� wsp�czynnika a: ")
b=input("Prosz� wpisa� warto�� wsp�czynnika b: ")
c=input("Prosz� wpisa� warto�� wsp�czynnika c: ")

print "Miejsca zerowe tej funkcji to: "
results=[miejsca_zerowe(a,b,c)]
print results

print "Warto�ci funkcji jakie przyjmuje w przedziale od -10 do 10: "
for x in range(-10,10,1):
    print kwadratowa(a,b,c,x)

    
