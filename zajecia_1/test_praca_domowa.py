import unittest

from zajecia_1.praca_domowa import (
    skracacz,
    madry_skracacz,
    palindromator,
)


class TestSkracacz(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(skracacz('akurat 10!'), 'akurat 10!...')

    def test_empty_string(self):
        self.assertEqual(skracacz(''), '...')

    def test_very_long(self):
        long_string = (
            'to jest niesłychanie długi napis, który powinien zostać'
            'skrócony do znacznie krótszego napisu'
        )
        shortened_string = 'to jest ni...'
        self.assertEqual(skracacz(long_string), shortened_string)


class TestMadrySkracacz(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(madry_skracacz(''), '')

    def test_too_short(self):
        self.assertEqual(madry_skracacz('akurat 10!'), 'akurat 10!')

    def test_not_too_short(self):
        long_string = (
            'to jest niesłychanie długi napis, który powinien zostać'
            'skrócony do znacznie krótszego napisu'
        )
        shortened_string = 'to jest ni...'
        self.assertEqual(madry_skracacz(long_string), shortened_string)


class TestPalindromator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(palindromator(1), 'b')

    def test_2(self):
        self.assertEqual(palindromator(2), 'bb')

    def test_5(self):
        self.assertEqual(palindromator(5), 'baaab')

    def test_42(self):
        self.assertEqual(
            palindromator(42), 'baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
        )


if __name__ == '__main__':
    unittest.main()
