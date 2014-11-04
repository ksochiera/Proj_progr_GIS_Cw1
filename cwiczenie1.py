"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 1
Zadanie 1 "Fizz Buzz"
"""
n=int(input("Proszê wpisz dowoln¹ dodatni¹ liczbê: "))
if n<=0:
    print "To nie jest liczba dodatnia"
    while True:
        break
zakres=range(1,n+1)
for liczba in zakres:
    if liczba%3==0 and liczba%5==1 or liczba==3:
        print "Fizz"
    elif liczba%5==0 and liczba%3==1 or liczba==5:
        print "Buzz"
    elif liczba%3==0 and liczba%5==0:
        print "Fizz Buzz"
    else:
        print liczba
