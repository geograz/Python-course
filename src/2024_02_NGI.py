# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in May 2024 in
4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 2 on 8th May 2024
###########################

# Exercise 4

rock_list = ['gneiss', 'marl', 'limestone']
rock_tuple = ('gneiss', 'marl', 'limestone')

print(rock_list[:2])
print(rock_tuple[:2])

rock_list.append('greenschist')
# rock_tuple.append('greenschist')

rock_list[1] = 'dolomite'
# rock_tuple[1] = 'dolomite'

### control structures: conditional statements: if, elif, else, match cases,
### operators

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

rock_1_ucs = 190  # [MPa]
rock_2_ucs = 200  # [MPa]

# == ... equal to
print(rock_1_ucs == rock_2_ucs)
# != ... not equal to
print(rock_1_ucs != rock_2_ucs)
# > or < ... greater or smaller than
print(rock_1_ucs > rock_2_ucs)
print(rock_1_ucs < rock_2_ucs)
# >= or <= ... greater than or equal or smaller than or equal
print(rock_1_ucs >= rock_2_ucs)
print(rock_1_ucs <= rock_2_ucs)

# these operators can be used in logical statements
rock_type = 'limestone'
if rock_type == 'granite':
    print('the rock is a granite')
elif rock_type == 'gneiss':
    print('the rock is a gneiss')
elif rock_type == 'greenschist':
    print('the rock is a greenschist')
else:
    print('the rock is something else')

# match-cases are a new alternative to check if a variables matches something
match rock_type:
    case 'granite':
        print('the rock is a granite')
    case 'gneiss':
        print('the rock is a gneiss')
    case 'limestone':
        print('the rock is a limestone')


# comparisons to Booleans (i.e. True, False) should be done with using "is" or
# "is not"
good_weather = True
if good_weather is True:
    print('get a haircut')
# in comparisons to booleans the "is True" can be skipped but this is bad for
# readability



### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore
a = 1

while a < 10:
    print(f'a is {a} and is smaller than 10')
    a += 1  # this is equivalent to: a = a + 1

print(f'after the loop, a is {a}')

# Exercise 5
MAX = 2000000  # the maximum limit of the fibonacci series that I want

fibonaccis = [0]

number = 1


while number < MAX:
    fibonaccis.append(number)
    number = fibonaccis[-1] + fibonaccis[-2]

print(fibonaccis)

# a while loop can be used to iterate over a finite list like this
soil_types = ['gravel', 'clay', 'sandy gravel', 'cobbles']
print(soil_types)

index = 0

while index < len(soil_types):
    soil_types[index] = 'silty ' + soil_types[index]
    index += 1

print(soil_types)

# a better solution is however to use a for loop which is always finite
soil_types = ['gravel', 'clay', 'sandy gravel', 'cobbles', 'silt']
friction_angles = [37, 20, 35, 38, 25]
cohesions = [0, 20, 0, 0, 5]

# for i in range(len(...)): is a typical construction to get an index
for i in range(len(soil_types)):
    print(f'the {soil_types[i]} has a friction angle of {friction_angles[i]} degrees')

# alternatively the enumerate() function can be used to get an element + index
for i, soil_type in enumerate(soil_types):
    print(f'{soil_type}:c: {cohesions[i]}, phi: {friction_angles[i]}')

# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop. To compare:

friction_angles_new = []
for friction_angle in friction_angles:
    friction_angles_new.append(friction_angle + 2)
print(friction_angles_new)

# ... vs. the shorter list comprehension
friction_angles_new = [friction_angle + 2 for friction_angle in friction_angles]
print(friction_angles_new)
# it is short but comes at the price of readability

# Exercise 6

STOP = 1000

numbers = []

for i in range(STOP):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
print(sum(numbers))

# alternative as list comprehension
result = sum([i for i in range(STOP) if i % 3 == 0 or i % 5 == 0])

print(result)

# Exercise 7

rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
         'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
         'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke',
         'suevite']

START_YEAR = 2007

years = list(range(START_YEAR, START_YEAR+len(rocks)))

# alternative with enumerate()
for i, year in enumerate(years):
    print(f'the rock of the year {year} was {rocks[i]}')
# alternative with zip()
for year, rock in zip(years, rocks):
    print(f'the rock of the year {year} was {rock}')
