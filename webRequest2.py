#!/usr/bin/python


# based on exercises and labs in offsec.com Get Good at Python learning path
# making web requests using python modules
#   the "requests" module includes the following functions: 
#   get, status_code, headers, encoding, text, and json.


# import the requests module
import requests



# requests the webpage called out below, stores it in a variable, and prints the status and contents of the webpage to the terminal, which can be manipulated;
#   contents of webpage get stored in the variable "r", which is used to check the web response status using 'status_code' and 'text' function.

r = requests.get('https://www.offsec.com/offsec/game-hacking-intro/')
print(r.status_code)
print(r.text)
