'''Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.'''

import os
#Select the directory path whose content you want list
directory_path = '/'

# use the os module to list down the directory content
contents = os.listdir(directory_path)
    
#print the directory content 
for item in contents:
        print(item)
