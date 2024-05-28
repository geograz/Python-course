# -*- coding: utf-8 -*-
"""
This script contains the code that was written during the first session for
educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 1 on 27th May 2024
###########################

### introduction and overview over Spyder


### datatypes: integers, floats, strings, print function

# there are three different types of strings
# type 1 - double quotes
"Georg's problem"
# type 2 - single quotes
'this is a problem of "rock mechanics"'
# multi line strings with single or double quotes
"""rock
mechanics"""
'''rock
mechanics'''

# Exercise 1


### operators: +, -, /, *, **, //, %

# integer
123
# floating point number
123.123

###########################
# Exercise 2
###########################

# print(5**8)
# print(9**(1/2))
# print(14 % 5)
# print(13//3*3)

# variables
# do not use functions and keywords as variable names

ROCK_TYPE = 'granite'  # recommendation for permanent / constant variables

color = 'green'
print(ROCK_TYPE, color)


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# lists use square brackets []
# indices         0  1  2  3  4  5
exemplary_list = [1, 2, 3, 4, 5, 6]

print(exemplary_list)

first_part_of_list = exemplary_list[:3]
second_part_of_list = exemplary_list[3:]
print(first_part_of_list, second_part_of_list)

list_of_lists = [[10, 20, 30], [40, 50, 60]]
print(list_of_lists[0][-1])
list_of_lists.append([70, 80, 90])
print(len(list_of_lists))

print(len('rock mechanics'))

# use dir() to find out methods of a dataype

# string formatting
rock_type = 'limestone'
ucs = 180  # [MPa]

# option 1
print('The ' + rock_type + ' has ' + str(ucs) + ' MPa')
# option 2
print('The {} has {} MPa'.format(rock_type, ucs))
# option 3
print(f'The {rock_type} has {ucs} MPa')

# example file path construction
FOLDER = r'C:\users\GEr\images'
file = 'test1.jpg'
filepath = fr'{FOLDER}\{file}'
print(filepath)

###########################
# Exercise 3
###########################

# empty_list = []

# empty_list.append(len('marl'))
# empty_list.append(len('gneiss'))
# empty_list.append(len('limestone'))
# empty_list.append(len('eclogite'))

# print(empty_list)
# sum_elements = sum(empty_list[-3:])
# print('the result is: {}'.format(sum_elements))
# print(f'the result is: {sum_elements}')

# tuples ... same as lists but not editable

exemplary_list = [1, 2, 3, 4, 5, 6]
exemplary_tuple = (1, 2, 3, 4, 5, 6)

print(exemplary_tuple)

# to modify a tuple, convert to a list first
exemplary_tuple = list(exemplary_tuple)
print(exemplary_tuple)
exemplary_tuple.append(7)
exemplary_tuple = tuple(exemplary_tuple)
print(exemplary_tuple)

###########################
# Exercise 4
###########################

# rock_list = ['gneiss', 'marl', 'limestone']
# rock_tuple = ('gneiss', 'marl', 'limestone')

# print(rock_list[:2])
# print(rock_tuple[:2])

# rock_list.append('greenschist')
# rock_tuple.append('greenschist')

# rock_list[1] = 'dolomite'
# rock_tuple[1] = 'dolomite'


# dictionaries are unsorted collections of keys & values

#                 key       value
rock_ucs_dict = {'granite': 180,
                 'marl': 20,
                 'eclogite': 250}
# add new entry to dictionary
rock_ucs_dict['dolomite'] = 110
print(rock_ucs_dict['dolomite'])

# create dictionary from 2 lists
rock_list = ['granite', 'marl', 'eclogite']
rock_ucs_list = [200, 20, 240]
rock_ucs_dict = dict(zip(rock_list, rock_ucs_list))
print(rock_ucs_dict)

# create lists from dictionary
list_from_dict_keys = list(rock_ucs_dict.keys())
list_from_dict_values = list(rock_ucs_dict.values())

###### control structures are used to control which parts of the code should be
# skipped or repeated
### conditional statements: if, elif, else, match cases

a = 40
b = 20

print(a < b)
print(a == b)
print(a != b and a < b)
print(a != b or a < b)

# exemplary conditional statement
if a < 50:
    print('a is smaller 50')
elif a < 100:
    print('a is smaller than 100')
elif a < 200:
    print('a is smaller than 200')
else:
    print('a is equal or larger than 200')

