#!/usr/bin/python

# based on exercises and labs in offsec.com Get Good at Python learning path

# r: read; w: write; a: append; r+: read+write; 
# write mode will overwrite a file if it already exists; 
# 	append mode is a better option for adding data to an existing file



# b: binary (is appended to others if being used):
#	rb: read-binary file; wb: write-binary


# demonstration of opening a file in read mode
f = open("data.txt", "r")


# now that file is open and defined as variable f, we can read the contents using the read() method...

# contents of the file opened are stored as a string into variable "data"
data = f.read()


# readlines() can be used instead of read() to read only one line of the file at a time

# add readlines() in a forloop sequence, it temporarily stores the line in the variable that can be manipulated:
for line in f:
	prin(line)


# example of appending files using append, then write modes:

# declare variable
myData = "I'm sample data to be written to a file"

# open file in append mode
f = open("data.txt", "a")

# append value of variable "myData" to data.txt using write mode
f.write(myData)

# the file should be closed as a best practice
f.close()







