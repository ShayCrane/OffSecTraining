#!/usr/bin/python


#While Loops - Offsec.com Learning Path: Get Good at Python


nameList = ["Sleepy", "Sneezy", "Happy", "Grumpy", "Bashful", "Dopey", "Doc"]

print(nameList)
                                                                            

# Get the number of items in the list and store the value in a variable
nameListCount = len(nameList)


# Print a message with how many items are in the list
print("There are " + str(nameListCount) + " names in the name list.")


nameIndex = 0
while nameIndex < nameListCount:
    # Print the index number
    print(nameIndex)
    # Print the name at the current index
    print(nameList[nameIndex])
    # Add 1 to the index value before the loop starts over
    nameIndex = nameIndex + 1 
