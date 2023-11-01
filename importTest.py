#!/usr/bin/python


# based on exercises and labs in offsec.com Get Good at Python learning path




def printFlag(file):

        f = open(file, 'r')
        contents = f.read()
        f.close()
        return contents


file = "importMe.py"

contents = printFlag(file)
print(contents)



# calling the function as seen below is not necessary to print the contents read by the script:
# printFlag(file)
