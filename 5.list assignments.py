##LISTS ASSIGNMENTS
#27 July 23

#write python program to add all the items in the list

def add_items(num):
    sum=0
    for i in num:
        sum=sum+i
    return sum
lst=[1,3,4,5,7]
print(add_items(lst))


#Write a python program to multiply all items in the list
lst=[1,2,3,4]
def mult_items(num):
    mul=1
    for i in num:
        mul=mul*i
    return mul
print(mult_items(lst))

#Write python program to get the largest and smallest number in the list

lst=[23,21,34,32,45,43]
print(max(lst))
print(min(lst))

#Write python program to count the number of strings which satisfies the 
#condition that the string length is 2 or more and the first and last 
#character are the same
lst1=['abc','xyx','aba','1221']
def match_words(words):
    count=0
    for i in words:
        if len(i)>2 and i[0]==i[-1]:
            count+=1
    return count
print(match_words(lst1))


#write python program to get a list, sorted in increasing order by
#the last element in each tuple from a given list of non-empty tuples.
lst1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def sort_lst(num):
    for i in num:
    
        print()
####################     
lst1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def last(n):
    return n[-1]
def sort_list(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list(lst1))

a=[10,20,30,20,10,50,60,40,80,50,40]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)

a=[10,20,30,20,10,50,60,40,80,50,40]
b=set(a)
print(b) #set removes duplicate items , hence list is converted to set
b=list(b)
print(b) # converted to set



#Write python program to clone or copy a list

a=[10,20,30,20,10,50,60,40,80,50,40]
new=[]
new.extend(a)
print(new)

a=[10,20,30,20,10,50,60,40,80,50,40]
new=list(a)
print(a)
print(new)


#Write a code to find the list of words that are longer than n
# from given list of words
def long_words(n,str):
     word_len=[ ]
     txt=str.split(" ")
     for x in txt:
         if len(x)>n:
             word_len.append(x)
     return word_len
print(long_words(3, "The quick brown fox jumps over lazy dog"))


#Write a python function that takes two lists and return true if
#the have at least one common member

def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
    return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))
    

#Write python program to calculate difference between two lists
#Unique elements difference and concatenate
list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
print(diff1)
print(diff2)
total_diff=diff1+diff2
print(total_diff)

#IMP#
#Write a python program to convert a list of characters into a string
#IMP#
s=['a','b','c','d']
str1= ''.join(s)
print(str1)

#Write a python program to find the index of an item in a specified list
num=[10,30,4,-6]
print(num.index(30))

#Write a python program to append a list to the second list
list1=[1,2,3,4]
list2=['Red','Green','Black']
final=list1+list2
print(final)





