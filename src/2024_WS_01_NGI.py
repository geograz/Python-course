# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in October 2024
in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 1 on 7th October 2024
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

# addition
print(1 + 3)

# subtractions
print(54 - 98)

# division
print(10 / 3)

# multiplication
print(12*12)

# to the power of
print(3**3)

# floored division
print(10 // 3)

# modulo
print(10 % 3)

# Exercise 2

# 5 to the power of 8
print(5**8)
# square - root of 9
print(9**(1/2))
# remainder of 14 / 5
print(14 % 5)
# product of the floored quotient of 13 and 3 with 3
print(13//3*3)


### variables, string formatting

# give meaningful variable names
n_outcrops = 4

# string formatting is used to create dynamic strings and there are multiple
# options

# string concatenation
output_string_0 = 'today I mapped ' + str(n_outcrops) + ' outcrops'

# .format() method
output_string_1 = 'today I mapped {} outcrops'.format(n_outcrops)

# f-string method
output_string_2 = f'today I mapped {n_outcrops} outcrops'

print(output_string_0)
print(output_string_1)
print(output_string_2)

# typical use case for string formatting: file path creation
# here we use a "fromatted raw" string so that the backslashes are ignored
filename = 'figure3'
filepath = fr'C:\Users\GEr\{filename}.jpg'
print(filepath)

# dir function to see methods of objects
print(dir(123.34))


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# from start       0       1         2         3
# from end        -4      -3        -2        -1
soiltype_list = ['silt', 'sand', 'cobbles', 'clay', 'silty clay', 'sandy silt']
print(soiltype_list)

# accessing single elements
print(soiltype_list[2])

# slicing of lists
print(soiltype_list[:3])
print(soiltype_list[3:])
print(soiltype_list[2: 4])

# lists can be modified e.g. by adding or inserting values
soiltype_list.append('gravel')
soiltype_list.insert(1, 'silty sand')

# len() gives us the number of elements of a list, tuple or string
print(len(soiltype_list))


# Exercise 3

# create a new empty list
x = []

# compute the number of characters of the strings 'marl', 'gneiss', 'limestone', 'eclogite'
# append the numbers to the empty list in the above given order
x.append(len('marl'))
x.append(len('gneiss'))
x.append(len('limestone'))
x.append(len('eclogite'))

# print the list
print(x)

# compute the sum of the last three elements of the list
sum_last_3 = sum(x[-3:])

# print the result as a string “the result is: XX” two times by using the .format() method and an f-string.
print('the result is: {}'.format(sum_last_3))
print(f'the result is: {sum_last_3}')


# tuples are also collections of objects, but they cannot be modified
example_tuple = (10, 20, 30, 40)
print(example_tuple)
# to modify a tuple, convert it to another datatype first
example_tuple = list(example_tuple)
example_tuple.append(50)
print(example_tuple)
# ... and then convert it back
example_tuple = tuple(example_tuple)
print(example_tuple)


# a dictionary is an unordered collection of pairs of keys and values
# keys must be unique, values can be anything
#                      keys          values

friction_angle_dict = {'clay': [20, 19, 21],
                       'sand': [28, 29, 30],
                       'gravel': [35, 34, 33]}

print(friction_angle_dict['sand'])

# dictionaries can be created from lists
rocks = ['marl', 'limestone', 'granite']
UCSs = [30, 120, 200]  # [MPa]

rock_UCS_dcit = dict(zip(rocks, UCSs))

print(rock_UCS_dcit)

# keys and values of dictionaries can be accessed directly
soils = list(friction_angle_dict.keys())
friction_angles = list(friction_angle_dict.values())


# Exercise 4


