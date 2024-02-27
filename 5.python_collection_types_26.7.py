# 26 july 2023

#Creating Tuples

tup=(1,2,3,4)
        #Accessing elements of tuples
print(f"tup[0]:\t {tup[0]}")
print('tup[1]:\t', tup[1])
print('tup[2]:\t', tup[2])
print('tup[3]:\t', tup[3])


tup2=(1,'John',True, -12.32)
print(tup2[3])

#iterating over tuples
tup3=('apple', 'orange', 'banana', 'apple')
for x in tup3:
    print(x)
    
    
#Tuple related functions
#You can also find length of tuple
len(tup3)

#You can count how many times a specified value appeared in tuple

tup4=('apple', 'orange', 'banana', 'apple', 'apple')
#tuples allows duplicates
tup4.count('apple')


#can also find out (first) index of value in tuple
print(tup4.index('apple'))
print(tup4.index('banana'))


#checking if an element exists
if 'orange' in tup3:
    print('orange is in the tuple')
    
    
#Nested Tuples
#tuples can be nested within tuples
#tuple can contain as one of its elements in another tuple
tuple1=(1,2,3,4)
tuple2=('ani','sah','pra','abh')
tuple3=(42,tuple1,tuple2,5.5)
print(tuple3)



############################################################

#LISTS:-  Mutable , []

#creating lists
lst1=['John','Mike','Trevor','Franklin']


lst1=[1,25.3,True]
lst2=['apple','orange',31]
root_list=['john',lst1,lst2,'denise']
print(root_list)

    
#####################################################
#accessing elements from list
lst1=['John','Paul','George','Ringo']
print(lst1[-1])
print(lst1[0])
print(lst1[-2])
lst1[-3]


lst1=['John','Paul','George','Ringo']
print('lst1[1]:',lst1[1])
print('lst1[-1]:',lst1[-1])
print('lst1[1:3]:',lst1[1:3])
print('lst1[:3]:',lst1[:3])
print('lst1[1:]:',lst1[1:])


#Adding to the list
#append-adding to the end of list
lst1=['John','Paul','George','Ringo']
lst1.append('Pete')
print(lst1)

#You can also add all the items ina list to another list.
#extend-adding elements in a list
lst1=['John','Paul','George','Ringo']
lst1.extend(['Albert','Bob'])
print(lst1)

#inserting into a list
a_list=['Adele','Madonna','Sahil']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)

#List concatenation
lst1=[3,2,1]
lst2=[6,5,4]
lst3=lst1+lst2
print(lst3)

#Removing from list
#in this we directly give the element in the list 
lst1=[3,2,1]
lst1.remove(2)
print(lst1)


lst1=[3,2,1]
lst1.remove(lst1[2])
print(lst1)

lst1=['John','Paul','George','Ringo']
lst1.remove('George')
print(lst1)

#pop method in lists
#in this the index is given to remove element from list
lst1=['John','Paul','George','Ringo']
lst1.pop(2)
print(lst1)


#inserting in the list
lst1=['John','Paul','George','Ringo']
lst1.insert(2,'Shawn')
print(lst1)





#1.Take 5 numbers in a list and find out min and max in the list
#2.Take 5 strings in the list make it reverse
#3.Take 10  numbers in the list write script to search for a value
#4.Take 10 numbers in list , insert some duplicate numbers write script to find duplicates
#5.Take vowels in the list and non vowel letters find the total number of vowels in the list

#1
lst1 = [25,36,16,32,54]
minimum = min(lst1)
maximum = max(lst1)
print("Minimum:", minimum)
print("Maximum:", maximum)


#2
lst2=["Michael","Jordan","James","Franklin","Shawn"]
lst2.reverse()
print(lst2)


#3
lst3=[32,12,14,45,25,46,37,38,29,74]
x=int(input("Enter a Number:"))
if x in lst3:
    print(x ,"is present")
else:
    print(x ,"is not present")
    

#4
lst4=[32,12,14,45,32,46,37,12,32,46]
for num in lst4:
    if lst4.count(num)>=2:
        print(num, "is duplicate in list")
        




lst4=[21,35,47,21,59,72,61,49,59,85]
unique=[]
duplicate=[]
for i in lst4:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)        
print(duplicate)


#5
lst5=['a','e','u','d','e','k','a','b']
vowels=['a','e','i','o','u','A','E','I','O','U']

lst5=['a','j','u','c','e','k','a']
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0  
i=0
for lst5[i] in lst5:
    if lst5[i] in vowels:
        count+=1
print("The Count of Vowels is :",count)
    





######################################################


#DATE:27 July 23
#SETS:
#Creating a set
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

#Adding items to set
basket={'apple','orange','apple','pear','orange','banana'}
basket.add('mango')
print(basket)

#should be passed in list for multiple adding of values in set
basket={'apple','orange','apple','pear','orange','banana'}
basket.update(['mango','grapes'])
print(basket)


#obtaining the length of set
basket={'apple','orange','apple','pear','orange','banana'}
print(len(basket))

#obtaining max and min value in set
basket2={32,42,12,34,26}
print(min(basket2))
print(max(basket2))

#Removing an item in set
basket={'apple','orange','apple','pear','orange','banana'}
basket.remove('apple')
basket.discard('banana')
print(basket)

#########################################
#Set operations
s1={'apple','orange','pear','banana'}
s2={'grapefruit','lime','banana'}
print('Union:',s1|s2)
print('Intersection:',s1&s2)
print('Difference:',s1-s2)



#################################################

#DICTIONARIES:
capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'MP':'Bhopal',
          'Karnataka':'Bangalore'}
print(capitals)

#Accessing items via keys
print('capitals[Maharashtra]:', capitals['Maharashtra'])

#Adding a new entry
capitals['West Bengal']='Kolkata'
capitals

#changing a key value
capitals['Gujrat']='Gandhinagar'
print(capitals)

#Removing an entry
capitals.pop('Karnataka')
print(capitals)


del capitals['MP']
print(capitals)


#iterating over keys
capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'MP':'Bhopal',
          'Karnataka':'Bangalore'}
for states in capitals:
    print(states, end=', ')
for states in capitals:
    print(states, end=', ')
    print(capitals[states])


#Values, Keys and Items
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#Checking key membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)
 
#Dictionaries can have values in tuples
season={'Summer':('Feb','Mar','April','May'),
        'Winter':('June','July','Aug','Sep'),
        'Rainy':('Oct','Nov','Dec','Jan')}
print(season['Rainy'])
print(season['Rainy'][1])

#Dictonary Methods
dict2={'brand':'Maruti',
       'model':'Brezza',
       'year':2021,
       'year':2020}   #Duplicates keys are not allowed in dictionaries
print(dict2)

#loop through a dictionary, it will show only keys
for x in dict2:
    print(x)
    
#print all values in dictionary one by one





        
































































































































































