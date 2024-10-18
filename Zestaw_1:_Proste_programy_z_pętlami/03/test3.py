import unittest
import io
from contextlib import redirect_stdout

from exercise3 import Zadanie_3

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test3(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_3(2024)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ["19 11", "(19, 11)"]
        self.assertIn(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test3)
    unittest.TextTestRunner(verbosity=2).run(suite)
