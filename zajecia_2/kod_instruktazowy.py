import requests  # moduł requests nie jest wbudowany w instalację pythona!

result = requests.get('https://wolnelektury.pl/media/book/txt/lalka-tom-drugi.txt')
print(result.status_code)
# 200 oznacza sukces, 4** oznacza błędny request (nasza wina),
# 5** oznacza błąd serwera (często nie nasza wina)
tekst = result.text

print(tekst[:100])

# zapisuje w "lokalnym katalogu", czyli w tym, w kontekście którego działa nasz skrypt
# zob. niżej
with open('lalka-tom-pierwszy.txt', 'w', encoding='utf-8') as fp:
    fp.write(tekst)


zdanie = 'Tako rzecze Ithlinne, elfia wieszczka i uzdrowicielka: Drżyjcie, albowiem nadchodzi Niszczyciel Narodów.'
print(zdanie.upper())  # upper() zamienia napisy na wielkie litery
print(zdanie.lower())  # lower() zamienia napisy na małe litery
print(zdanie.title())  # title() zamienia napisy na pierwsze-słowo-z-wielkiej-litery
print(zdanie.capitalize())  # lower() zamienia napisy na małe litery
slowa = zdanie.split()  # prawie lista słów w tekście (split buduje listę dzieląc napis po białych znakach)
print(len(slowa))
print(slowa)

### liczenie słów

# wersja 'chcemy policzyć tylko jedno słowo'
def wersja_1(text, searched_word):
    count = 0
    for word in text.split():
        if word == searched_word:
            count += 1

    return count


print(wersja_1(tekst, 'dzień'))


# wersja naiwna
def wersja_2(text):
    struct = []
    for word in text.split():
        struct.append(word)

    return struct


dane_2 = wersja_2(tekst)
print(dane_2.count('dzień'))


# wersja dużo-lepsza: wyszukiwanie w słowniku jest szybsze
def wersja_3(text):
    struct = {}
    for word in text.split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct


dane_3 = wersja_3(tekst)
print(dane_3['dzień'])

### proste operacje na plikach
from pathlib import Path

# prawym przyciskiem myszy klikamy na nazwie projektu w oknie projektu
# i wybieramy "Copy path"
katalog_programu = '/home/piotr/LACH/python/kurs-pythona-2018Z'
obiekt_katalogu = Path(katalog_programu)

for file in obiekt_katalogu.iterdir():
    print(file, file.is_dir(), file.is_file())
    if file.name == 'nie_ma_takiego_pliku.py':
        file.rename('nowa_nazwa.py')
    elif file.name == 'takiego_tez_nie_ma.py':
        file.unlink()

new_file = Path('chcemy_miec_ten_plik.py')
with new_file.open('w', encoding='utf-8') as fp:
    fp.write('print("nowy plik!")')

