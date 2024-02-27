# 28 JULY 2023

#EXCEPTION HANDLING------------->
#------>Exceptions:Issues that Appear at run time or compile time
#------>Error: Occur due to absence of system resources

#--->Exceptions are handled with try-except blocks

#Handling the ZeroDivisionError exception
print(5/0)

#Using try-except block
a=5
b=6
c=a=b
print(5/0)
try:
    print(5/0)
except ZeroDivisionError:
    print('You cant divide by zero!')
print(c)##############    ERROR



a=5
b=6
c=a=b
try:
    print(5/0)
except ZeroDivisionError:
    print('You cant divide by zero!')
print(c)  #####################       CORRECT 

#########################################################


#Handling the FileNotFoundError Exception
###  IMPORTANT   ####

filename='alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f'Sorry the file {filename} does not exist.')

    
###########################################################

'''
#Storing Data
#Stored in JSON (javascript object notation) file 
#JSON file is in the form of Dictionary
#What is JSON is--->  Format was originally developed for JavaScript
#Many of your users will ask to input certain kinds of information.
#A simple way to do this involves storing your data in JSON
#Whenever any ip is taken from user any input, Then mechanism
# provided is ---> JSON
#Data is transferred and stored through JSON only
'''

#Using json.dump() and json.load()
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open (filename, 'w') as f:
    json.dump(numbers, f)

import json
username=input('What is your name? : ')
filename='username.json'
with open (filename, 'w') as f:
    json.dump(username,f)
print(f"We'll remember you when you come back,{username}!")

################################
#Now lets write new program that greets a user whose name has already been stored

import json
filename='username.json'
with open (filename) as f:
    username=json.load(f)
print(f"Welcome back {username}!")


################################

#Load the username,if it has been previously
# otherwise, prompt for the username and store it.

try:
    with open (filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input('What is your name?:')
    with open (filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
        



































































