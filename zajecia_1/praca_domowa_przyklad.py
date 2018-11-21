def skracacz(napis):
    return napis[:10] + '...'


def madry_skracacz(jakis_napis):
    skrocony_napis = jakis_napis[:10]
    if skrocony_napis == jakis_napis:
        return jakis_napis
    else:
        return skrocony_napis + '...'


def madry_skracacz_inaczej(napis):
    # funkcja len() sprawdza długość/liczbę elementów:
    # stringa, listy, zbioru, słownika etc.
    if len(napis) > 10:
        return napis[:10] + '...'
    else:
        return napis


def madry_skracacz_niemadrze(napis):
    dlugosc = 0
    for _ in napis:
        dlugosc += 1
    if dlugosc > 10:
        return napis[:10] + '...'
    else:
        return napis


def palindromator(dlugosc):
    if dlugosc == 0:
        return ''
    if dlugosc == 1:
        return 'b'

    return 'b' + (dlugosc - 2) * 'a' + 'b'
