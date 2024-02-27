# DATE 26 JULY 2023

#function can return dictionary
#Returning a dictionary

def build_person(first_name,last_name):
    musician=build_person('Ram','Sarkar')
    print(musician)
    
####################

#Returning dictionary  
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('Ram','Sarkar')
print(musician)


###############################################

#Passing a list

def greet_users(names):
    for name in names:
        msg=f"Hello, {name}"
        print(msg)
usernames=['Sahil','Aniket','Prajwal','Abhi']
greet_users(usernames)



###########################################

#Passing a arbitrary Number of Arguments

def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheeze')

##Using for loop
def make_pizza(*toppings):
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print(f'-{topping}')
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheeze')


#Mixing positional and arbitrary arguments

def make_pizza(size,*toppings):
    print(f"\nMaking a {size} inch pizza with following toppings:")
    for topping in toppings:
        print(f'-{topping}')
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheeze')
#######################
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green pepper','extra cheeze')


###########################################
#importing specific functions
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheeze')
##########################################


#using as to give a functions an alias

from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green pepper','extra cheeze')

##########################################
#using as to give a module an alias

import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green pepper','extra cheeze')

##########################################

#Importing all functions in module
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheeze')

############################################
#Scope of variable
x=x+1
x=6
print(x)
#you cant reference a variable 
x=6
x=x+1
print(x)

############################################

#Lambda Function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)


def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(4,5,6))
add=lambda a,b,c:a*b*c
add(4,5,6)

    
val=lambda *args:sum(args)
val(1,2,3,5,6)
val(1,2,3,5,7,8,9)

###########################################
#Keyword Arguments

def person(name,**data):
    print(name)
    print(data)
person('Navin',age=28,place='Mumbai',mob_no=9987654321)




def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='Navin',age=28,place='Mumbai',mob_no=9987654321)





val=lambda **data:sum(data.values())
val(a=2,b=3,c=6,d=8)


max=lambda a,b:x if (a>b)
print(max(1,2))  #error


max=lambda a,b:x if (a>b) else b
max=lambda a,b:x if (b>a) else a
#print(max(1,2))
print(max(10,8))

#####################################################
























































































































    