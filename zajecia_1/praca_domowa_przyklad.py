
def skracacz(napis):
    return napis[:10] + '...'


def madry_skracacz(jakis_napis):
    skrocony_napis = jakis_napis[:10]
    if skrocony_napis == jakis_napis:
        return jakis_napis
    else:
        return skrocony_napis + '...'


def palindromator(dlugosc):
    if dlugosc == 0:
        return ''
    if dlugosc == 1:
        return 'b'

    return 'b' + (dlugosc - 2) * 'a' + 'b'
