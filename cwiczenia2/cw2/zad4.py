"""
kazdy z kazdym pojemnik polaczony rurami, pojemnik to prostokat reprezentowany przez 2 punkty (topleft , bottomright)
do pojemnikow nalano A powierzchni wody, znajdz wypelniony pojemnik

-> nie obchodzi nas gdzie pojemnik sie znjaduje tylko na jakiej wysokosci sie zaczyna i konczy i jaka ma pojemnosc

jakis leetcode bylo cos takiego?

@ sposob to jakies "zamiatanie"
1. sort po gornej krawedzi (z pamietamiem co to za pojemnik)
2. sort po dolnej krawedzi -||-

kiedy zaczelo sie pudelko dodajemy szeroksc pudelka aby miec szerokosc wody
jesli napotykamy na gore to pudelko zostalo zapenione

#mozna binsearchowac wysokosc i sprwadzac empirczie
"""

from random import randint

for n in range(20):
    a = randint(0, 100)
    op = "z"
    b = randint(0, 100)
    print(f"{a}% {op} {b}")

def main():
    print("Hello World!")
    a: str = input("Podaj pierwsza liczbe:")
    b: str = input("Podaj pierwsza liczbe:")
    a = int(a)
    b = int(b)
    print(f"Suma wynosi: {a+b}")
    print(f"Srednia wynosi: {(a+b)/2}")


def calculator_main():
    print("CALCULATOR wyjdz z wpisujac :quit")
    while True:
        a: str = input(">>> ")
        if a == ":quit":
            break
        try:
            res = eval(a)
            print(f"= {res}")
        except Exception as e:
            print(f"Podano zle dane!")

calculator_main()