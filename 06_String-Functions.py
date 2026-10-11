#--------------String Functions in Python-------------#

#String Functions Types:

# %%
####################################################################################
#str() - converts the specified value into a string

name = "Nico"
print(type(name))

age = 20
print(type(age))

print("Your Age is: " + str(age)) # tutaj musimy zamienic int na string bo nie mozemy
# laczyc stringa z int

age = age + 5
age = str(age) # tutaj zamieniamy int na string bo chcemy go polaczyc z innym 
#stringiem

print(type(age))
age = age + 5 # tu wyskoczy blad bo age jest juz stringiem i nie mozemy dodac do 
# niego inta

# %%
######################################################################################
# len() zwraca dlugosc obiektu, w tym przypadku stringa.

password = "12 3a678785"
print(len( password)) # len() zwraca dlugosc obiektu, w tym przypadku stringa. 
if len(password) < 8:
    print("Password is too short")

# %%
#######################################################################################
text = """
Pyhthon is easy to learn.
Python is powerful.
Many people love Python.
"""
text.count("Python") # count() zwraca liczbe wystapien danego znaku lub slowa w stringu
print(text.count("Python"))

### zwraca 2 bo python jest case-sensitive
# %%
#########################################################################################
# replace() - zamienia jeden znak na inny w stringu
price = "1234,56"
print(price)
print(price.replace(",", "."),"\n") # replace() zamienia jeden znak na inny w stringu

phone = "123-456-789"
print(phone.replace("-","/"))
print(phone.replace("-",""),"\n") ### mozna zamienic tez pustym stringiem

price2 = "$1,299.99"
print(price2.replace("$","").replace(",","")) # mozna laczyc replace() w jednej linii

# %%
#########################################################################################
# Python Task: Convert phone number
phone_number = "+49 (176) 123-4567"
print(
    phone_number.replace("+","").replace(" ","").replace("(","").replace("-","")
    .replace(")","")
      )
# %%
##########################################################################################
# Concatenation of Strings
first_name = "Nico"
last_name = "Scott"

full_name = first_name + " " + last_name # laczenie stringow
print(full_name)

folder = "C:/Users/Nico/"
file = "report.csv"

full_path = folder + file
print(full_path) 

# %%
###########################################################################################
# f-strings

name = "Nico"
age = 20
is_student = False

print(f"Name: {name}, Age: {age}, Is Student: {is_student}")
print(f"{{This is a string with curly braces}}") # aby wyswietlic {} trzeba je podwoic

# %%
###########################################################################################
# split() - dzieli string na liste elementow na podstawie separatora

stamp = "2023-06-01 12:34:56"
print(stamp.split(" ")) # dzieli string na liste elementow na podstawie separatora,
# w tym przypadku spacji

stamp2 = "2022-09-29"
print(stamp2.split("-"))

csv_file = "1234,Max,Usa,2023-06-01,M"
print(csv_file.split(","))
# %%
