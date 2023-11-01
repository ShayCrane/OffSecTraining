#!/usr/bin/python


# if, elif, and else statements refresher demo script; based on offsec.com learning path, Getting Good at Python


# set variable (this one is an integer)
numApples = 150
# numApples = 15
# numApples = 40


if numApples > 100:
    print("That's a lot of apples!")
elif numApples > 50:
    print("That's a very good amount of apples")
elif numApples > 30:
    print("That's a moderate amount of apples")
else:
    print("Running low on apples!")
