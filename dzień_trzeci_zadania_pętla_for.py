#Zadanie 1
#Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
#Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

numbers = range(1,11)
for numer in numbers:
    print(sum(numbers[:numer]))

#Zadanie 3
#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem
# lub białym znakiem). Następnie powitaj każdą osobę na liście.

names=input("Podaj imiona oddzielone spacją: ")
names=names.title()
for name in names.split():
       print("Cześć "+name)

# Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
# – czy liczba jest wielokrotnością 3
# – czy liczba jest wielkorotnością 4
# – wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
# – wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony

liczba = int(input("Wprowadz liczbe "))

for i in range(1, liczba + 1):
    #sprawdza podzielność liczby przez 3 i 4
    if i % 3 == 0 and i % 4 == 0:
        print("Przetwarzanie liczby: ", i)
        print("Hurra, ta liczba dzieli sie przez 3 i 4", "\n")
    # sprawdza podzielność liczby przez 3
    elif i % 3 == 0:
        print("Przetwarzanie liczby: ", i)
        print("Teraz ta liczba jest wielokrotnoscia 3", "\n")
    # sprawdza podzielność liczby przez 4
    elif i % 4 == 0:
        print("Przetwarzanie liczby: ", i)
        print("Teraz ta liczba jest wielokrotnoscia 4", "\n")
    #jeśłi niespełnione warunki wyświetla gwiazdkę
    else:
        print("Przetwarzanie liczby: ", i, )
        print("*\n")