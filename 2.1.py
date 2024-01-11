print("Program sprawdza, czy liczby a, b i c tworzą liczbę pitagorejską.")
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a * a + b * b == c * c:
    print(f"Liczby {a}, {b} i {c} tworzą trójkę pitagorejską :)")
else:
    print(f"Niestety liczby {a}, {b} i {c} nie tworzą liczby pitagorejskiej ;( ")
