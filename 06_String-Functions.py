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
###########################################################################################
# repetition operator (*) - powtarza string określoną liczbę razy

print("Hello " * 3) # powtarza string określoną liczbę razy

print("=" * 20)
# %%
###########################################################################
# extracting substrings
text = "Python"
print(text[0]) # indexowanie normalne (od 0)
print(text[-6]) # indexowanie od konca (od -1)

print(text[5]) #indexowanie normalne (od 0)
print(text[-1])

print(text[3])
print(text[-3])

# %%
###########################################################################
# slicing strings

date = "2023-06-01"

print(date[0:4]) # zwraca rok z date
print(date[:4]) # zwroci to samo co powyzej bo domyslnie python zaczyna od 0

print(date[5:7]) # zwraca miesiac z daty
print(date[8:]) # zwraca dzien z daty

print(date[-2:]) # zwraca dzien z daty

# %%
###########################################################################
# whitespace cleanup
#.lsrip() - usuwa biale znaki z lewej strony stringa
#.rstrip() - usuwa biale znaki z prawej strony stringa
#.strip() - usuwa biale znaki z obu stron stringa, chyba ze przekazemy
# parametr (przyklad nizej)

text = " Engineering".lstrip()
print(text)

text2 = "Engineering ".rstrip()
print(text2)

text = "  Engineering ".strip() 
print(text)

text = "Data Science".strip() # nie usuwa bialych znakow w srodku stringa
print(text)

text = "###Abc###".strip("#") # mozemy przekazac do tej metody znak
# kroty chcemy usunac

print(text)
# %%
##########################################################################
# use case for strip()

text = " Engineering"
print(len(text))
print(len(text.strip()))

text = text.strip() # jesli chcemy zmodyfikowac nasz string to musimy to
# tak zrobic poniewaz same wywolanie zwykle metody klasy string nie 
# zmienia go. Stringi w pythonie sa immutable.

nr_of_spaces = len(text) - len(text.strip())
is_data_clean = len(text) == len(text.strip())

print("Ilosc spacji:" ,nr_of_spaces)
print("Is data clean:", is_data_clean)

# %%
############################################################################
# Case Conversions
# lower() - zmienia text na lowercase
# upper() - zmienia text na uppercase

text = "python PROGRAMMING"

print(text.lower())
print(text.upper())

#Use case: searching

search = " Email"
data = "email "

print(search == data) # false bo stringi nie sa takie same

search = search.lower().strip()
data = data.lower().strip()

print(search == data) # true bo teraz te stringi sa takie same

# %%
#python task:

messy_string = "968-Maria, ( D@t@ Engineer ) ;; 27y   "
# wynik ma byc: name: Maria | role: data engineer | age: 27

messy_string = messy_string.strip().replace(";;","$")
messy_string = messy_string.replace("@","a").replace("-","").replace(",","")
messy_string = messy_string.replace(")","").replace("(","#")
messy_string = messy_string[2:].replace("y","").replace("8","name: ")
messy_string = messy_string.replace("#","| role:").replace("$","| age:")
messy_string = messy_string.replace("Data Engineer  ","Data Engineer ")

print(messy_string)


# %%
