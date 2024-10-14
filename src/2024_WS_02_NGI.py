# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in October 2024
in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 2 on 9th October 2024
###########################

### control structures: conditional statements: if, elif, else, match cases,
### operators

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

air_temperature = 17  # [degrees]

if air_temperature > 30:
    print('do office work it is too hot')
    if air_temperature > 40:
        print('go to Norway')
elif air_temperature <= 5:
    print('do office work it is too cold')
elif air_temperature <= 10:
    print('rather do office work it might be too cold')
elif air_temperature == 18:
    print('today is the field day of the year!')
else:
    print('go out into the field')

# comparisons to Booleans (i.e. True, False) should be done with using "is" or
# "is not"
nice_temperature = True
if nice_temperature is True:
    print('go out into the field')
# in comparisons to booleans the "is True" can be skipped but this is bad for
# readability

# match-cases are a new alternative to check if a variables matches something
geotechnical_test = 'CPT'
match geotechnical_test:  # noqa
    case 'dynamical sounding':
        print('you are dealing with gravel')
    case 'CPT':
        print('you are dealing with fine grained sediment')

# to check if something is included in something else
# works for substrings in strings, or for elements on lists etc.
soil_types = ['gravel', 'sand', 'silt', 'cobble', 'clay']

if 'silt' in soil_types:
    print('there is silt in your soil types')
else:
    print('there is no silt')


### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore

STOP_CRITERION = 10

iterator = 0

while iterator < STOP_CRITERION:
    print(f'this is iteration number: {iterator}')
    # iterator = iterator + 1
    iterator += 1

print(f'now the loop is finished because the iterator = {iterator}')

# Exercise 5
fibonaccis = [0]

number = 1

while number < 200:
    fibonaccis.append(number)
    number = sum(fibonaccis[-2:])

print(fibonaccis)


# modified ChatGPT solution
limit = 200
fib_list = []
a, b = 0, 1
while a < limit:
    fib_list.append(a)
    a, b = b, a + b
print(fib_list)

# for loops are there to iterate over finite numbers of elements
soil_types = ['gravel', 'sand', 'cobble', 'clay', 'silt']
cohesions = [50, 66, 80, 45, 46, 47]  # [kPa]
friction_angles = [33, 30, 28, 34, 33]  # [degrees]

CORRECTION = 12

cohesions_corrected = []
for c in cohesions:
    cohesions_corrected.append(c + CORRECTION)
print(cohesions_corrected)

# to acces multiple values of the loop
for c, phi in zip(cohesions, friction_angles):
    print(f'the soil has a cohesion of: {c} kPa and a phi of {phi} deg.')

print('\n')

# if you expect errors / exceptions the can be specifically caught and avoided
for i in range(len(cohesions)):
    try:
        c = cohesions[i]
        phi = friction_angles[i]
        print(f'the soil has a cohesion of: {c} kPa and a phi of {phi} deg.')
    except IndexError:  # always specify error type
        print('\nERROR: one of the lists is shorter than the other!!!!')
        print(f'error occured after {i+1} iterations')
        pass

# enumerate() in a loop gives an iterator and whatever one iterates over
for i, soil in enumerate(soil_types):
    phi = friction_angles[i]
    print(f'this is a {soil} outcrop with a friction angle of {phi} degrees')


# Exercise 7
rock_list = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff',
             'quartzite',  'kaolin', 'phonolite', 'gneiss', 'sand',
             'diabase', 'black coal', 'slate', 'andesite', 'andesite',
             'gypsum and anhydrite', 'greywacke', 'suevite']

START_YEAR = 2007

years = list(range(START_YEAR, START_YEAR + len(rock_list)))

for i in range(len(rock_list)):
    print(f'the rock of the year {years[i]} was {rock_list[i]}')


# Exercise 6
STOP = 1000

numbers = []

for i in range(STOP):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
print(sum(numbers))

# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop.

print(sum([i for i in range(STOP) if i % 3 == 0 or i % 5 == 0]))


# Exercise 3 bonus:

empty_list = []

rock_types = ['marl', 'gneiss', 'limestone', 'eclogite']

# with for loop
for rock in ['marl', 'gneiss', 'limestone', 'eclogite']:
    empty_list.append(len(rock))
print(sum(empty_list[-3:]))

# with while loop
empty_list = []
iterator = 0
while iterator < len(rock_types):
    empty_list.append(len(rock_types[iterator]))
    iterator += 1
print(sum(empty_list[-3:]))

# with list comprehension
print(sum([len(rock) for rock in rock_types][-3:]))
