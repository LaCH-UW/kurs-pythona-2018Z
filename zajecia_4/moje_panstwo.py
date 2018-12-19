import json
import time

import requests


r = requests.get('https://api-v3.mojepanstwo.pl/dane/krs_formy_prawne.json')
json_data = r.json()

# co tu w ogóle jest?
print(json_data.keys())

# liczba elementów
print(json_data['Count'])
# najważniejszy klucz -- lista danych!
print(json_data['Dataobject'])

# ponieważ to API, możemy się spodziewać, że wszystkie elementy na liście mają taką samą
#  strukturę -- i możemy zbadać "pierwszy z brzegu" obiekt
first = json_data['Dataobject'][0]
print(first)
print(first.keys())

print(first['id'])
print(first['data'])
print(first['data'].keys())
print(first['data']['krs_formy_prawne.nazwa'])

# i wiemy, gdzie szukać nazwy; zatem nasz docelowy skrypt to:
for i in json_data['Dataobject']:
    if i['data']['krs_formy_prawne.nazwa'] == 'KÓŁKO ROLNICZE':
        print(i['id'], i['data']['krs_formy_prawne.nazwa'])
        break



id_kolka_rolniczego = 5
lista_kolek_rolniczych_po_500 = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}&limit=500'.format(id_kolka_rolniczego)


def get_one_page(url):
    r = requests.get(url)
    json_data = r.json()
    return json_data


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


#j = get_one_page(lista_kolek_rolniczych_po_500.format(id_kolka_rolniczego))
#dump_all_pages(lista_kolek_rolniczych_po_500.format(id_kolka_rolniczego), 'kolka_rolnicze.json')
