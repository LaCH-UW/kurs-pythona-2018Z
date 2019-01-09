# Wizualizacja danych: 9 stycznia (środa) 16.30-19.30


### Podstawowe wykresy
"Domyślna" biblioteka do wykresów w pythonie to `matplotlib`. Pozwala w miarę prosto robić w miarę proste wykresy - 
które możemy potem mniej prosto upiększać.

#### Wykres liniowy, line chart (`wykres_liniowy.py`)

```python
from matplotlib import pyplot as plt  # "import as" pozwala odwoływać się do zaimportowanej biblioteki przez inną nazwę

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
plt.plot(data, linewidth=2)

plt.xticks(range(len(names)), names, rotation=90)
plt.xlabel("Próbki")
plt.ylabel("Liczba wystąpień")

plt.show()
# wykres możemy też zapisać do pliku (format jest autorozpoznawany po rozszerzeniu)
plt.savefig('out.png')
```

#### Wykres słupkowy, bar chart (`wykres_slupkowy.py`)

```python
from matplotlib import pyplot as plt

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
for idx, value in enumerate(data):
    plt.bar(idx, value)

plt.xticks(range(len(names)), names, rotation=90)
plt.xlabel("Próbki")
plt.ylabel("Liczba wystąpień")

plt.show()
```

#### Wykres kołowy, pie chart (`wykres_kolowy.py`)

```python
from matplotlib import pyplot as plt

plt.rcdefaults()
plt.clf()

data = [2, 1, 1, 1, 59, 1, 27, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

plt.title("Liczba wystąpień słów")
plt.pie(data, labels=names)
plt.axis('equal')

plt.show()
```

### Wykresy inaczej
Alternatywną biblioteką jest `plotly`. Jest zaprojektowana jako bardziej "sexi" i domyślnie tworzy bardziej 
interaktywne wykresy. Minus: nie są to obrazki (które możemy sobie wstawić do dokumentu, czy gdziekolwiek) tylko
fragmenty stron internetowych i skrypty (do publikowania w internecie).

Poniżej prosty wykres słupkowy (`plotly_slupkowy.py`).

```python
import plotly.offline as py
import plotly.graph_objs as go

data = [2, 1, 1, 1, 207, 1, 59, 16, 3, 6]
names = ['Bolesław', 'Prus', 'Lalka', 'Tom', 'I', 'I.', 'Jak', 'wygląda', 'firma', 'J.']

bars = []
for d, n in zip(data, names):
    bars.append(go.Bar(
        x=[n],
        y=[d],
        width=0.5,
        opacity=0.7,
        name=n,
    ))

fig = go.Figure(data=bars)

py.plot(fig)
```

### Podstawy podstaw map
`Plotly` pozwala też na proste zaznaczanie punktów na mapie - należy tylko pamiętać o tym, że jest 
to funkcja niejako "przy okazji" biblioteki do wykresów (przykład: `plotly_mapka.py`.

```python
import plotly.offline as py
import plotly.graph_objs as go

points = [
    ('Kraków',   (50.06465, 19.94498)),
    ('Warszawa', (52.22967, 21.01223)),
    ('Gdańsk',   (54.35202, 18.64664)),
]

data = []
for name, coords in points:
    data.append(go.Scattergeo(
        lon=[coords[1]],
        lat=[coords[0]],
        text='Niezwykle ważne miasto',
        marker=dict(
            size=15,
        ),
        name=name,
    ))

layout = go.Layout(
    title='Miasta w Polsce',
    geo=dict(
        resolution=50,
        projection=dict(type='mercator'),
        showland=True,
        showcountries=True,
        lonaxis=dict(range=[13, 25]),
        lataxis=dict(range=[48, 56]),
    ),
)

fig = go.Figure(layout=layout, data=data)

py.plot(fig)
```

### Wspomnienie o bardziej mapach
Biblioteką dedykowaną do map jest np. `folium` (pythonowy wrapper dla znanej javascriptowej biblioteki `leaflet`).
Garść przykładów użycia (uwaga: zakładają użycie jupytera, ale poza różnicą w wyświetlaniu zadziała też w Pycharmie): 
<https://python-visualization.github.io/folium/docs-v0.6.0/quickstart.html#Getting-Started>

Prosty przykład z działającym "u nas" wyświetlaniem (`folium_miniprzyklad.py`):

```python
import folium
import webbrowser

m = folium.Map(location=[52.2117514, 20.9864695], zoom_start=17)

folium.Marker([52.211937, 20.984562], popup='Tu jesteśmy').add_to(m)

# Zapis do pliku:
m.save('folium.html')
# folium nie ma opcji "podglądu" używalnej w PyCharmie, więc możemy otworzyć zapisany plik:
webbrowser.open('folium.html')
```

### Korzystanie z zasobów HTML

#### Tagi HTML, które się w życiu przydają (przypomnienie)
* `head` - nagłówek strony (metadane)
* `body` - ciało strony (część widoczna)
* `a` - hiperłącze (w węźle tekstowym treść linka, w atrybucie href adres, do którego prowadzi)
* `div`, `span` - "elementy" na stronie; ich sens często oddaje atrybut class lub id
* `ol`, `ul` - odpowiednio lista numerowana i nienumerowana
* `li` - element listy
* `table` - tabela
* `tr` - wiersz w tabeli
* `td`, `th` - odpowiednio "zwykła" i nagłówkowa komórka tabeli

> Ćwiczenie 1: Policz, ile jest wierszy w tabelkach
na stronie https://en.wikipedia.org/wiki/List_of_Roman_hoards_in_Great_Britain

> Ćwiczenie 2: Policz, ile rzymskich skarbów zostało znalezionych w Wielkiej Brytanii
i powiedz czemu to inne ćwiczenie niż 1.

> Ćwiczenie 3: Policz, ile spośród skarbów jest przechowywanych w Londynie

> Ćwiczenie 4: Zbuduj słownik: nazwa miejsca przechowywania skarbu (klucz) na liczbę skarbów przechowywanych 
w tym miejscu (wartość)

> Ćwiczenie 5: Zrób wykres słupkowy w `matplotlib` w oparciu o słownik z ćwiczenia 4

> Ćwiczenie 6: Zrób wykres słupkowy z ćwiczenia 5 w `plotly`

> Ćwiczenie 7: Utwórz listę nazw skarbów, lat ich odkrycia i współrzędnych geograficznych odkrycia.
(Weź pod uwagę tylko te skarby, dla których Wikipedia zna te współrzędne)

> Ćwiczenie 8: Tak, zaznacz na mapie dane z ćwiczenia 7

### Dziękuję bardzo.
