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

# repetition

# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1

# lists can be multiplied

# adding new entries to dictionaries


### control structures: conditional statements: if, elif, else, match cases,
### operators

air_temperature = 17  # [degrees]


if air_temperature > 30:
    print('do office work it is too hot')
elif air_temperature <= 5:
    print('do office work it is too cold')
elif air_temperature <= 10:
    print('rather do office work it might be too cold')
elif air_temperature == 18:
    print('today is the field day of the year!')
else:
    print('go out into the field')


nice_temperature = True

if nice_temperature is True:
    print('go out into the field')




### control structures: loops: while loop, for loop

# Exercise 5

# Exercise 6

# Exercise 7

# Exercise 3 - bonus

# Exercise 8

# Exercise 9


### functions

# Exercise 10


### coding style, Zen of Python


### modules, code environments, module documentation

# Exercise 11


### data handling with pandas, data visualization with matplotlib

# Exercise 12

# Exercise 13