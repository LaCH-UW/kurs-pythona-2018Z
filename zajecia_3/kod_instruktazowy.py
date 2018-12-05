import unicodedata


with open('dane/lalka-tom-drugi.txt', encoding='utf-8') as fp:
   tekst = fp.read()


def wersja_1(text, searched_word):
    count = 0
    for word in text.split():
        if word == searched_word:
            count += 1

    return count


def wersja_2(text):
    struct = []
    for word in text.split():
        struct.append(word)

    return struct


def wersja_3(text):
    struct = {}
    for word in text.split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct


def wersja_4(text):
    struct = {}
    for word in text.casefold().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct


def wersja_5(text):
    struct = {}
    for word in text.replace('.', '').replace('?', '').replace('!', '').replace('…', '').casefold().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct


def wersja_6(text):
    struct = {}
    for word in ''.join(c for c in text if unicodedata.category(c) != 'Po').upper().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct


def wersja_7(text):
    struct = {}
    for word in ''.join(c for c in text if not unicodedata.category(c).startswith('P')).upper().split():
        if word not in struct:
            struct[word] = 1
        else:
            struct[word] += 1
    return struct
