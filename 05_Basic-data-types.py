#----------------------Data types----------------------#

# %%
# Basic data types in Python:
a = 10 # integer (int)
b = 3.15 # float
c = "hello" # string (str)
d = 'hi' # string (str)
e = "1234" # string (str)
f = True # boolean (bool) --pierwsza litera musi byc duza
g = False # boolean (bool)
h = None # NoneType (None) --brak wartosci, pusty obiekt
i = "" # empty string (str) --nie NONE!
j = " " # string with space (str) --nie NONE!

# Typy danych z funkcjami wbudowanymi w Pythonie:
# %%
text = "hi"
number = 10

print(text)
print(number)

# %%
# type() zwraca typ zmiennej, pozwala nam to stwierdzic jakiego rodzaju to obiekt
# dziala dla kazdego typu obiekty w Pythonie, np. listy, slowniki, sety, tuple, itp.

print(type(text))
print(type(number))

# %%
# len() zwraca dlugosc obiektu, w tym przypadku stringa. Jest to funkcja

print(len(text))
#print(len(number)) # tu wyskoczy blad bo len() nie dziala na int

# %%
# upper() zwraca stringa w wersji z duzych liter. Jest to metoda klasy
# string, a nie zwykła funkcja

print(text.upper())
#print(number.upper()) # tu wyskoczy blad bo upper() nie dziala na int

# %%
# bit_length() zwraca liczbe bitow potrzebnych do zapisania liczby w systemie
# binarnym. Jest to metoda klasy int, a nie zwykła funkcja

print(number.bit_length())
#print(text.bit_length()) # tu wyskoczy blad bo bit_length() nie dziala na str

# %%
# python task: Data types

wiek = 20
wzrost = 178
imie = 'nico'
student_condition = True
pusta_zmienna = None

print(wiek)
print(type(wiek))
print(wiek.bit_length(),"\n")

print(wzrost)
print(type(wzrost))
print(wzrost.bit_length(),"\n")

print(imie)
print(type(imie))
print(len(imie),"\n")

print(student_condition)
print(type(student_condition))
print(student_condition.bit_length(),"\n")

print(pusta_zmienna)
print(type(pusta_zmienna))
#print(pusta_zmienna.bit_lenght) # to nie zadziala


# %%
# Teoria:
#1. Kazda wartosc ma tyh danych
#2. Python automatycznie rozpoznaje typy danych
#3. Typy danych są dynamiczne! tj. moga sie zmieniac
#4. Kategorie typow:
#   -- No Value: NoneType.
#   -- Single Value: int, str, bool, float, complex
#   -- Multiple Values: set, tuple, dict, list
#5. Wartosci sa obiektami klasy danego typu danych!
