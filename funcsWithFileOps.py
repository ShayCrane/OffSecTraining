#!/usr/bin/python


# Open, read, store file contents into the variable "fileVar", then closes the file. Based on offsec.com learning path "Getting Good at Python".

# define the function
def storeFile(file):
    f = open(file, 'r')
    contents = f.read()
    f.close()
    return contents

# Variable that stores the filename. Note: file called out in this step must already exist for this to work.
fileVar = "notes.txt"

contents = storeFile(fileVar)
print(contents)
