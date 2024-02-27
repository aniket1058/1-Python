#####################################

#indentation error
num = int (input('Enter a number:'))
if num >0:
print (num)


#if statement
num = int (input('Enter a number:'))
if num >0:
    print (num)
    
#####################################
    
#if else
num=int(input('enter:'))
if num<0:
    print('negative')
else:
    print('positive')
    
    
###################################

#else if (elif) condition

a=float(input('Enter how much savings:'))
if a==0:
    print('Sorry no savings')
elif a<500:
    print('Well done')
elif a<1000:
    print('Thats a tidy sum')
elif a<10000:
    print('Welcome sir')
else:
    print('Thank you')


#################################
#while loop
count =1
while count<=10:
    print(count)
    count+=1
    
################################

#for loop
#loop over a set of values in range
print('Print out values in range')
for i in range(2,10):
    print(i)
print('Done')


print('Only print code if all iterations completed')
num=int(input('Enter a number to check for:'))
for i in range (0,16):
    if i == num:
        break
    print(i)
print('Done')

####################################
#Now use an 'anonymous' loop variable

for _ in range(0,10):
    print('.',end='')
    print()               #output as vertical '.'
    
    
for _ in range(0,10):
    print('.',end='')      #output as horizontal '.'
    
    
#######################################

#Break loop statement
for i in range(0,6):
    if i == num:
        break
    print(i,'',end='')
print('Done')

#location of print is changed
for i in range(0,6):
    if i == num:
        break
    print(i,'',end='')
    print('Done')

######################################

#Program to print odd numbers in the given range
start,end=3,25

for num in range(start,end+1):
    if num%2 != 0:
        print(num,end=' ')
        
        
#Program to print even numbers in the given range
start,end=3,25

for num in range(start,end+1):
    if num%2 == 0:
        print(num,end=' ')
        
        

#Program to print all even numbers in the range
for even_numbers in range(0,21,2):
    if even_numbers%2 == 0:
        print(even_numbers,end=' ')
        
#Program to print all odd numbers in the range       
for odd_numbers in range(1,30,3):
    if odd_numbers%2 != 0:
        print(odd_numbers,end=' ')
        
        
#write code for finding prime numbers in given range
start,end=1,100
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
           
            
num=int (input('Enter no:'))
count=1
for i in range (count,num+1):
    if(num%count==0):
        count+=1
if(count==2):
    print('prime number')
else:
    print('not prime')
    
def prime_num (num):
    for i in range(2,num):
        if(num%i)==0:
            return"Not Prime"
            break
    return"Prime"
        
    

#Leap year
a=int(input('Enter Year:'))
if(a%4==0 and a%100!=0 or a%400==0):
    print('Leap year')
else:
    print('Not leap year')



#Is palindrome
x=input('Enter string:')
y=x[::-1]
print(x)
if x==y:
    print('Is a palindrome')
else:
    print('Not palindrome')


#Mario pyramid
for i in range(4):
    for j in range (i+1):
        print('*',end=' ')
    print()
    
for i in range(4):
    for j in range (4-i):
        print('*',end=' ')
    print()
        


##################################################
#global variables
x='Awesome'
def my_function():
    print("python is " +x)
my_function()



##################################################
#local and global variables
x="Awesome"
def my_function():
    x="Fantastic"
    print("Python is "+x)
my_function()
print("Python is "+x)


##################################################
#Dictionary
x={'name':"Ram","age":21}
print(type(x))
print(x)


###############################################
str1="Hello"
str2=2
str3=str1+str2   #error:only concatenate string(not "int") to str
print(str3)

##################################################
#string
#if you want multiple line strings
x="""This is python.
It is very Powerful"""
print(x)

##############################################
#string slicing
print(x[2:11])

#####################
#slicing from start
print(x[:3])

#####################
#slicing to end
print(x[4:])

####################
#negative indexing
x="This is Python"
print(x[-5:-2])

x="       Aniket Wakchaure"
x=x.upper()
print(x)
x=x.lower()
print(x)
print(x.strip())
print(x.replace("aniket","Sanket"))

#replace
x="hello aniket"
print(x.replace("aniket","Sanket"))

#use of split which replaces whilte space/or
x="hello aniket"
print(x.replace("aniket","Sanket"))
print(x.split(","))

#split string
x="hello aniket"
print(x.replace("aniket","Sanket"))
print(x.split(" "))


#to reverse given string
x="Hello World"
string1=x[::-1]
print(string1)
string1=x[::-2]
print(string1)


########################
#find function
x="This is python and is very powerful"
print(x.find("and"))

#string concatination
x="hello"
y="world"
print(x+y)
print(x+""+y)
print(x+" "+y)


#########################
x=36
y="My name is anthony"
#print(x+y)
#this will give error
print(f"my name is anthony and my age is {x}")


quantity=3 
item_no=54
price=67
print(f"I want {quantity} pieces and item number {item_no} , its price is {price}")
      
      
my_order="I want {} pieces and item number is{}, its price is {}"
print(my_order.format(quantity,item_no,price))

quantity=3 
item_no=54
price=67
my_order="I want {0} pieces and item number is {1}, its price is {2}"
print(my_order.format(quantity,item_no,price))


############################################
#escape character
a="This is \"fun fair\""
print(a)


a=20
b=10
print(a!=b)





    



























