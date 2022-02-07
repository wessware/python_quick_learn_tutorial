"""
Learn python essentials in a 'few' lines of code
Comment out each separate section to run separate blocks
"""
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
name = input('What is your git username? ')  # string prompt
print('Welcome, ' + name + '!')

years_on = input('Years on GitHub? ')  # integer prompt
years_on = int(years_on)

constant = input('Your favorite mathematics constant? ')
constant = float(constant)
