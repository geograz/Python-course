# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in May 2024 in
4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 3 on 13th May 2024
###########################

# repetition - control structures: conditional statements & loops

# Exercise 3 - bonus

empty_list = []

for rock in ['marl', 'gneiss', 'limestone', 'eclogite']:
    empty_list.append(len(rock))

print(empty_list)

sum_of_last_three = sum(empty_list[-3:])
print(f'the result is: {sum_of_last_three}')
print('the result is: {}'.format(sum_of_last_three))

# Exercise 8

rock_list = ['gneiss', 'marl', 'limestone']
ucs = [150, 45, 90]

# use a zip function to create dictionary
rock_dict = dict(zip(rock_list, ucs))
# use a for loop for new elements in empty dicitonary

rock_dict = {}

for i in range(len(rock_list)):
    rock_dict[rock_list[i]] = ucs[i]

rock_dict['greenshist'] = [80]

for rock in rock_dict.keys():
    print(f'The {rock} has a UCS of {rock_dict[rock]} MPa')

# Exercise 9

list_of_numbers = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# mean

mean = sum(list_of_numbers) / len(list_of_numbers)

print(f'mean value: {round(mean, 2)}')

# median

if len(list_of_numbers) % 2 != 0:  # uneven numbers of elements
    print('it is a list with an uneven number of elements')
    median = sorted(list_of_numbers)[int(len(list_of_numbers)/2)]
else:  # even numbers of elements
    print('it is a list with an even number of elements')
    lower = sorted(list_of_numbers)[int(len(list_of_numbers)/2)-1]
    upper = sorted(list_of_numbers)[int(len(list_of_numbers)/2)]
    median = (lower + upper) / 2

print(f'median value: {round(median, 2)}')

# variance

variance_temp_numbers = []

for number in list_of_numbers:
    variance_temp_numbers.append((number - mean)**2)

variance = sum(variance_temp_numbers) / len(variance_temp_numbers)

print(f'variance: {round(variance, 2)}')

# standard deviation

std = variance**(1/2)

print(f'standard deviation: {round(std, 2)}')


### functions

# functions are created with the "def" keyword and have to have a name and a
# "body" in brackets after the name
def hello_world():  # basic printing function
    print('hello world!')


# functions need to be executed like this to run
hello_world()


# function with input and output
def custom_subtraction(a: float, b: float) -> float:
    '''this is a custom subtraction function'''
    return a - b


print(custom_subtraction(5, 3))

# method vs function: methods and functions work in the same way but methods
# always belong to an object and functions are object independet
another_list = [3, 2, 1, 3, 2, 1]
# to sort a list with a method
another_list.sort()
print(another_list)
another_list.insert(3, 123)
print(another_list)
# to sort a list with a function
another_list = sorted(another_list)
print(another_list)


# Exercise 10

def custom_mean(x):
    return sum(x) / len(x)


def custom_median(x):
    median = sorted(x)

    if len(x) % 2 != 0:
        idx_median = int(len(x)/2)
        median = x[idx_median]
    else:
        idx_median = int(len(x)/2)
        median = (x[idx_median] + x[idx_median-1]) / 2
    return median


def custom_variance(x):
    nums_ = []

    for num in x:
        nums_.append((num - custom_mean(x))**2)
    nums_ = sum(nums_)
    return 1 / len(x) * nums_


def custom_std(x):
    return custom_variance(x)**(1/2)


nums = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# mean
mean = custom_mean(nums)
print(f'mean value: {round(mean, 2)}')

# median
median = custom_median(nums)
print(f'median value: {round(median, 2)}')

# var
var = custom_variance(nums)
print(f'var: {round(var, 2)}')

# std
std = custom_std(nums)
print(f'std: {round(std, 2)}')


# type hints in functions should be used which datatypes are required as input
# and to indicate which datatype will be the output. Furthermore default values
# can be set for the input arguments of a function
def state_of_weather(state: str = 'good') -> None:
    print(f'today the weather is {state}')


state_of_weather('sunny')

### coding style, Zen of Python
# check the zen of python by doing: "import this"
