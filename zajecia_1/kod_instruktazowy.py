
# printowanie inta
print(3)

# printowanie stringów
print("heeej")
print('hooo')

# printowanie floata
print(3.14)

# print może dostać dowolnie dużo argumentów - wypisze je wszystkie, oddzielając spacjami
print(3, 4, 5, 12)

# uwaga, to jest string (bo ma cudzysłowy)
print("3")

# proste działania arytmetyczne
print(2 + 2)
print(14 * (1 + 1) ** (12 - 9 // 3))

# działania na stringach
print('St' + 'ój' + ' ' + 'H' + 'alina')
print('Ha' * 10)

# przypisanie na zmienną a wartości int 3
a = 3
# wypisanie wartości zmiennej a
print(a)
# zmiana wartości a
a = 17
print(a)
# dla przypomnienia: wypisanie stringa "a"
print("a")

# operacje na zmiennych
a = 4
b = a + 6
print(a + b)

# TU JEST MIEJSCE NA ĆWICZENIE 1
# > Ćwiczenie 1: policz, ile to jest 15 do potęgi 10, zapisz to na zmiennej wynik
# > i wypisz wartość tej zmiennej.
print()

# odwołania do elementów listy
moja_pierwsza_lista = [1.3, 2, 'skarb', 56]
print(moja_pierwsza_lista[0])
print(moja_pierwsza_lista[3])
print(moja_pierwsza_lista[-1])

# wycinki
print(moja_pierwsza_lista[1:3])
print(moja_pierwsza_lista[:3])
print(moja_pierwsza_lista[2:])

# dodawanie/podmienianie elementów
moja_pierwsza_lista.append('marny koniec')
moja_pierwsza_lista[0] = 13.11
print(moja_pierwsza_lista)

# operacje na słowniku
moj_pierwszy_slownik = {'Zosia': 4, 'Krzysiek': 15}
print(moj_pierwszy_slownik['Zosia'])
moj_pierwszy_slownik['Marek'] = 0
print(moj_pierwszy_slownik)
print(moj_pierwszy_slownik['Marek'])
print('Zosia' in moj_pierwszy_slownik)  # nb. wynikiem jest zmienna typu bool - True/False
print('Wacek' in moj_pierwszy_slownik)

# operacje na zbiorze
moj_pierwszy_zbior = {'Polska', 'Francja'}
print('Francja' in moj_pierwszy_zbior)
print('Niemcy' in moj_pierwszy_zbior)
moj_pierwszy_zbior.add('Niemcy')
print('Niemcy' in moj_pierwszy_zbior)

# stringi
print('NaPis'.lower())
print('NaPis'.upper())

# pętla
suma = 0
for liczba in [0, 1, 2, 3, 4, 5]:  # deklaracja pętli
    suma += liczba  # ciało pętli; skrócony zapis na: suma = suma + liczba
    print('Wynik częściowy:', suma, 'w obrocie pętli numer', liczba)  # dalej ciało pętli
print('Wynik końcowy:', suma)  # już nie ciało pętli

suma = 0
for liczba in range(6):
    suma += liczba
print('Wynik końcowy:', suma)

# instrukcja warunkowa
if 4 < 5:
    print('No raczej')
else:
    print('Pisanie tego kodu jest niemądrą stratą czasu')
    s = znajdz_sens_zycia()
    print(s)

# TU JEST MIEJSCE NA ĆWICZENIA 2 i 3
#> Ćwiczenie 2 (for): Zsumuj liczby 0..100.
#> Ćwiczenie 3 (for + if): Zsumuj te sposród liczb 0..100, które są podzielne przez 5.

# funckja
def podwojenie(x):
    return 2 * x

print(podwojenie(10))
print(podwojenie('ha'))

# import modułu
import zajecia_1.kod_pomocniczy
super_wynik = zajecia_1.kod_pomocniczy.zwielokrotnienie(10, 4)
print(super_wynik)
print(zajecia_1.kod_pomocniczy.zwielokrotnienie('ha', 6))

# inny import modułu
from zajecia_1.kod_pomocniczy import zwielokrotnienie
print(zwielokrotnienie(20, 4))

# TU JEST MIEJSCE NA ĆWICZENIE 4
# > Ćwiczenie 4: Napisz funkcję o nazwie pan_funkcja, która poprzedzi każdy
# > przekazany jej napis słowem "pan":

# print(pan_funkcja('Tadeusz'))

import datetime
today = datetime.date.today()
print(today)
print(today.weekday())  # liczba 0 - poniedziałek, 1 - wtorek etc.
from zajecia_1.kod_pomocniczy import dzien_tygodnia
print(dzien_tygodnia(today.weekday()))
print(dzien_tygodnia(
    datetime.date(year=1939, month=9, day=1).weekday()
))
