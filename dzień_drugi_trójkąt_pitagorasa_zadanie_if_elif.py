#Poproś użytkownika o wpisanie długości boków trójkąta
def question_to_user(message):
    input_value = input(message)
    return float(input_value)


print('\nPodaj wymiary boku a, b oraz c.  \nNastąpi sprawdzenie o możliwości utworzenia trójkąta oraz \nokreślenie czy trójkąt jest trójkątem pitagorejskim lub egipskim.\n')
a = question_to_user('Podaj dlugosc boku a:')
b = question_to_user('Podaj dlugosc boku b:')
c = question_to_user('Podaj dlugosc boku c:')

#Sprawdź, czy da się ułożyć trójkąt o podanych długościach
# (najdłuższy bok powinien być krótszy niż suma dwóch pozostałych):
if (a>b and a>c and a<b+c) or (b>a and b>c and b<a+c) or (c>a and c>b and c<a+b):
   print('\nZ tych wymiarów istnieje możliwość stworzenia trójkąta.')
elif a == b == c:
    print('\nZ tych wymiarów istnieje możliwość stworzenia trójkąta równobocznego.')
else:
    print('\nZ tych wymiarów nie ma możliwości stworzenia trójkąta.')
    quit()

# Sprawdź, czy to trójkąt pitagorejski:
if a**2+b**2==c**2:
    print('Trójkąt o takich wymiarach boków to trójkat pitagorejski.')

    # Sprawdź, czy trójkąt pitagorejski jest trójkątem egipskim:
    if (a/3 == b/4 == c/5):
        print('Trójkąt o takich wymiarach boków to trójkat egipski.')
else:
    print('Boki o podanych wymiarach nie stworzą trójkat pitagorejskiego.')