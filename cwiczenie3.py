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
        print "Brak rozwi¹zañ w zbiorze liczb naturalnych"

a=input("Proszê wpisaæ wartoœæ wspó³czynnika a: ")
b=input("Proszê wpisaæ wartoœæ wspó³czynnika b: ")
c=input("Proszê wpisaæ wartoœæ wspó³czynnika c: ")

print "Miejsca zerowe tej funkcji to: "
results=[miejsca_zerowe(a,b,c)]
print results

print "Wartoœci funkcji jakie przyjmuje w przedziale od -10 do 10: "
for x in range(-10,10,1):
    print kwadratowa(a,b,c,x)

    
