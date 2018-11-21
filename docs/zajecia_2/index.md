# Git i GitHub w kodowaniu: 21 listopada (środa) 16.30-19.30

### Co to jest (i po co jest) Git?

> System kontroli wersji śledzi wszystkie zmiany dokonywane na pliku
> (lub plikach) i umożliwia przywołanie dowolnej wcześniejszej wersji.
> (...). Pozwala on przywrócić plik(i) do wcześniejszej wersji, odtworzyć
> stan całego projektu, porównać wprowadzone zmiany, dowiedzieć się kto jako
> ostatnio zmodyfikował część projektu powodującą problemy, kto i kiedy
> wprowadził daną modyfikację. Oprócz tego używanie VCS oznacza, że nawet
> jeśli popełnisz błąd lub stracisz część danych, naprawa i odzyskanie ich
> powinno być łatwe. Co więcej, wszystko to można uzyskać całkiem niewielkim
> kosztem.  ([Git Pro](https://git-scm.com/book/pl/v2/Pierwsze-kroki-Wprowadzenie-do-kontroli-wersji))

Git jest rozproszonym systemem kontroli wersji (Distributed Version Control System),
co oznacza, że kopie projektu objętego kontrolą VCS (określanego mianem "repozytorium")
mogą być przechowywane w kilku miejscach jednocześnie, a narzędzia wbudowane
w Gita umożliwiają wygodne synchronizowanie danych w tych lokalizacjach.

### Co to jest (i po co jest) GitHub?

Zwykle pracując z Gitem chcemy mieć lokalne repozytorium u siebie
na komputerze (tam wprowadzamy zmiany), ale także zdalne repozytorium na jakimś
serwerze - w nim dane są:
* dostępne dla ew. naszych innych komputerów
* dostępne dla naszych współpracowników
* zabezpieczone przez zaginięciem/zepsuciem naszego komputera zawierającego
  lokalne repozytorium

GitHub to organizacja, która umożliwia utrzymywanie zdalnych repozytoriów
Gita (i umila to wieloma towarzyszącymi narzędziami).

### Konfiguracja lokalnego repozytorium

W tej chwili wszyscy mamy na dyskach lokalne repozytoria Gita zawierające
dane do pracy na zajęciach. Ponieważ uzyskaliśmy je za pomocą klonowania (`clone`)
zdalnego repozytorium, Git automatycznie zachował metadane dotyczące tegoż
zdalnego (`remote`) repozytorium. Tradycyjnie zdalne repozytorium, z którego
sklonowano projekt nosi nazwę `origin`. Zajrzyjmy teraz do `VCS->Git->Remotes...`
i zobaczmy, że jest tam `origin` wskazujące na adres repozytorium, które
sklonowaliśmy.

To repozytorium jest Państwa prywatną "własnością" i w ciągu tego kursu to Wy
będziecie je modyfikować. Chcemy jednak mieć możliwość dociągania kolejnych
materiałów, które będą pojawiać się z zajęć na zajęcia. W tym celu dodamy
drugie repozytorium zdalne.

1. Wchodzimy ponownie w `VCS->Git->Remotes...` i klikamy ikonkę plusa.
2. W `name` wpisujemy `upstream` (żebyśmy wszyscy mieli to samo).
3. W `URL` wpisujemy `https://github.com/LaCH-UW/kurs-pythona-2018Z`
(na górze [strony kursu](https://lach-uw.github.io/kurs-pythona-2018Z/) jest
przycisk "View on GitHub" - interesuje na adres strony, na której lądujemy
po kliknięciu na niego).
4. Klikamy `OK` i ponownie `OK` (potwierdziwszy, że faktycznie mamy na liście
dwa repozytoria zdalne).

Teraz możemy zaciągać nowe materiały (i ew. zmiany w istniejących) z `upstream`
oraz zapisywać nasze zmiany (w tym prace domowe) do `origin`.

#### Zaciąganie zmian

Zmiany można synchronizować w dwie strony - możemy zaciągać zmiany ze zdalnego
repozytorium (`pull`) lub wypychać tam nasze lokalne zmiany (`push`). Zaczniemy
od tego pierwszego:

1. `VCS->Git->Pull...`
2. W `Remote` wybieramy `upstream` i klikamy na ikonkę strzałek obok (PyCharm
zaciągnie sobie informacje o strukturze zdalnego repozytorium).
3. W `Branches to merge` zaznaczamy `upstream/master` i klikamy `Pull`.

Powinniśmy zobaczyć w widoku projektu, że np. pojawił się katalog `zajecia_2`,
a w `zajecia_1` pojawiły się pliki `praca_domowa_przyklad.py`
i `test_praca_domowa.py`.

Jeśli kiedyś będziemy chcieli pracować nad naszym repozytorium na dwóch
komputerach, analogicznie zaciągamy zmiany z `origin/master`. Uwaga: unikajmy
w miarę możliwości równoległego nanoszenia podobnych (i.e. w tych samych
miejscach tych samych plików) zmian. Prowadzi to tzw. konfliktów. Git oczywiście
posiada narzędzia do ich rozwiązywania (a PyCharm jeszcze je wzbogaca), ale
w ogólnym przypadku może to być kłopotliwe i pracochłonne.

#### Zapisywanie i wypychanie zmian

Pliki, które w naszym lokalnym repozytorium są zmienione, są tylko lokalnie
zmienione (mówimy wówczas, że repozytorium jest "brudne" (`dirty`)).
Żeby te zmiany zachować, musimy je explicite zacommitować (`commit`) - commity
dzielą historię edycji w repozytorium na dyskretne fragmenty. Z każdym commitem
powiązany jest opis (tzw. `commit message`), który powinien podsumowywać
różnice, jakie w repozytorium zaszły między nim a poprzednim commitem.

W widoku projektu nazwy zmodyfikowanych plików mają kolor niebieski. Klikając
na niego prawym przyciskiem myszy i wybierając
`Git->Compare with the Same Repository Version` możemy zobaczyć, na czym
polegają te zmiany (oglądamy w tej sposób tzw. `diff`). Wybierając z kolei
`Git->Revert` (`Ctrl+Alt+Z`) możemy przywrócić plik do postaci z ostatniego
commita (uwaga: stracimy bezpowrotnie nasze zmiany!).

Pliki nowe (nieobecne w poprzednim commicie) mają kolor zielony (jeśli
zaplanowaliśmy dodanie ich do najbliższego commita) lub brązowy (? jeśli nie).
Możemy zmienić kolor pliku z brązowego na zielony klikając na niego prawym
przyciskiem myszy i wybierając `Git->Add` (lub skrótem `Ctrl+Alt+A`).
Jeśli chcemy zmienić kolor z zielonego na brązowy, wybieramy `Git->Revert`
(plik pozostanie na dysku - chyba, że zaznaczymy opcję
`Delete local copies of added files`).

Commitujemy zmiany za pomocą opcji `VCS->Commit...` (`Ctrl+K`). Powoduje
to otwarcie menu, w którym:
* możemy zaznaczyć pliki, których zmiany mają być częścią commita
* oglądamy diffa, żeby upewnić się, że nie commitujemy czegoś, czego nie chcemy
* wpisujemy commit message
* zaznaczamy ew. inne opcje (poza zakresem niniejszego kursu)

Uwaga: wykonany commit modyfikuje historię naszego lokalnego repozytorium.
Jeśli chcemy ten commit (lub commity) dodać do historii naszego zdalnego
repozytorium (`origin`), musimy zrobić to za pomocą oddzielnej komendy `push`
(`VCS->Git->Push`, `Ctrl+Shift+K`). Czasem chcemy zrobić commit i od razu push -
PyCharm umożliwia to za pomocą strzałki rozwijającej opcje w przycisku `Commit`
na ekranie commitowania.

### O pracy domowej

W pliku `zajecia_1/praca_domowa_przyklad.py` znajdują się przykładowe
rozwiązania zadań z pracy domowej. Omówimy je sobie pokrótce. 

#### Testy

W pliku `zajecia_1/test_praca_domowa.py` znajdują się testy. Testy to zbiór
funkcji, które korzystają z modułu/biblioteki w przewidywalny sposób
i weryfikują, czy otrzymują wyniki zgodne z przewidywaniami. Do pisania
testów można np. użyć (standardowej) biblioteki `unittest`.

Z praktycznego punktu widzenia: oczekujcie Państwo, że biblioteka, którą
znajdziecie "na internecie", zawiera testy (łatwo to często sprawdzić,
bo dużo opensource'owych bibiliotek udostępnia źródła na GitHubie).
W przeciwnym razie jej twórca jest prawdopodobnie leniem i/lub niechlujem,
a biblioteka może nie działać "bo tak".


### Kodowanie na dziś - prosta praca z plikami i równie proste pobieranie
### z internetu

Jak poprzednio, popatrzmy na `kod_instruktazowy.py` (tym razem w katalogu
`zajecia_2`).

Polecenie `get()` z modułu `requests` pozwala na wykonywanie requestu
`HTTP GET` (i w efekcie zaciąganie plików udostępnionych jako
"strony internetowe".

```python
import requests

result = requests.get('https://wolnelektury.pl/media/book/txt/lalka-tom-drugi.txt')
print(result.status_code)
tekst = result.text

print(tekst[:100])
```

#### Instalowanie bibliotek

Biblioteka `requests` jest naszą pierwszą niewbudowaną biblioteką. W domyślnej
instalacji Pythona jej nie będzie, a PyCharm podkreśli jej nazwą na czerwono
(wężykiem).

Wiele popularnych bibliotek Pythona (i tych mniej popularnych też)
znajduje się w centralnym repozytorium bibliotek PyPI i można je stamtąd
instalować mniej więcej automatycznie. W PyCharmie klikamy na słowo `requests`,
a potem kliknąwszy na żarówkę wybieramy `Install package requests`
(alternatywnie: mając kursor klawiatury na `requests` naciskamy `Alt+Enter`
i tam wybieramy `Install...`). Dla zainterowanych: bez PyCharma użylibyśmy
polecenia `pip install requests`.

#### O wyniku działania

`status_code` to trzycyfrowa liczba opisująca jakoś "jak nam poszło". W
telegraficznym skrócie: 200 oznacza sukces, 4** oznacza błędny request
(nasza wina), 5** oznacza błąd serwera (często nie nasza wina). Dla chętnych:
[Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

Jeśli `status_code` jest równy 200, możemy spodziewać się, że wynik requestu
(obiekt zwracany przez `requests.get()`) ma atrybut text, który zawiera
"ciało" wyniku (i.e. to, co byłoby na stronie).

#### Operacje plikowe

Za pomocą polecenia `with open(<scieżka-do-pliku>, <tryb>) as wskaznik:`
możemy znaleźć się w kontekście otwartego pliku, pod zmienną `wskaznik`
mając wskaźnik do pliku. Jeśli otwieramy plik do odczytu (`tryb == 'r'`),
wskaźnik ma metodę `read`; jeśli do zapisu, to `write` (`tryb == 'w'`;
UWAGA: otwarcie pliku w trybie zapisu go wyczyści; możemy dopisywać coś
do pliku otwarłszy go do "dopisywania" (`'a'`)).

Dodatkowo możemy podać opcjonalny parametr `encoding`, który określi kodowanie
pliku, który czytamy/zapisujemy. Co do zasady, "dobrym" kodowanie jest `utf-8`.

Spróbujmy teraz zapisać tekst pierwszego tomu Lalki do pliku
`zajecia_2/lalka_tom_1.txt`.

```python
with open('lalka-tom-pierwszy.txt', 'w', encoding='utf-8') as fp:
    fp.write(tekst)
```

Teraz możemy wczytać z powrotem nasz tekst na zmienną. Zróbmy to.

> Ćwiczenie 1: Sprawdź ile znaków jest w pierwszym tomie Lalki

### Dwa słowa o operowaniu na stringach

```python
zdanie = 'Tako rzecze Ithlinne, elfia wieszczka i uzdrowicielka: Drżyjcie, albowiem nadchodzi Niszczyciel Narodów.'
print(zdanie.upper())  # upper() zamienia napisy na wielkie litery
print(zdanie.lower())  # lower() zamienia napisy na małe litery
print(zdanie.capitalize())  # capitalize() zamienia napisy na pierwsze-słowo-z-wielkiej-litery
print(zdanie.title())  # title() zamienia napisy na Każde Słowo z Wielkiej Litery
slowa = zdanie.split()  # prawie lista słów w tekście (split buduje listę dzieląc napis po białych znakach)
print(len(slowa))
print(slowa)
```

#### Jak liczyć wystąpienia słowa w tekście?

Przykłady rozwiązań w kodzie instruktażowym. Na następnych zajęciach użyjemy
do tego biblioteki.

### Proste operacje na plikach

Bardzo pomocna w operowaniu na plikach jest biblioteka standardowa `pathlib`.

Głównym obiektem w tej bibliotece jest `Path`, który inicjujemy ścieżką
do pliku lub katalogu. Taki "opakowany" obiekt ma garść przydatnych metod
(dla chętnych i zainteresowanych:
[dokumentacja](https://docs.python.org/3/library/pathlib.html)):

`sciezka = pathlib.Path('.')` (kropka to "katalog bieżący", cokolwiek to znaczy)

* `sciezka.exists()` - `True` jeśli istnieje obiekt z tą ścieżką
* `sciezka.mkdir()` - założy katalog w danej ścieżce
* `sciezka.is_file()` -  `True` dla plików, `False` dla katalogów
* `sciezka.is_dir()` - `True` dla katalogów, `False` dla plików
* `sciezka.iterdir()` - lista elementów w katalogu; dla pliku nie zadziała
* `str(sciezka)` - mapowanie na stringa - pełna ścieżka
* `sciezka.name` - sama nazwa pliku/katalogu
* `sciezka.suffix` - rozszerzenie pliku (np. `.py`)
* `sciezka.parent` - katalog, którym znajduje się `sciezka`
* `sciezka.rename("nowa_nazwa.txt")` - przenazywa plik
* `sciezka.unlink()` - (!) kasuje plik
* `sciezka.rmdir()` - kasuje katalog, jeśli jest pusty
* `sciezka.open()` - alternatywa dla funkcji `open()`; przyjmuje też tryb
i kodowanie, nadaje się do używania w `with`

### Praca domowa

1. Zacommituj i wypushuj plik `zajecia_1/praca_domowa.py` taki, żeby testy
w `zajecia_1/test_praca_domowa.py` przechodziły.

2. ~~Współczynnk bogactwa leksykalnego tekstu to stosunek liczby różnych słów~~
~~w tekście do łącznej liczby słów w tekście.~~
~~W pliku `zajecia_2/praca_domowa.py` napisz funkcję `oblicz_bogactwo(sciezka_pliku)`,~~
~~która policzy współczynnik bogactwa leksykalnego dla tekstu zawartego w pliku~~
~~o podanej w parametrze nazwie. Przetestuj ją na pierwszy tomie Lalki~~

3. W pliku `zajecia_2/praca_domowa.py` napisz funkcję `wieloplik(katalog, liczba)`,
który w (istniejącym) katalogu założy "liczba" plików (=tyle, jaka liczba będzie
w drugim parametrze) o nazwach `1.txt`, `2.txt`, `3.txt` etc. i do każdego
z nim wpisze napisz "To jest plik nr `<tutaj numer>`".

Pracę domową proszę wypushować do swojego repozytorium do 23:59 2018-12-02.