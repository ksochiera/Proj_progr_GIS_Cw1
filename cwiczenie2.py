"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sprawozdanie I
Zadanie 2: Sprawdzanie polidromów
"""
zdanie=(raw_input("Proszê wpisaæ zdanie, które sprawdzimy, czy jest palindromem: " ).lower())
zdanie=zdanie.replace(" ","")
zdanie_wspak=zdanie[::-1]
wynik=zdanie==zdanie_wspak
print wynik