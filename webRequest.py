#!/usr/bin/python


# based on exercises and labs in offsec.com Get Good at Python learning path
# making web requests using python modules
#   the "requests" module includes the following functions: 
#   get, status_code, headers, encoding, text, and json.


# import the requests module
import requests



# requests the webpage called out below, stores it in a variable, and prints the status of the webpage to the terminal;
#   contents of webpage get stored in the variable "page", which is used to check the web response status using 'status_code' function. 
page = requests.get('https://www.offsec.com/offsec/game-hacking-intro/')
print(page.status_code)



# output will be http response code; for example: "200" = page was successfully reached. 
