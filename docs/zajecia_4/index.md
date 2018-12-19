# Programowy dostęp do zasobów internetowych: 19 grudnia (środa) 16.30-19.30

Uwaga: Dzisiejsze zajęcia (bardziej niż którekolwiek z poprzednich) zawierają więcej materiału, niż jakikolwiek
rozsądny prowadzący powinien przekazać na jednych zajęciach. Dlatego sporo zagadnień prawdopodobnie przelecimy w biegu,
i zachęcam do spokojnego przeczytania w domu tych slajdów, i podłubania w kodzie.

Polecenie get z modułu `requests` pozwala na wykonywanie requestu `HTTP GET` (i w efekcie zaciąganie
plików udostępnionych jako "strony internetowe".

```python
import requests  # moduł requests nie jest wbudowany w instalację pythona, ale powinniśmy go byli zainstalować na zajeciach 2.

result = requests.get('https://wolnelektury.pl/media/book/txt/lalka-tom-pierwszy.txt')
print(result.status_code)  # 200 oznacza sukces, 4** oznacza błędny request (nasza wina), 5** oznacza błąd serwera (często nie nasza wina)
tekst = result.text

print(tekst[:100])
```

> Ćwiczenie 1: Zapiszmy na dysku pierwszy tom Lalki.

> Ćwiczenie 2: Policzmy słowa w pierwszym tomie Lalki
(najlepiej nltk)

W poprzednim przykładzie dostaliśmy surowy plik tekstowy -- to w rzeczywistym świecie bardzo rzadki przypadek.
Na poprzednich zajęciach rozmawialiśmy o doc(x), xls(x) i pdf, ale w zasoby internetowe mają też charaktertystyczne
dla siebie formaty.

Często będziemy mieć do czynienia z danymi w formacie XML lub JSON (jeśli mamy szczęście i są ustrukturyzowane)
lub HTML (jeśli mamy mniej szczęścia).

### JSON (JavaScript Object Notation)

NB. Korzystamy tutaj z API GitHuba (=Application Programing Interface, zasoby zaplanowane specjalnie pod
dostęp programowy).

```python
import requests

r = requests.get('https://api.github.com/users/{user}'.format(user='piotrkasprzyk'))
j_data = r.json()

print(j_data)
```

Jak "widać" JSON rozparsował się do zwykłego słownika (`dict`)

```python
print(j_data['name'])
print(j_data['url'])
print(j_data['avatar_url'])
```

Ostatnie jest linkiem do obrazka - avatara. Jego też możemy ściągnąć i wyświetlić.

### Interludium: obrazki

```python
from PIL import Image  # ta linijka, z przyczyn historycznych, wymaga zainstalowania "pillow"
from io import BytesIO  # a to jest biblioteka standardowa

avatar_url = j_data['avatar_url']
r = requests.get(avatar_url)
i = Image.open(BytesIO(r.content))
i.show()
```

> Ćwiczenie 3: Wyświetl swój avatar GitHubowy.

> ( dla zainteresowanych: avatar == "zdjęcie profilowe", można zmienić w https://github.com/settings/profile )

Uwaga: obrazek jest plikiem binarnym, i jeśli chcemy zapisać go do pliku, powinniśmy ten plik otworzyć do zapisu
w trybie binarnym (wówczas Python nie interesuje się kodowaniem):

```python
with open('moj_avatar.jpg', 'wb') as fp:
    i.save(fp)
```

Analogicznie powinniśmy wczytywać obrazek z lokalnego pliku:

```python
with open('moj_avatar.jpg', 'rb') as fp:
    i = Image.open(fp)
```

### Koniec interludium: mojepanstwo.pl

Link podstawowy z informacjami o API: https://mojepanstwo.pl/api/

```python
r = requests.get('https://api-v3.mojepanstwo.pl/dane/krs_formy_prawne.json')

json_data = r.json()

print(json_data)
```

> Ćwiczenie 4: Znajdź identyfikator formy prawnej "kółko rolnicze" w bazie mojepanstwo.pl
> ( pomocny link: https://api-v3.mojepanstwo.pl/dane/krs_formy_prawne.json )

> Ćwiczenie 5: Ustal, ile jest kółek rolniczych w bazie mojepanstwo.pl
> ( pomocny link: https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={id-formy-prawnej} )

Spróbujmy znaleźć najstarsze Kółko Rolnicze w KRS (wg. daty rejestracji u Mojego Państwa)

```python
import requests

id_kolka_rolniczego = 5

r = requests.get('https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}'.format(id_kolka_rolniczego))
json_data = r.json()
print(len(json_data['Dataobject']))
print(json_data['Count'])
```

Jak widać, MojePaństwo zwraca wyniki w paczkach po 50 sztuk.
Krótka lektura https://mojepanstwo.pl/api/krs pozwoli nam zmodyfikować request tak, aby ściagał dane w paczkach
po 500 sztuk (tyle się da maksymalnie).

```python
import requests

id_kolka_rolniczego = 5

r = requests.get('https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}&limit=500'.format(id_kolka_rolniczego))
json_data = r.json()
print(len(json_data['Dataobject']))
print(json_data['Count'])
print(json_data['Links'].keys())  # nawigacja: poprzednia strona, kolejna strona etc.
```

Jak zatem ściągnąć wszystkie dane (i nie zadławić strony MojePaństwo)?
1. Pętla
2. Funkcja sleep z biblioteki time
3. Zapis do pliku (żeby nie ściągać za każdym razem jak chcemy nad nimi pracować)

#### while

```python
# jeśli nie wiemy ile iteracji pętli nas czeka (ale wiemy kiedy chcemy skończyć), pętla while jest dobrym rozwiązaniem

import random

liczba_iteracji = random.randint(50, 100)  # losowa liczba całkowita z przedziału <50, 100)

suma = 0
while liczba_iteracji > 0:
    suma += liczba_iteracji
    liczba_iteracji -= 1

print(suma)
```

#### sleep

Funkcja sleep w module time zatrzymuje bieg programu na ustaloną liczbę sekund ("odczekuje" trochę)/

```python
import time

print('zaczynamy')
time.sleep(1)
print('minęła sekunda')
time.sleep(0.5)
print('minęło kolejne pół sekundy')
```

#### Moduł json

Moduł `json` służy do konwersji json <-> pythonowe struktury (przedtem robił to za nas `requests`).

```python
import json

s = {'lista': ['elt1', 2, 'elt3'], 'liczba': 42}
print(repr(s))  # funkcja repr() formatuje trochę inaczej, ułatwiając rozpoznawanie typów
json_s = json.dumps(s)
print(repr(json_s))
parsed_s = json.loads(json_s)
print(repr(parsed_s))
```

Na marginesie:
```python
print('1')
print(1)
print(repr('2'))
print(repr(2))
```

#### Kompletny download:

```python
import time
import json
import requests

lista_kolek_rolniczych_po_500 = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}&limit=500'.format(id_kolka_rolniczego)

# print(dane[0].keys())
def dump_all_pages(first_page_link, fname):
    # zerujemy plik
    open(fname, 'w', encoding='utf-8').close()
    current_link = first_page_link
    while current_link is not None:
        r = requests.get(current_link)
        print("getting: ", current_link)
        json_data = r.json()
        with open(fname, 'a', encoding='utf-8') as fp:
            for obj in json_data['Dataobject']:
                fp.write(json.dumps(obj) + '\n')
        current_link = json_data['Links']['next'] if 'next' in json_data['Links'] else None
        time.sleep(1)

# dump_all_pages(lista_kolek_rolniczych_po_500, '../dane/kolka_rolnicze.json')
```

Żeby nie krzywdzić MojegoPaństwa na zajęciach (tudzież jakby miało przejściowe problemy), plik wynikowy znajduje się
w materiałach: `kolka_rolnicze.json`

> Ćwiczenie 6: Wczytaj dane o kółkach rolniczych na zmienną kolka
z pliku ../dane/kolka_rolnicze.json; użyj biblioteki json

> Ćwiczenie 7: Znajdź klucz zawierający datę rejestracji kółka
Weźmy przykładową datę rejestacji: '2017-12-12'
Sortowanie jest w tym przypadku łatwe - data jest w formacie ISO 8601, w której porządek leksykograficzny odpowiada porządkowi chronologicznemu.

Potrzebujemy teraz tylko sortowania -- służy to tego funkcja sorted, która zwraca elementy w posortowanej kolejności.
Prosty przypadek:

```python
for i in sorted([5, 2, 1, 3, 4]):
    print(i)
```

Nieprosty przypadek -- słowniki nie mają porządku, więc musimy podać klucz, po którym sortujemy:
```python
l = {'a': 5, 'b': 'a'}, {'a': 2, 'b': 'o'}, {'a': 1, 'b': 'z'}, {'a': 3, 'b': 's'}, {'a': 4, 'b': 'i'}

for i in sorted(l, key=lambda x: x['a']):
    print(i['b'])
```

### Korzystanie z zasobów internetowych - nie-JSON

Najczęstszymi danymi, na które się natkniemy, będą formaty XML (ustrukturyzowane dane)
i HTML (strony internetowe, niezupełnie niepodobne do XML).

Dobrą biblioteką do parsowania jednego i drugiego jest `lxml`.

```python
import requests
from lxml import etree

response = requests.get('http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0133%3Abook%3D1%3Acard%3D1')
root = etree.fromstring(response.content)
print(root)
print(root.tag)
print([c.tag for c in root])
print([c.tag for c in root[0]])
print([c.tag for c in root[0][0]])
print([c.tag for c in root[0][0][0]])
print(root[0][0][0][2].text)
```

```python
import requests
from lxml import html
response = requests.get('https://en.wikipedia.org/wiki/Douglas_Adams')
html_root = html.fromstring(response.content)

# dalej jw
print(html_root.tag)
```

Klika wskazówek:
1. XML warto otworzyć w przeglądarce -- dostaniemy znacznie lepszy ogląd
2. HTML w zasadzie trzeba otworzyć w przeglądarce; kod (to, co widzi Python) możemy zobaczyć za pomocą "narzędzi developerskich" (F12 w większości przeglądarek)
3. Wygodnym sposobem chodzenia po XML jest XPath ( https://en.wikipedia.org/wiki/XPath ), np. root.xpath('.//l')

```python
import requests
from lxml import etree

response = requests.get('http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0133%3Abook%3D1%3Acard%3D1')
root = etree.fromstring(response.content)

print(len([l for l in root.xpath('.//l')]))  # wszystkie węzły 'l'
print(len([t for t in root.xpath('.//text()')]))  # wszystkie węzły tekstowe

txt = ''.join(t for t in root.xpath('.//text()'))  # zgodnie z powyższym -- cały tekst we wczytanym xmlu
print(txt[:100] + '...')
```

Nieco wynurzeń o xpath i ogólnie sposobach dostępu do XML można znaleźć w pliku `xpath.py`.

#### Tagi HTML, które się w życiu przydają
(lista niewyczerpująca)
* `head` - nagłówek strony (metadane)
* `body` - ciało strony (część widoczna)
* `a` - hiperłącze (w węźle tekstowym treść linka, w atrybucie href adres, do którego prowadzi)
* `div`, `span` - "elementy" na stronie; ich sens często oddaje atrybut class lub id
* `ol`, `ul` - odpowiednio lista numerowana i nienumerowana
* `li` - element listy
* `table` - tabela
* `tr` - wiersz w tabeli
* `td`, `th` - odpowiednio "zwykła" i nagłówkowa komórka tabeli

> Ćwiczenie 8: Policz, ile jest węzłow milestone w pliku na stronie
 http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0133%3Abook%3D1%3Acard%3D1
