# -*- coding: utf-8 -*-
"""
This script contains the code that was written during the second session for
educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 2 on 28th May 2024
###########################

###### control structures are used to control which parts of the code should be
# skipped or repeated
### conditional statements: if, elif, else, match cases

a = 40
b = 20
# operators used to compare number values
print(a < b)
print(a == b)
print(a >= b)
print(a != b and a < b)
print(a != b or a < b)

# exemplary conditional statement wit logical if-else
if a < 50:
    print('a is smaller 50')
elif a < 100:
    print('a is smaller than 100')
elif a < 200:
    print('a is smaller than 200')
else:
    print('a is equal or larger than 200')

# another example
soil_type = 'cobble'

if soil_type == 'clay':
    print('the soil is fine grained')
elif soil_type == 'silt':
    print('the soil is fine grained')
elif soil_type == 'sand':
    print('the soil is coarse grained')
elif soil_type == 'gravel':
    print('the soil is coarse grained')
else:
    print('the soil is coarse grained')

# match case as an alternative to logical if-else statements
match soil_type:
    case 'clay':
        print('the soil is fine grained')
    case 'silt':
        print('the soil is fine grained')
    case 'sand':
        print('the soil is coarse grained')
    case 'gravel':
        print('the soil is coarse grained')
    case _:
        print('the soil is coarse grained')

### loops: while loop, for loop

# while loops run until the condition is not valid anymore

# generic example
a = 1
while a < 10:
    print(f'the value of a is {a}')
    a = a + 1
print(f'after the loop a is {a}')

###########################
# Exercise 5
###########################

fibonaccis = [0]

num = 1
STOP = 200_000_000

while num < STOP:
    fibonaccis.append(num)
    num = fibonaccis[-1] + fibonaccis[-2]

print(fibonaccis)

# for loops are used to iterate over a finite set
soil_types = ['clay', 'silt', 'sand', 'gravel']
friction_angles = [20, 26, 30, 33]  # degrees
cohesions = [20, 10, 0, 0]  # kPa

for soil in soil_types:
    print(soil)

# the range function gives a range of numbers from 0 (default) at a step of 1 (default)
print(list(range(20, 50, 3)))

# get iterator for multiple lists
for i in range(len(soil_types)):
    print(f'the {soil_types[i]} has a friction angle of {friction_angles[i]} degrees and a c of {cohesions[i]} kPa')
print('\n')
for i, soil in enumerate(soil_types):
    print(f'the {soil} has a friction angle of {friction_angles[i]} degrees and a c of {cohesions[i]} kPa')

# example for one liners / list comprehensions
new_cohesions = []
for c in cohesions:
    correct_cohesion = c + 5
    new_cohesions.append(correct_cohesion)
print(new_cohesions)
# one liner alternative
new_cohesions2 = [c + 5 for c in cohesions]
print(new_cohesions2)

###########################
# Exercise 3+
###########################

empty_list = []

rocks = ['marl', 'gneiss', 'limestone', 'eclogite']
# for rock in rocks:
#     empty_list.append(len(rock))

iterator = 0

while iterator < len(rocks):
    empty_list.append(len(rocks[iterator]))
    iterator += 1  # same as "iterator = iterator + 1"

print(empty_list)
sum_elements = sum(empty_list[-3:])
print('the result is: {}'.format(sum_elements))
print(f'the result is: {sum_elements}')

###########################
# Exercise 6
###########################

STOP = 1000

nums = []

for i in range(STOP):
    if i % 3 == 0 or i % 5 == 0:
        nums.append(i)


# nums = [i for i in range(STOP) if i % 3 == 0 or i % 5 == 0]

print(sum(nums))

###########################
# Exercise 7
###########################

rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
          'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
          'slate', 'andesite', 'andesite', 'gypsum and anhydrite',
          'greywacke', 'suevite']

START_YEAR = 2007
years = list(range(START_YEAR, START_YEAR+len(rocks)))

for i, year in enumerate(years):
    print(f'the rock of the year {year} was {rocks[i]}')

###########################
# Exercise 8
###########################

rock_list = ['gneiss', 'marl', 'limestone']

ucs = [150, 45, 90]

rock_dict = dict(zip(rock_list, ucs))

# rock_dict = {}
# for i in range(len(rock_list)):
#     rock_dict[rock_list[i]] = ucs[i]

rock_dict['eclogite'] = 220

for key in rock_dict.keys():
    print(f'The {key} has a UCS {rock_dict[key]} MPa')


