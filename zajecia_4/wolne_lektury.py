import requests  # moduł requests nie jest wbudowany w instalację pythona, ale powinniśmy go byli zainstalować na zajeciach 2.

result = requests.get('https://wolnelektury.pl/media/book/txt/lalka-tom-pierwszy.txt')
print(result.status_code)  # 200 oznacza sukces, 4** oznacza błędny request (nasza wina), 5** oznacza błąd serwera (często nie nasza wina)
tekst = result.text

print(tekst[:100])
