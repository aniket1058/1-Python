# DATE --> 31/07/2023

# by normal method
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

# same code by LIST Comprehension ==>
#            ------------------------- 
lst=[num for num in range(0,20)]
print(lst)

#####################
names = ['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)


##################
#List comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

######################
#Looping of for loop
lst=[f"{x}{y}" for x in range(3) for y in range(3)]
print (lst)

##################
#Set Comprehension
set1={x for x in range(3)}
print(set1)

###################
dict={x:x*x for x in range(1000)}
print(dict)


##############################

#GENERATOR:
#It is another way of creating iterators in a simple way where it
# used keyword 'yield'

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

#"Next" Method
gen=(x for x in range(5))
next(gen)
next(gen)
next(gen)
next(gen)

###########################
#Function which returns multiple values

def range_even(end):
    for num in range(0,end,2):
        yield (num)
for num in range_even(6):
    print(num)

##########################
#Now instead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
next(gen)

#############################
#Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
    
 #######   
    
def lengths (itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
#Select number,
number = random.randrange(0,100)
#select special character
special_char = random.choice(string.punctuation)
#create new secure password
passwords = adjectives + nouns + special_char + str(number)
print(passwords)
for password in hide(lengths(passwords)):
    print(password,end='')
    
    

##################################

######         ENUMERATE        ###############
 #             =========
#Printing list with index
lst=["Milk","Egg","Bread"]
for index in range (len(lst)):
    print(f"{index+1} {lst[index]}")
    
#Same code can be implemented using enumerate
lst=["Milk","Egg","Bread"]
for index, item in enumerate(lst,start=1):
    print(f"{index} {item}")

    

















































