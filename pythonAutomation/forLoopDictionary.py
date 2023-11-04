#!/usr/bin/python

# based on exercises and labs in offsec.com Get Good at Python learning path


guts = {
        "Name":"Guts",
        "Personality":"gruff",
        "Weapon":"Dragon Slayer",
        "Armor":"Berserker Armor"
        }

print(guts)


                                                                             # expected output from here without adding any more code is:                        

# kali@kali:~$ ./forDictionary.py
# {'Name': 'Guts', 'Personality': 'gruff', 'Weapon': 'Dragon Slayer', 'Armor': 'Berserker Armor'}


# additional code below iterates each key-value pair on separate lines... comment out line 10 "print(guts)"


for key in guts.keys():
    print(key + ": " + guts[key])
    
    

