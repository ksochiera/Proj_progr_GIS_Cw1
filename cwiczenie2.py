"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sprawozdanie I
Zadanie 2: Sprawdzanie polidrom�w
"""
zdanie=(raw_input("Prosz� wpisa� zdanie, kt�re sprawdzimy, czy jest palindromem: " ).lower())
zdanie=zdanie.replace(" ","")
zdanie_wspak=zdanie[::-1]
wynik=zdanie==zdanie_wspak
print wynik