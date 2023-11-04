#!/usr/bin/python


# if, elif, and else statements refresher with user input; based on offsec.com learning path, Getting Good at Python


# name = "Griffith"
# age = 24


# request user input
name = input("Please enter your name: ")
age = int(input("Please enter your age using integers only: ")) # make sure to type cast the user's age input as an integer by adding "int" and parens.


print("Hi " + name + "!")

if age >= 100:
    print("You are over 100 years old? What's your secret?")
elif age >= 70:
    print("You are over 70 years old? Are you retired or still working?")
elif age >= 60:
    print("You are over 60 years old? Will you be retiring soon?")
elif age >= 40:
    print("You are over 40 years old? What do you do for a living?")
elif age >= 20:
    print("You are over 20 years old? What do you want to do for your career?")
elif age >= 18:
    print("You are over 18 years old? That makes you a legal adult!")
else:
    print("It looks like you are under 18 years old.")
    
    
    
