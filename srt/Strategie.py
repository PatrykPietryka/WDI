import os
import sys

# Dodaj wszystkie podfoldery po za komendy do sys.path
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    if "Komendy" != root:
        sys.path.append(root)

# Liczba plików tworzonych na podstawie strategii zależy od liczby zwracanych klas.
# Jeśli użyjemy strategii zwracającej 1 klasę, zostanie stworzony 1 plik.
# Możemy jednak opracować strategię zwracającą 10 klas, co pozwoli na stworzenie 10 plików zadania.
# Pliki będą miały nazwy odpowiadające nazwom folderów, z których pochodzą.
# Na przykład, jeśli w przyszłości planujemy dodać plik z wyjaśnieniami autora zadania
# lub innymi informacjami, wystarczy stworzyć dodatkowy folder z nazwą, jaką chcemy nadać plikowi,
# oraz dodać klasę dziedziczącą po bazowej, która zapisze te treści.


def testy_domyslne():
    "Aktualizowana najlepsza strategia testow"
    from Testy.Prime import Prime

    return Prime


def szablon_domyslny():
    "Aktualizowana najlepsza strategia Szablonow"
    from Szablon.input_main import input_main

    return input_main


def rozwiazania_domyslne():
    "Aktualizowana najlepsza strategia rozwiazania"
    from Rozwiazanie.importless import importless

    return importless


def domyslna():
    """Zwraca domyslna wartości dla strategii czyli akutalizowna najlepsza strategie szablonów,rozwiązań i testów."""
    return (szablon_domyslny(), rozwiazania_domyslne(), testy_domyslne())


def meritum():
    "sama funkcja w rozwiązaniu"
    from Rozwiazanie.meritum import meritum

    return szablon_domyslny(), meritum, testy_domyslne()
