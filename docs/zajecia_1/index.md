# Podstawy programowania: 7 listopada (środa) 16.30-19.30

### Zasady podstawowe

Mamy dość szerokie spektrum zagadnień i stosunkowo niedużo czasu. Kurs będzie starał
się w związku z tym iść na tyle szybko, na ile to możliwe - ale nie szybciej.

Jeśli ktoś ma problem/pytanie/wątpliwość, proszę to jak najszybciej sygnalizować.
Nieśmiałość w tej kwestii grozi robieniem zaległości, które coraz trudniej nadrobić.

Powyższe jest tym ważniejsze, że prowadzący może się chwilami zapędzić i używać
terminów, które wytłumaczył "nie dość dokładnie".

### Zestawienie środowiska

1. Na początek wchodzimy na stronę
[https://classroom.github.com/a/AHf59vSp](https://classroom.github.com/a/AHf59vSp).
Tam logujemy się danymi konta GitHubowego, co spowoduje utworzenie prywatnego
repozytorium, z którego każdy będzie korzystał przez cały kurs.

2. Kolejnym krokiem jest uruchomienie `PyCharma`. Wybieramy opcję stworzenia nowego projektu
 jako `Checkout from version control -> Git`.

3. W pole URL wklejamy adres repozytorium: `https://github.com/LaCH-UW/kurs-pythona-2018Z-<login-github>.git`
(inaczej: adres strony internetowej repozytorium z doklejoną końcówką `.git`;
 inaczej: na stronie internetowej repozytorium klikamy zielony guzik `Clone or download`, wybieramy
 `Use HTTPS` i kopiujemy podany tam adres).

4. `Directory` to katalog na dysku, w którym znajdzie się repozytorium. Ustawiamy wedle uznania.

5. Klikamy guzik `Log in to GitHub...` i logujemy się, po czym klikamy `Clone`.

6. Po udanym sklonowaniu projektu tworzeniu wirtualne środowisko Pythona:
`File -> Settings... -> Project Interpreter -> <ikonka trybika> -> Add -> New Environment`
(zwracamy uwagę, żeby jako `Base Interpreter` był Python 3.*)

### Pierwsza konsumpcja

1. Dwukrotnie klikając otwieramy folder `zajecia_1`, w nim dwukrotnie klikając 
otwieramy plik `pierwszy_program.py`. Klikamy prawym przyciskiem w oknie edytora 
i wybieramy `Run pierwszy_program` (lub naciskamy `Ctrl+Shift+F10`) 

2. Jeśli na dole otworzyło się okno zawierające napis "Witaj, świecie!"
i `Process finished with exit code 0`, możemy być z siebie zadowoleni.

### ~~Trzy słowa~~ Dużo słów o teorii (przeplatanej praktyką)

Python jest imperatywnym językiem programowania. Oznacza to, że programy
piszemy podając po kolei polecenia, które interpreter Pythona ma wykonać - a on
wykonuje je w zadanej kolejności (od góry do dołu).

Mimochodem poznaliśmy już jedno takie polecenie: funkcję `print()`. Pisząc:
```python
print("Testowy napis")
```
wydajemy polecenie wypisania **parametru przekazanego do funkcji print()**
(="tego, co jest nawiasie").

> Teraz jest dobry moment, żeby otworzyć sobie w edytorze PyCharma 
> plik `zajecia_1/kod_instruktazowy.py` i go konsumować. Możemy wykonać
> cały plik, klikając prawym przyciskiem myszy i `Run kod_instruktazowy`,
> lub tylko fragment - zaznaczając go, klikając prawym przyciskiem myszy
> i wybierając `Execute selection in console` (`Alt + Shift + E`)

> Uwaga: od znaku `#` w Pythonie zaczynają się komentarze - oznacza to, że
> wszystko od `#` do końca linii jest tylko adnotacją przeznaczoną dla ludzi;
> komputer to zignoruje (a PyCharm wyszarzy, żeby nam pomóc w pamiętaniu o tym) 

#### Podstawowe typy

Do funkcji `print()` możemy przekazać napis ("ciąg znaków", `string`), 
który otoczony jest cudzysłowami (pojedynczymi `'` lub podwójnymi `"`),
jak powyżej. Możemy też przekazać liczbę całkowitą (`int`) lub ułamek w notacji
dziesiętnej (z punktu widzenia komputera jest to tzw. liczba zmiennoprzecinkowa,
`float`):

```python
# printowanie inta
print(3)

# printowanie stringów
print("heeej")
print('hooo')

# printowanie floata
print(3.14)

# uwaga, to jest string (bo ma cudzysłowy)
print("3")

# print może dostać dowolnie dużo argumentów - wypisze je wszystkie, oddzielając spacjami
print(3, 4, 5, 12)

```

#### Operacje arytmetyczne

Na liczbach możemy przeprowadzać mniej lub bardziej złożone operacje arytmetyczne
(`+` dodawanie, `-` odejmowanie, `*` mnożenie, `/` dzielenie,
 `//` dzielenie całkowitoliczbowe (bez reszty),
 `%` modulo (reszta z dzielenia), `**` potęgowanie)
```python
print(2 + 2)
print(14 * (1 + 1) ** (12 - 9 // 3))
```

Stringi też można dodawać (a w zasadzie: konkatenować), ale nie można ich odejmować.
Możliwe jest też mnożenie stringa przez liczbę (!).
```python
print('St' + 'ój' + ' ' + 'H' + 'alina')
print('Ha' * 10)
```

#### Zmienne

W budowaniu poleceń wydatnie pomogą nam zmienne. Można o nich myśleć, jak
o etykietowanych kubełkach, w których jest "jakaś" zawartość. Odwołując się
do zmiennej (za pośrednictwem jej nazwy), odwołujemy się do jej wartości.

Zmienną deklarujemy (powołujemy do życia) przypisując jej jakąś wartość. Tę wartość
możemy potem zmieniać, ale nie możemy odwoływać się nigdy do zmiennej, która
nie została zadeklarowana (PyCharm podkreśli taką zmienną na czerwono).

Nazwa zmiennej musi zaczynać się od litery (konwencja każe, żeby ta litera była mała)
lub podkreślenia `_` i składać wyłącznie z liter, cyfr i `_`.

```python
# przypisanie na zmienną a wartości int 3 
a = 3
# wypisanie wartości zmiennej a
print(a)
# zmiana wartości a
a = 17
print(a)
# dla przypomnienia: wypisanie stringa "a"
print("a")
```

Na zmiennych możemy operować dokładnie tak, jak na obiektach na nich przechowywanych.

Nb. Zmienna może brać udział w przypisaniu po obu jego stronach; stała (np. liczbowa) - tylko po prawej.

```python
a = 4
b = a + 6
print(a + b)
```

> Ćwiczenie 1: policz, ile to jest 15 do potęgi 10, zapisz to na zmiennej wynik
> i wypisz wartość tej zmiennej.

#### Inne przydatne typy

Oprócz typów `string`, `int` i `float` przydatne nam będą typy:
* `list` (lista, czasem zwana tablicą), np. `[1.3, 2, 'skarb', 56]`
* `dict` (dictionary, słownik, mapa), np. `{'Marek': 32, 'Zbyszek': 11, 'Krzyś': 999}`
* `set` (zbiór), np. `{'Marek', 'Zbyszek', 'Zosia'}`
* `bool` (stałe boole'owskie, logiczne), `True` i `False`

#### Słowo o listach

Do poszczególnych elementów listy odwołujemy się po indeksie podanym w kwadratowym
nawiasie (uwaga, lista jest indeksowana od 0). Python pozwala także odwoływać
się do n-tego elementu "od końca", wówczas poprzedzamy liczbę znakiem `-`.

```python
moja_pierwsza_lista = [1.3, 2, 'skarb', 56]
print(moja_pierwsza_lista[0])
print(moja_pierwsza_lista[3])
print(moja_pierwsza_lista[-1])
```

Możemy także wyciągnąć wycinek (`slice`) listy, podając w kwadratowym nawiasie
indeks początkowy i "końcowy+1" (czyli "numer pierwszego elementu, który nie należy
do wycinka"), oddzielając je dwukropkiem `:`. Jeśli pominiemy indeks początkowy,
wycinek zacznie się od początku listy. Jeśli pominiemy koniec, wycinek skończy się
na końcu listy. 

```python
moja_pierwsza_lista = [1.3, 2, 'skarb', 56]
print(moja_pierwsza_lista[1:3])
print(moja_pierwsza_lista[:3])
print(moja_pierwsza_lista[2:])
```

Na raz zadeklarowanej liście możemy podmieniać elementy, przypisując nową wartość
do indeksu (wartość pod indeksem musi już być obecna w liście). 
Możemy także dodawać elementy metodą `append(nowy_obiekt)` (metody to funkcje powiązane
z obiektami; wołamy je przez `obiekt.metoda(argument)`, PyCharm podpowie nam
listę metod obiektu, gdy napiszemy kropkę).

```python
moja_pierwsza_lista = [1.3, 2, 'skarb', 56]
moja_pierwsza_lista.append('marny koniec')
moja_pierwsza_lista[0] = 13.11
print(moja_pierwsza_lista)
```

Nb. `string` jest "swego rodzaju" listą - możemy odwołać się do litery pod indeksem,
ale nie możemy jej podmienić.


#### Słowo o słownikach

O słowniku możemy myśleć jak o liście, której indeksy możemy kontrolować.
Zamiast używać kolejnych liczb 0, 1, 2..., klucze w słowniku możemy określać sami.
Analogicznie jak w przypadku listy możemy odczytać lub zapisać wartość pod kluczem.
Ponieważ klucze nie mają (i.e. nie muszą mieć) logicznej kolejności, dodajemy
nowy wpis przypisując wartość do nieistniejącego klucza - brak tu operacji append.

```python
moj_pierwszy_slownik = {'Zosia': 4, 'Krzysiek': 15}
print(moj_pierwszy_slownik['Zosia'])
moj_pierwszy_slownik['Marek'] = 0
print(moj_pierwszy_slownik)
print(moj_pierwszy_slownik['Marek'])
```

Mamy też możliwość sprawdzania, czy dany klucz jest w ogóle obecny w słowniku
(bez wyciągania wartości pod nim przechowywanej), za pomocą konstrukcji `klucz in slownik`.

```python
moj_pierwszy_slownik = {'Zosia': 4, 'Krzysiek': 15, 'Marek': 0}
print('Zosia' in moj_pierwszy_slownik)  # nb. wynikiem jest zmienna typu bool - True/False
print('Wacek' in moj_pierwszy_slownik)
```

#### Pół słowa o zbiorach

O zbiorze możemy myśleć jak o słowniku, który nie ma wartości (tylko klucze).
Wobec tego wyciąganie i zapisywanie wartości nie ma sensu, możemy za to użyć
konstrukcji `in`. Dodajemy specjalną metodą `add(nowy_obiekt)`

```python
moj_pierwszy_zbior = {'Polska', 'Francja'}
print('Francja' in moj_pierwszy_zbior)
print('Niemcy' in moj_pierwszy_zbior)
moj_pierwszy_zbior.add('Niemcy')
print('Niemcy' in moj_pierwszy_zbior)
```

#### Słowo o stringach

Stringi też mają swoje metody. Szczegółowiej porozmawiamy o nich na zajęciach 3,
warto chwilowo wspomnieć o `lower()` i `upper()`.
```python
print('NaPis'.lower())
print('NaPis'.upper())
```

#### Bardziej złożone operacje

Żeby faktycznie pisać programy, które wykonują więcej roboty niż my przy ich pisaniu,
potrzebujemy dwóch rzeczy:
możliwości powtarzania wykonania
oraz
warunkowania wykonania kodu różnymi okolicznościami.

Wielokrotne powtarzanie kodu uzyskujemy za pomocą pętli `for`.

W pętli for wyróżniamy deklarację pętli (`for nazwa_zmiennej in obiekt_po_ktorym_iterujemy:`)
oraz ciało pętli - kod, który jest wykonywany raz dla każdego elementu iterowanego 
obiektu. Ciało pętli może mieć dowolnie dużo linii - jego koniec poznajemy po końcu wcięcia.

```python
suma = 0
for liczba in [0, 1, 2, 3, 4, 5]:  # deklaracja pętli
    suma += liczba  # ciało pętli; skrócony zapis na: suma = suma + liczba 
    print('Wynik częściowy:', suma, 'w obrocie pętli numer', liczba)  # dalej ciało pętli
print('Wynik końcowy:', suma)  # już nie ciało pętli
```

Nb. Powyższe można napisać krócej za pomocą funkcji `range(n)`, która generuje
ciąg kolejnych liczb całkowitych od `0` do `n-1`.

```python
suma = 0
for liczba in range(6):
    suma += liczba
print('Wynik końcowy:', suma)
```

Warunkowe wykonanie kodu umożliwia konstrukcja warunkowa `if`.

```python
if 4 < 5:
    print('No raczej')
else:
    print('Pisanie tego kodu jest niemądrą stratą czasu')
    s = znajdz_sens_zycia()
    print(s)
```

Zauważmy, że mamy tutaj dwa "wcięte" bloki - pierwszy (po `if warunek:`) jest
wykonywany, kiedy warunek jest prawdziwy, drugi (po `else:`) w przeciwnym
przypadku.

Operatory porównania, których możemy używać w warunku `if`:
* `a == b` - a takie samo jak b
* `a != b` - a nie jest takie samo jak b
* `a is b` - a jest tym samym co b (czasem to ważne rozróżnienie; na co dzień używajmy ==)
* `a in b` - element a znajduje się w obiekcie b; b powinno być napisem, listą lub słownikiem
* `a < b` (`a > b`) - a jest mniejsze (większe) od b
* `a <= b` (`a >= b`) - a jest mniejsze (większe) lub równe od b

Dodatkowo warunki możemy łączyć słowami `or` i `and` lub poprzedzić słowem `not`.

> Ćwiczenie 2 (for): Zsumuj liczby 0..100.

> Ćwiczenie 3 (for + if): Zsumuj te sposród liczb 0..100, które są podzielne przez 5.


#### Funkcje i moduły

Kod możemy (i powinniśmy) organizować w funkcje, a je w moduły.

Funkcja dzieli się na nagłówek i ciało. Nagłówek zawiera nazwę funkcji i argumenty,
które można/trzeba przekazać do niej, i zaczyna się od słowa `def`, a kończy dwukropkiem.
Ciało funkcji zawiera jej logikę; kończy się tam, gdzie kończy się blok wciętego kodu.
W ciele funkcji możemy użyć słowa kluczowego `return`: powoduje ono przerwanie 
wykonywania funkcji i zwrócenie przez funkcję podanej wartości.

```python
def podwojenie(x):
    return 2 * x

print(podwojenie(10))
print(podwojenie('ha'))
```

W pewnym uproszczeniu: pliki zawierające kod Pythonowy (i zawierające je katalogi) 
stają się modułami. Możemy odwoływać się do nich przez słowo kluczowe `import`.

```python
import zajecia_1.kod_pomocniczy
super_wynik = zajecia_1.kod_pomocniczy.zwielokrotnienie(10, 4)
print(super_wynik)
print(zajecia_1.kod_pomocniczy.zwielokrotnienie('ha', 6))
```

Jeśli chcemy zaimportować tylko część modułu, możemy użyć konstrukcji
`from modul import nazwa` - daje to też krótszy kod korzystający z modułu.

```python
from zajecia_1.kod_pomocniczy import zwielokrotnienie
print(zwielokrotnienie(20, 4))
```

Moduł `zajecia_1.kod_pomocniczy` to kod zawarty w pliku `zajecia_1/kod_pomocniczy.py`.
Warto do niego zajrzeć.

Nb. PyCharm pozwala skoczyć do modułu poprzez kliknięcie na jego nazwie z `Ctrl`.

> Ćwiczenie 4: Napisz funkcję o nazwie pan_funkcja, która poprzedzi każdy 
> przekazany jej napis słowem "pan":

```
>>> print(pan_funkcja('Tadeusz'))
pan Tadeusz
```

Nb2. Python jest znany z tego, że posiada liczne i pożyteczne moduły w bibliotece
standardowej. Możemy uzyskać do nich (jak i do zewnętrznych bibliotek, które
w przyszłości zainstalujemy) dostęp właśnie za pomocą `import`.

```python
import datetime
today = datetime.date.today()
print(today)
print(today.weekday())  # liczba 0 - poniedziałek, 1 - wtorek etc.
from zajecia_1.kod_pomocniczy import dzien_tygodnia
print(dzien_tygodnia(today.weekday()))
print(dzien_tygodnia(
    datetime.date(year=1939, month=9, day=1).weekday()
))
```

> Praca domowa: Stwórz plik `zajecia_1/praca_domowa.py`, a w nim funkcje:
> * `skracacz`, która obetnie podany w argumencie napis do 10 znaków i doda na końcu wielokropek.
> * `madry_skracacz`, która dodaje wielokropek tylko wtedy, jeśli faktycznie coś skróciła.
> * `palindromator`, która przyjmie liczbę i wygeneruje palindrom postaci baaa..aaab 
>    o długości wyrażonej tą liczbą. Palindrom o długości 1 to b, o długości 2 to bb.
>
> Następnie użyj funkcji `palindromator` do wygenerowania 100 palindromów 
> o długościach 1, 2, ... i wypisz palindromy nr. 3, 7, 15, 62.
