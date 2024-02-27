#7. 31.7.2023
#List comprehension Assignment 

###########################
#Find all the numbers fron 1 to 1000 which have 3 in them
three=[n for n in range(1,1000) if '3' in str(n)]
print(three)



#Count the number of spaces in the string
some='the slow solid squid swam sumptuously through the slimy swamp'
spaces=[s for s in some if s==' ']
print(len(spaces))
 


#####################################
#Find all the numbers from 1 to 1000 which are divisible by 7
div=[n for n in range(1,1000) if n%7==0]
print(div)

##################################

#Create alist of all consonents in the string
#"Yellow Yaks like yelling and yawning and yesterday they yodled while eating yucky yams"

sentence='Yellow Yaks like yelling and yawning and yesterday they yodled while eating yucky yams'
result=[letter for letter in sentence if letter not in 'a,e,i,o,u " "']
print(result)

##########################################
#Find the common numbers in two lists (without using a tuple or set) list

lst1=[1,2,3,4]
lst2=[2,3,4,5]
common=[a for a in lst1 if a in lst2]
print(common)

#########################################

#Get only the numbers in a sentence like 'In 1984 there were 13 instance of 
# a protest with over 1000 people attending'
sentence='In 1984 there were 13 instance of a protest with over 1000 people attending'
words=sentence.split()
result=[number for number in words if not number.isalpha() ]
print(result)

############################################
'''Given numbers=range(20) ,produce a list containing the word 'even' '''
for n in range(20):
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)


#List comprehension
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)

######################################
#Produce a lisyt of tuples consisting of only the matching numbers in these 
# list list_a=[1,2,3,4,5,6,7,8,9], lst_b=[2,7,1,12]. Result would look like
# (4,4),(12,12)

list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)


################################
#Find all the words in a string that are less than 4 letters
sentence='On a summer day ramnath sonar went swimming in the sun and his red skin stung'
examine=sentence.split()
result=[word for word in examine if len(word)<=4]
print(result)


##################################
#Write python pprogram for print a specified list after removing 0th, 4th
# and 5th elements.
color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print (color)

################################
#Write python program that creates a generator function that yields a 
# cubes of numbers from 1 to n , accept number from user
def cube_generator(n):
    for i in range(1,n+1):
        yield i**3
n=int(input("Enter Number: "))
#create the generator object
cubes=cube_generator(n)
#iterate over the loop
for num in cubes:
    print(num)

####################################
#Write a python program to implement a generator that generates random number
# within a given range

import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start,end)
start=int(input("Enter Start Number:"))
end=int(input("Enter end Number:"))
random_numbers=random_number_generator(start, end)
for _ in range(100):
    print(next(random_numbers))
    
    
#Write a python program to generate a 3*4*6 3d array whose each element
# is *
#3 rows
#4 columns
#6 columns

array=[[['*' for col in range(6)] for col in range(4)] for col in range(3)]
print(array)

####################################
#Write a python program to print the numbers of a specfied list after removing
# even numbers from it
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)



