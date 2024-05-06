# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in May 2024 in
4x4 hour sessions.

This script contains the code that was written during the sessions for
educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 1 on 6th May 2024
###########################

### introduction and overview over Spyder


### basic datatypes: strings, integers, floats, print function

# there are 2 ways to create strings:
'Hello world'  # single quote string
"Hello world"  # double quote string
# ... and both can be used to create multi line strings with linebreaks
"""
Hello
World
"""

'''
Hello
World
'''

# integers = numbers without decimals
1, 2, 3

# floats = floating point numbers = numbers with decimals
1.2, 34.6789, 100.100

# the print() function is used to print output and results to the console
print('Hello World')

# there are functions to convert datatypes into each other
print(float(10))
print(int(10.734))
print(str(10))

# Exercise 1

### operators: +, -, /, *, **, //, %

print(1 + 3)  # addition
print(3 - 5)  # subtraction
print(12 / 3)  # division
print(2 * 3)  # multiplication
print(4 ** 2)  # to the power of
print(13 // 4)  # floored division
print(12 % 5)  # modulo

# Exercise 2

### variables, string formatting

# variables are placeholders for all kinds of datatypes
# variable names should be explicit and informative
limestone_ucs = 90  # [MPa]

# string formatting is used to create dynamic strings and there are multiple
# options
# string formatting option 1
print('the UCS of the rock is ' + str(limestone_ucs) + ' MPa')

# string formatting option 2
print('the UCS of the rock is {} MPa'.format(limestone_ucs))
print('the UCS of the rock is {} {}'.format(limestone_ucs, 'MPa'))

# string formatting option 3
print(f'the UCS of the rock is {limestone_ucs} MPa')

# typical use case for string formatting: file path creation
# here we use a "fromatted raw" string so that the backslashes are ignored
filename = 'figure3'
filepath = fr'C:\Users\GEr\{filename}.jpg'
print(filepath)


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# lists are mutable / editable collections of all kinds of objects
# lists and tuples are ordered and elements have an index, starting with 0
# index          0         1           2
soil_types = ['gravel', 'clay', 'sandy gravel']
print(soil_types)
# to call specific elements of a list or tuple, use the index behind the list
print(soil_types[0])  # first element
print(soil_types[1])  # second element
print(soil_types[-1])  # last element

# lists can be modified e.g. by adding or inserting values
soil_types.append('silt')
soil_types.insert(1, 'silty sand')
print(soil_types)

# len() gives us the number of elements of a list, tuple or string
print(len(soil_types))

# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1
number_list = list(range(10))
print(number_list)

# lists can be multiplied
many_soil_types = soil_types * 10
print(many_soil_types)

# lists can be sliced up with indices
slice_of_many_soil_types = many_soil_types[10: 15]
print(slice_of_many_soil_types)

# a dictionary is an unordered collection of pairs of keys and values
# keys must be unique, values can be anything
#              keys          values
rock_UCSs = {'granite': [220, 200, 205],
             'limestone': [140, 130, 120],
             'eclogite': [250, 300, 270]}

# new entries can be added to the dictionary like this
rock_UCSs['marl'] = [30, 20, 40]
print(rock_UCSs)

# Exercise 3

###########################
# session 2 on 8th May 2024
###########################

# repetition

# Exercise 4


### control structures: conditional statements: if, elif, else, match cases


### control structures: loops: while loop, for loop

# Exercise 5

# Exercise 6

# Exercise 7

# Exercise 8

# Exercise 9

### functions

# Exercise 10


### reading & writing files with Python directly


### coding style, Zen of Python


### modules, code environments, data visualization

# Exercise 11

### data handling with pandas
# import CPT dataset Premstaller and visualize random CPT test

# Exercise 12

# Exercise 13

# Exercise 14

