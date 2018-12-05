# Automatyczna obróbka plików tekstowych: 5 grudnia (środa) 16.30-19.30

> Przypomnienie:
> ```python
> with open('dane/lalka-tom-drugi.txt', encoding='utf-8') as fp:
>    tekst = fp.read()
>```

## Liczenie słów w tekście

#### Wersja 'chcemy policzyć tylko jedno słowo'

```python
def wersja_1(text, searched_word):
    count = 0
    for word in text.split():
        if word == searched_word:
            count += 1

    return count
```

#### Wersja naiwna

```python
def wersja_2(text):
    struct = []
    for word in text.split():
        struct.append(word)

    return struct
```

#### Wersja dużo-lepsza: wyszukiwanie w słowniku jest szybsze

```python
def wersja_3(text):
    struct = {}
    for word in text.split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
```

Uwaga: Ponieważ dane słowo jest dodawane do słownika przy pierwszym wystąpieniu to byłby błąd: `dane_3['carewicz']`

Możemy użyć polecenia `get()` (drugi parametr jest wartością zwracaną przez metodę, jeśli klucza nie ma w słowniku):
`dane_3.get('carewicz', 0)`

> Ćwiczenie 2:
> 1. Weź 20 pierwszych "słów" z tekstu Lalki.
> 2. Policz ile razy każde z nich występuje w tekście.

Powyższe metody liczenia są z gruntu wadliwe. Co im dolega?

Po pierwsze, jest kwestia wielkości liter:
```python
> print(dane_3.get('dzień', 0))
59
> print(dane_3.get('Dzień', 0))
7
```

```python
def wersja_4(text):
    struct = {}
    for word in text.casefold().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
```

Po drugie, warto się pozbyć znaków niealfanumerycznych:
```python
def wersja_5(text):
    struct = {}
    for word in text.replace('.', '').replace('?', '').replace('!', '').replace('…', '').casefold().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
```

> Ćwiczenie 3: Wykonaj polecenia z ćwiczenia 2 licząc "bardziej słowa". Porównaj wyniki.
> Czy na pewno wyrzuciliśmy wszystkie znaki interpunkcyjne? Jak mieć pewność?

https://en.wikipedia.org/wiki/Unicode_character_property

```python
import unicodedata

> print(unicodedata.category('a'))
Ll
> print(unicodedata.category('A'))
Lu
> print(unicodedata.category('.'))
Po
> print(unicodedata.category(' '))
Zs
> print(unicodedata.category('1'))
Nd
> print(unicodedata.category('\n'))
Cc
```

```python
import unicodedata

def wersja_6(text):
    struct = {}
    for word in ''.join(c for c in text if unicodedata.category(c) != 'Po').upper().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
```

Czy to jest dobrze? Skąd wiemy co chcemy wyrzucić?

> Ćwiczenie 4: Zbuduj (i obejrzyj) mapę znaków i ich klas unicode'owych

```python
import unicodedata

def wersja_7(text):
    struct = {}
    for word in ''.join(c for c in text if not unicodedata.category(c).startswith('P')).upper().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
```

## Obróbka za pomocą NLTK
```python
import nltk  # sytuacja jak z reequests - powinnismy zainstalować nltk
nltk.download('punkt')  # przed pierwszym użyciem musimy ściągnąć paczkę z tokenizerami

from nltk.tokenize import sent_tokenize, word_tokenize

s = sent_tokenize(tekst, language='polish')
print(s[:10])

w = word_tokenize(tekst, language='polish')
print(w[:20])
```

## Formaty inne niż "goły tekst"

#### DOCX

```python
import docx  # wymaga instalacji modułu python-docx
# https://python-docx.readthedocs.io/en/latest/index.html

pbp_fname = 'dane/pbp.docx'
doc = docx.Document(pbp_fname)

print(len(doc.paragraphs))
print(len(doc.tables))
second_table = doc.tables[1]
title_column = second_table.columns[0]
for cell in title_column.cells:
    print(cell.text)
```

#### XLS / XLSX
Na początek: "nowy Excel" (.xlsx) i wpływy do budżetu - dane z https://danepubliczne.gov.pl/dataset/wplywy_budzetowe vs biblioteka openpyxl.

```python
import openpyxl
# https://openpyxl.readthedocs.io/en/default/tutorial.html

budget_fname = 'dane/budzet/2017_1.xlsx'
wb = openpyxl.load_workbook(budget_fname)
sheet = wb.worksheets[0]

header_row = list(sheet.rows)[0]
for header_cell in header_row:
    print(header_cell.column, header_cell.row, header_cell.value)
    
print(sheet['A2'].value)

first_column = list(sheet.columns)[0]
for name_cell in first_column:
    print(name_cell.value)

wb.close()
```

Drugi przykład: "stary Excel" (.xls) i "absencje chorobowe" - dane z https://danepubliczne.gov.pl/dataset/absencja_chorobowa vs biblioteka xlrd.

```python
import xlrd
# z dokumentacją nie ma szału...
# https://github.com/python-excel/tutorial/raw/master/python-excel.pdf
# https://xlrd.readthedocs.io/en/latest/
# ale głównie należy wołać help() i dir() na czym się da...

absence_fname = 'dane/zus/2013.xls'
wb = xlrd.open_workbook(absence_fname)
sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows):
    for cell in sheet.row(i):
        if cell.value == 'OGÓŁEM':
            start_row = i
            break

for i in range(start_row, start_row + 5):
    for cell in sheet.row(i):
        print(cell.value)
```


#### PDF 

Tutaj różnie bywa z dostępnymi danymi.

Można trafić na zeskanowane i "zPDFizowane" kartki (np. https://danepubliczne.gov.pl/dataset/sprawozdanie-z-dzialalnosci-pot-w-2016-roku) - z nimi cudów nie zrobimy.

Istnieją oczywiście PDFy z tekstem - wyciąganie go i tak bywa niewygodne, ale można walczyć: pypdf2 vs "Plan działania POT na 2018 rok" https://danepubliczne.gov.pl/dataset/plan-dzialania-na-rok-2018

```python
import PyPDF2  # wymaga instalacji pypdf2
# https://pythonhosted.org/PyPDF2/

pot_fname = 'dane/pot_2018.pdf'
with open(pot_fname, 'rb') as fp:  # 'rb' oznacz odczyt w trybie binarnym (nie otwieramy pliku jako tekst, tylko surowe dane)
    pdf = PyPDF2.PdfFileReader(fp)
    print(pdf.numPages)
    a_page = pdf.getPage(102)
    print(a_page.extractText()[:100])
```


### Praca domowa

0. Zaległe prace domowe dalej obowiązują.

1. Współczynnik bogactwa leksykalnego tekstu to stosunek liczby różnych słów
w tekście do łącznej liczby słów w tekście.
W pliku `zajecia_2/praca_domowa.py` napisz funkcję `oblicz_bogactwo(sciezka_pliku)`,
która policzy współczynnik bogactwa leksykalnego dla tekstu zawartego w pliku
o podanej w parametrze nazwie. Przetestuj ją na pierwszy tomie Lalki

2. Napisz funcję `ile_dlugich(sciezka_pliku)`, która policzy ile zdań mających 
więcej niż 7 słów jest w tekście zawartym w pliku o podanej w parametrze nazwie.

3. Napisz funkcję `ile_dlugich_n(sciezka_pliku, min_dl)`, która policzy ile 
zdań mających więcej niż `min_dl` słów jest w tekście zawartym w pliku 
o podanej w parametrze nazwie.

4. (Dla ambitnych) Napisz funkcję maim(fname_in, fname_out), która: wczyta 
tekst z pliku fname_in i wypisze do pliku fname_out jego zawartość pozbawioną 
diakrytów (np. zamieni 'żółty' na 'zolty').
    
    Podpowiedź 1: przeczytaj https://docs.python.org/3/library/unicodedata.html

    Podpowiedź 2: funkcja unicodedata.normalize('NFD', text) rozbija znaki 
na części składowe (np. 'ą' na 'a' i 'ogonek'), funkcja 
unicodedata.normalize('NFC', text) wykonuje operację odwrotną

    Podpowiedź 2b: informacja w 2 jest "prawie zawsze" prawdą. Zachowaj czujność!

Pracę domową proszę wypushować do swojego repozytorium do 23:59 2018-12-16.
