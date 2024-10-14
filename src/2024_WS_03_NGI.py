# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in October 2024
in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 3 on 14th October 2024
###########################


# Exercise 8

# create two lists with the following content:
rock_list = ['gneiss', 'marl', 'limestone']
ucs = [150, 45, 90]

# create a dictionary called “rock_dict” with the first list as keys and the
# second list as values

rock_dict = dict(zip(rock_list, ucs))
print(rock_dict)

# add a new entry to the dictionary consisting of a new rock type and an
# according UCS value

rock_dict['granite'] = 160

# print the content of the whole dictionary to the console through formatted
# strings saying “The XX has a UCS of YY MPa”. Use a for-loop for this

for rock in rock_dict.keys():
    print(f'The {rock} has a UCS of {rock_dict[rock]} MPa')


# Exercise 9
numbers = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]
n_numbers = len(numbers)

# mean
mean = sum(numbers) / n_numbers
print(f'mean value: {round(mean, 2)}')

# median
numbers_sorted = sorted(numbers)

if n_numbers % 2 == 0:
    idx_median = int(n_numbers/2)
    median = (numbers_sorted[idx_median] + numbers_sorted[idx_median - 1]) / 2
else:
    idx_median = int(n_numbers/2)
    median = numbers_sorted[idx_median]
print(f'median value: {round(median, 2)}')

# variance
sum_list = []
for number in numbers:
    sum_list.append((number - mean)**2)
sum_ = sum(sum_list)

variance = 1/n_numbers * sum_
print(f'variance value: {round(variance, 2)}')

# standard deviation
std = variance ** (1/2)
print(f'standard deviation: {round(std, 2)}')


### functions

# functions are created with the "def" keyword and have to have a name and a
# "body" in brackets after the name


def hello_world_function():  #  # basic printing function
    print('Hello World!')


# functions need to be executed like this to run
hello_world_function()


# function with input and output
def custom_subtraction(a: float, b: float) -> float:
    '''this is a custom subtraction function'''
    return a - b


print(custom_subtraction(5, 3))


# Exercise 10

# mean
def mean_function(number_list):
    return sum(number_list) / len(number_list)


def median_function(number_list):
    numbers_sorted = sorted(number_list)
    n_numbers = len(number_list)

    if n_numbers % 2 == 0:
        idx_median = int(n_numbers/2)
        median = (numbers_sorted[idx_median] + numbers_sorted[idx_median - 1]) / 2
    else:
        idx_median = int(n_numbers/2)
        median = numbers_sorted[idx_median]

    return median


def variance_function(number_list, mean):
    sum_list = []
    for number in number_list:
        sum_list.append((number - mean)**2)
    sum_ = sum(sum_list)

    variance = 1/len(number_list) * sum_
    return variance


def std_function(variance):
    return variance**(1/2)


numbers = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

mean = mean_function(numbers)

median = median_function(numbers)

variance = variance_function(numbers, mean)

std = std_function(variance)

print(f'mean value: {round(mean, 2)}')
print(f'median value: {round(median, 2)}')
print(f'variance value: {round(variance, 2)}')
print(f'standard deviation: {round(std, 2)}')


# example for function with pultiple outputs
def get_soil_properties(soil_name):

    match soil_name:  # noqa
        case 'clay':
            c, phi = 10, 20
        case 'sand':
            c, phi = 0, 30
        case _:
            c, phi = 'NAN', 'NAN'

    return c, phi


soil_props = get_soil_properties(soil_name='clay')
print(soil_props)

soil_c, soil_phi = get_soil_properties(soil_name='silt')
print(soil_c, soil_phi)

### coding style, Zen of Python

# import this
