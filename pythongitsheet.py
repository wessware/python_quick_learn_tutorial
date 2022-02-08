"""
Learn python essentials in a 'few' lines of code
Comment out each separate section to run separate blocks

PART ONE 
Intrdouction to basic python! Variables & data structures
"""
from numpy import sort


print('Hello git')

# hello git with a variable
text = 'Hello git'

print(text)

# concatenation - combining strings
first_name = 'nikola'
last_name = 'tesla'
full_name = first_name + ' ' + last_name
print(full_name)

# python lists
cars = ['toyota', 'suzuki', 'nissan']

# fetch first item on the list
first_car = cars[0]

# fetch last item on the list
last_car = cars[-1]

# loop through the list
for car in cars:
    print(car)

# adding items on the list
germans = []  # creating an empty list
germans.append('BMW')
germans.append('VW')
germans.append('MB')
print(germans)

# making numerical lists
squares = []
for y in range(1, 15):
    squares.append(y**2)

print(squares)

# alternative squares list
squared = [x**2 for x in range(1, 16)]
print(squared)

# slicing through a list - list operations
fruits = ['papaya', 'guava', 'orange', 'banana', 'apple']
first_two = fruits[:2]  # get the first two entities on the list
fruits_copy = fruits[:]  # copy the entire list - with a different name
fruits_copy.append('mellon')

print(first_two, fruits_copy)

# Tuples - immutable lists - lists that cannot be modified!
years = (1986, 1990, 1993, 1996, 1998, 2002)
print(years)

# Conditional statements
"""
equals x == 4
not equal x !=4
greater than x > 4
greater than or equal to x >= 4
less than x < 4
less than or equal to x <= 4

conditional test on a list
'BMW' in germans
'vW' not in germans

Booleans values
git_guru = True
git_nov = False
"""

# if statement
age = 20
if age >= 18:
    print('You can go to jail!')

# if-else statements
if age < 4:
    bus_fare = 0
elif age < 18:
    bus_fare = 50
else:
    bus_fare = 100

if age < 4:
    print('takes a free ride')
elif age < 18:
    print('pays half price')
else:
    print('pays full price')

# python dictionaries
crockery = {'serve': 'spoon', 'fry': 'pan',
            'cook': 'pot', 'serve': 'laddle', 'hold': 'tong'}

# accessing a value on a dictionary
print('The serving crockery is ' + crockery['serve'])

crockery['drink'] = 'mug'  # adding a value to a list

print(crockery)
# looping through all key-value pairs
for name, use in crockery.items():
    print(name + ' is done using ' + use)

# looping through all keys
for name in crockery.keys():
    print(name + ' is a kitchen crockery use.')

# looping through all values
for name in crockery.values():
    print(name + ' is a crockery item.')

# python user input prompt
"""
name = input('What is your git username? ')  # string prompt
print('Welcome, ' + name + '!')

years_on = input('Years on GitHub? ')  # integer prompt
years_on = int(years_on)

constant = input('Your favorite mathematics constant? ')
constant = float(constant)
"""
# END OF PART ONE

# BEGINNING OF PART TWO

# while loops
num_num = 1
while num_num <= 3:
    print('less than five')
    num_num += 1

# user input while loops
"""
text = ''
while text != 'quit':
    text = input('What is your git username?')
    print(text)
"""
# python functions


def greet_user():  # python function to display a simple greeting message!

    print('Git says Hello!')


greet_user()
# passing arguments to a python function


def arg_greet(username):
    print('Hello, ' + username + '!')  # personalized greeting message!


arg_greet('Wessware')

# default value parameter functions in python


def prep_ugali(addition='boiled water'):
    print('Add some ' + addition + ' first before you begin!')


prep_ugali()
prep_ugali('maize flour')

# python functions that return a value


def val_add(x, y):
    return x + y


added = val_add(67, 86)
print(sum)

# Python classes - they define objects & object attributes


class Bull():

    def __init__(self, name):
        self.name = name

    def rest(self):
        print(self.name + ' is resting')


my_bull = Bull('samo')

print(my_bull.name + " is an awesome bull")
my_bull.rest()

#Inheritance in Python


class fight_bull(Bull):
    def __init__(self, name):
        super().__init__(name)

    def fight(self):
        print(self.name + " is winning this fight!")


my_bull = fight_bull('Korea')
print(my_bull.name + ' is a fighting bull')
my_bull.fight()
my_bull.rest()


# working with files in Python
file = 'git.txt'
with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

# writing to a file
filename = 'git.txt'
with open(filename, 'w') as file_object:
    file_object.write('GitHub also provides hosting services for users!')

# appending to a file
file_named = 'git.txt'
with open(filename, 'a') as file_object:
    file_object.write('\nGit is a great SCVS utility.')

# exceptions in Python - responding to errors that are likely to occur during execution
"""
prompt = 'How many eggs do you need?'
egg_num = input(prompt)

try:
    # ensures that the number provided is an integer, else returns an error.
    egg_num = int(egg_num)
except ValueError:
    print('Provide a valid number')
else:
    print('Your order is being processed!')
"""
# PYTHON LISTS - LISTS OPERATIONS & METHODS
# creating a list
languages = ['python', 'java', 'javascript', 'C', 'C++', 'matlab']

languages_1 = languages[0]  # getting the first element of the list
print(languages_1)
languages_end = languages[-1]  # getting the last element on the list
print(languages_end)
languages_3 = languages[2]  # getting the third or n-th element on the list
print(languages_3)

# changing a list element
languages[0] = 'brainfuck'
languages[-2] = 'python'
print(languages)

# adding elements to a list
languages.append('R')
print(languages)

# initializing an empty list
web_languages = []
web_languages.append('Bootstrap')
web_languages.append('React')
web_languages.append('Vue')
web_languages.append('nextJS')
print(web_languages)

# inserting an element at a particular position on the list
languages.insert(0, 'julia')
web_languages.insert(3, 'django')
print(languages, web_languages)

# removing elements from a list
del languages[-1]  # deleting by position
print(languages)

web_languages.remove('nextJS')  # deleting by value
print(web_languages)

# popping elements from a list - pop() gets the last item on the list
# although pop() can also be modified to fetch elements from any position on the list
newest_lang = languages.pop()
print(newest_lang)
firstweb_lang = web_languages.pop(0)  # popping the first item on a list
print(firstweb_lang)

# list length
lang_num = len(languages)
print('I have highlighted ' + str(lang_num) + ' programming languages.')

# sorting lists
print(languages)
languages.sort()
print(languages)

print(web_languages)
web_languages.sort(reverse=True)
print(web_languages)

print(sorted(languages))
print(sorted(web_languages, reverse=True))

# looping through a list
for language in languages:
    print(language)

for web_language in web_languages:
    print(web_language + " is good for web programming!")
print('A good combination of any is most suitable.')
