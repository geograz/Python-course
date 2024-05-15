# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in May 2024 in
4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, Sjur Beyer MSc., georg.erharter@ngi.no
"""


###########################
# session 4 on 15th May 2024
###########################

### Reading and writing to files in python

"""
Take the "Zen of python" from being suggestions to being commandments.
For this we need to read a textfile that has the contents of the Zen of python.

Creating such a file can be done by opening Anaconda Prompt and writing:
python -c "import this" > zen_of_python.txt

Locate the file and move it into the directory where this script is.

"""

# set the with statement to open the textfile in read mode, and specify a variable name
with open("zen_of_python.txt", mode="r") as readfile:
    # read the content of the file to a list of string
    # one element per line
    content = readfile.readlines()
    
    # set a counter
    counter = 1
    
    # set an iterator for the indices of the list
    for i in range(len(content)):
        # set the line at the index as a variable
        line = content[i]
        
        # the first two lines are not a commandment
        # we are only interested in the lines after index 1 (NB! i=1 is line 2)
        if i > 1:
            content[i] = f"{counter}. {line}"
            # add one to the counter for the next commandment
            counter = counter + 1

        
    
# now we write the results by opening an empty file in write mode
with open("commandments.txt", mode="w") as writefile:
    writefile.writelines(content)



# Exercise 14
# Data Located at: https://offshorewind.rvo.nl/files/view/78bae29d-c8b6-409e-aead-0de48a920914/1609857721tnw_20201019_fnlm_in%20situ%20test%20locations%20report%20digital%20data_v01-f.zip



