# 8. 01 August 2023


#Use of zip function 
name=['dada','mama','kaka']
info=[9876,4324,2345]
for nm,inf in zip(name,info):
    print(nm,inf)


#Use of zip function with mis match list
name=['dada','mama','kaka','baba']
info=[9876,4324,2345]
for nm,inf in zip(name,info):
    print(nm,inf)
    
    
#Zip longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9876,4324,2345]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
    
#Use of fill value instead of none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9876,4324,2345]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)    

#Use of all() if all the values are true then it will produce output    
lst=[2,3,0,8,9]  #If 0 in list prints useless
if all(lst):
    print('All values are true')
else:
    print('Useless')
    
lst=[2,3,-5,8,9]  #If 0 not in list prints All values are true
if all(lst):
    print('All values are true')
else:
    print('Useless')
    
    
#Use of any if any one non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
    
#Use of any
lst=[0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
    

#######################################

#count() function:
    
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))    
print(next(counter))    
print(next(counter))    
print(next(counter)) 


#Now let us start from 1

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))  

#################################

#Cycle()

import itertools
instructions=("Eat","Code","Repeat")
for instruction in itertools.cycle(instructions):
    print(instruction)

#################################

#Repeat()

from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

#################################

#  combination()
from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players, 2):
    print(i)
    
#  permutations()
from itertools import permutations
players=['John','Jani','Janardhan']
for i in permutations(players, 2):
    print(i) 


#product()

from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)

#########################################

#Filter function:
age=[23,43,21,17]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])








































































































































































































































































   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    