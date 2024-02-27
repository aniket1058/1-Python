# 28 July 2023

#Dictionary assignment
'''
1.Write a python script to add a key to a dictionary
sample dictionary: {0:10,1:20}
'''

d={0:10,1:20}
print(d)
d.update({2:30})
print(d)

d={0:10,1:20}
print(d)
d[2]=30
print(d)

##############################################

'''
2.Write python program to concatenate the following dictionaries
 to create a new one
'''
#sample dictionary:
    #dict1={1:10,2:20}
    #dict2={3:30,4:40}
    #dict3={5:50,6:60}


dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)


'''
3.Write python script to check whether the given key
 is already exists in the dictionary or  not
'''
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def present(x):
    if x in d:
        print(f'{x} Key is present in dictionary.')
    else:
        print(f'{x} Key is not present in dictionary.')
present(5)
present(9)

'''
4.Write a python program to iterate over dictionaries using for loops
'''
d={'x':10,'y':20,'z':30}
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)

























