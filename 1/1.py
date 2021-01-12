1 # liczby
"napis" # lancuchy znaków (napisy)

# x 
# *2
# *4
# -10

komunikat1 = 'Jak masz na imię?'
komunikat2 = 'Ile masz lat?'

print(komunikat1)

imie = input()

print(komunikat2)

wiek = input()

print('Masz na imie ' + imie + '.' + ' Twój wiek to ' + wiek + '.')

if int(wiek) > 18:
    print('Jesteś pełnoletni.')
elif int(wiek) == 10:
    print('Masz 10 lat.')
else:
    print('Jesteś niepełnoletni.')


