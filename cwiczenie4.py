"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 1
Zadanie 4 Usuwanie duplikatów
"""
def remove_duplicates(names):
    output=[]
    for i in names:
        if i not in output:
            output.append(i)
    return output

print "Oto wstepna lista z imionami:"
input=['Michal', 'Michal', 'Krystian', 'Krystian', 'Wieslaw', 'Marek', 'Tomek', 'Waldek', 'Marek', 'Tomek']
print input

print "Oto wyniki zastosowania funkcji: "
print remove_duplicates(input)

