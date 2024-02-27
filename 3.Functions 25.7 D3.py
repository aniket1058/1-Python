#DATE:25 July 23

#Functions
#never write function name in capital and dont give space
x=int(input("enter no.:"))
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "Not Prime"
            break
    else:
        return 'Neither Prime Nor Composite'
    return "Is prime"
print(prime_num(x))

#######################################
#function without argument
def greet_user():
#Display a simple greeting
    print("hello!")
greet_user()


######################################

#passing info to function
def greet_user(username):
#Display a simple greeting    
    print(f"Hello,{username}!")
greet_user("Sanjivani AI")


###########################################

def describe_pet (animal_type,pet_name):
#animal_type,pet_name are positional arguments
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('Dog','Modi')

#Order matters in positinal arguments

###############################################

#Default values
def describe_pet (pet_name,animal_type='Dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='Moti')


##############################################
#Avoiding argument errors
def describe_pet (pet_name,animal_type):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()

#######################################

####Program for roller coster if your height is 120 cm or greater 
#then you are eligible to play roller coster, if your age is under
#18 then tickets will be 20 rs, if age is more than 18 tickets will
#be 50 rs, if age is less than 12 and height is equal to 120 cm then
#ticket will be 10 rs and age is betn 12 to 18 and height is 120 rs 
#then ticket is 15 rs
print("Welcome to the Roller Coaster")
height=int(input("Enter height in cm:"))
if (height>=120):
    age=int(input("Enter age:"))
    print("Eligible")
    if(age<=18 and height>120):
        print("Ticket is 20 Rs") 
    elif(age>18):
        print("Ticket is 50 rs")
    elif(age<12 and height==120):
        print("Ticket is 10 Rs")
    elif(12<=age<=18 and height==120):
        print("Ticket is 15 Rs")
else:
    print("Invalid Height")
    
    
    
    
    
print("Welcome tp roller coaster")
height=int(input("Enter a height: "))
bill=0
if height>=120:
    print("U are eligible to play rolar coastar")
    age=int(input("Enter a age:"))
    if age<12:
        print("5 Rs")
        bill=5
    elif age<=18:
        print("10")
        bill=10
    else:
        print("15")
        bill=15
    want_photo=input("Do you want photo Y or N: ")
    if want_photo=='Y':
        bill+=3
        print(f"your total bill wiil be{bill}")
    else:
        print(f"your total bill {bill}")
else:
    print("Height invalid")
        
        
        
        
        
        
        
##################################################################
#create a program using maths and f strings and tell us how many days,
# weeks and months we have left if we will live until 80 years.



def days_left(age):
    age_left=80-age
    days=365*age_left
    weeks=52*age_left
    months=12*age_left
    return f"You have {days} days, {weeks} weeks, {months} months remained"
age=int(input("Enter your age"))
print(days_left(age))



print("What is todays age")
years_today=input("Years:")
months_today=input('Months:')
days_today=input('Days:')
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"Your total age today in days {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live = 90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"Your remaining life in days {remaining_days_to_live}")



###############################################

#elif statement:
    
users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("hello admin,would you like to see a status report?")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello ")
        
        
#################################################
#password picker

import string
#pick the adjectives
adjectives=['sleepy','slow','smelly','wet','fat','red','brave','blue','purple']
nouns=['oppenheimer','avengers','thor','loki','hulk','tony','interstellar','tenet']
#pick the words
import random
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(1,100)
#select a special character
special_char=random.choice(string.punctuation)
#create new secure password
password=adjective +noun+special_char +str(number) 
print('Your new pasword is: %s' % password)

#multiple password generator
import random
print("welcome to pwd picker")
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    #select a number
    number=random.randrange(1,100)
    #select a special character
    special_char=random.choice(string.punctuation)
    #create new secure password
    password=adjective +noun+special_char +str(number) 
    print('Your new password is: %s' % password)
    response=input('would you like to generate another password? Type y or n:')
    if response=='n':
        break
    

#####################################################


#write python code to determine the pwd is good or not
 #1. it must have atleast 8 characters  
 #2. it must have 1 upper case letter 
 #3. one lower case letter

def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    for ch in password:
        if ch>='A' and ch<='Z':
            has_upper=True
        elif ch>='a' and ch<='z':
            has_lower=True
        elif ch>='0' and ch<='9':
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
password=input("Enter password:")
if checkPassword(password):
    print("strong password")
else:
    print("weak password")
    
    
    
#########################################################
#write a code to calculate pizza order bill if small pizza 15, medium 20 and large 
#25 .if you want to add pepperoni  for small 2 dollars, pepperoni for mediuum or large pizza 
#3 dollar and extra cheeze for any pizza 1 dollar.
    
            
print("Welcome to Dominoes")
size=input("enter size of pizza(S,M,L):")
pepp=input("Do you want to add pepporoni(Y/N):")
cheeze=input("Do you want to add cheeze(Y/N):")
bill=0
if size=='S':
    print("Small Pizza")
    bill=15
    if pepp=='Y' and cheeze=='Y':
        bill+=3
        print(f"Your bill is {bill}")
    elif pepp=='Y' and cheeze=='N':
        bill+=2
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='Y':
        bill+=1
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='N':
        bill+=0
        print(f"Your bill is {bill}")
    else:
        print("invalid input for pepporoni or cheeze")
elif size=='M':
    print("Medium Pizza")
    bill=20
    if pepp=='Y' and cheeze=='Y':
        bill+=4
        print(f"Your bill is {bill}")
    elif pepp=='Y' and cheeze=='N':
        bill+=3
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='Y':
        bill+=1
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='N':
        bill+=0
        print(f"Your bill is {bill}")
    else:
        print("invalid input for pepporoni or cheeze")
elif size=="L":
    print("Large Pizza")
    bill=25
    if pepp=='Y' and cheeze=='Y':
        bill+=4
        print(f"Your bill is {bill}")
    elif pepp=='Y' and cheeze=='N':
        bill+=3
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='Y':
        bill+=1
        print(f"Your bill is {bill}")
    elif pepp=='N' and cheeze=='N':
        bill+=0
        print(f"Your bill is {bill}")
    else:
        print("invalid input for pepporoni or cheeze")
else:
    print("Invalid Input")

    

            
            
            
            
            
            
            
            
            
        
        
    














