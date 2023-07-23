# Zapoznaj się z modułem random.
# Stwórz prostą grę zgadywankę.
# Komputer losuje wartość z przedziału od 1-30.
# Poproś użytkownika o zgadnięcie liczby.
# Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie.
#
# Zadanie 3
# Rozszerz grę z punktu powyżej. Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała


import random

a = random.randint(1,30)   #metoda randint zwraca liczbę z przedziału od 1 do 30 (obie obejmują)

while True:
    number_riddle = int(input("Zgadnij liczbę całkowitą z zakresu liczb od 1 do 30"))
    if a == number_riddle:
        print("Brawo, to ta liczba!")
        break
    else:
        print("Niestety, próbuj dalej")
        if number_riddle > a:
            print("Twoja liczba jest większa")
        else:
            print("Twoja liczba jest mniejsza")
            continue