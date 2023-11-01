#!/usr/bin/python

# based on offsec.com learning path, Getting Good at Python.

# functions organize code into small snippets, making it more manageable as the scale and scope of your scripting increases

# there are two main requirements for successful functions in your script: 
# 	1. define the function; and
# 	2. call the function (or it will not execute).




# defining the function:
# def hello()
#	print("Hi there!")
	

# calling the function: 
# hello()




# arguments used in the function are passed to a given function within the parens
# a return statement supplies the function output back to your running script... here's a demo: 

# defining the function...
def addNums(numA, numB):
    answer = numA + numB
    return answer
    
x = addNums(5, 7)


# calling the function...
print(x)



