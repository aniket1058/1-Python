# 14. 10 August 2023

###                             NUMPY--->                                 ###
#                               =========                                    #

'''
What is Numpy?
The numpy librarry is popular open source python library used
for scientific computing applications and it stands for Numerical Python
which is consisting of multidimentional arrays
objects and a collection of routines for processing those arrays'
'''

#########

'''
While python list can contain different data types within a single list,
all the elements in NumPy array should be homogeneous.
'''

#Arrays in numpy
#Create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)

#Create a multidimensional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#Represent the  inimum dimensions
#Use ndmin param to specify how many minimum dimension you want to create
# an array with Minimum Dimension
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

#Change the Data Type 
#Dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)

#Get the dimensions of array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

#Finding the size of each item in the array
arr=np.array([10,20,30])
print(arr.itemsize)

#Get the Data type of each array item
arr=np.array([10,20,30])
print(arr.dtype)    #int32

#Get the shape and size of the array
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array Size :",arr.size)
print("Shape :",arr.shape)

#Create a sequence of integers using arange()
#from 0 to 20 with steps of 3
arr=np.arange(0,20,3)
print("A sequential array with steps of 3:\n",arr)

#Acces single element using index

arr=np.arange(11)
print(arr)

print(arr[2])

print(arr[-2])

##############

#Multidimensional array indexing
#Access multidimensional array element
#Using array indexing
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)

print(arr.shape)

print(arr[1,2])
#O/P-->  50
print(arr[1][2])
#O/P-->  50

print(arr[1,-1])
#O/P-->  30

###################

#Access array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)

x=arr[-2:3:-1]
print(x)

x=arr[-2:10]
print(x)

################

#Indexing in Numpy
multi_arr=np.array([[10,20,10,40],[40,50,60,90],[60,10,70,80],[30,90,40,30]])
arr

#Slicing array
#For multi dimensional numpy arrays
#you can access the elements as below

multi_arr[1,2] #To access the value at row 1 and column 2
multi_arr[1,:] #To access the value at row 1 and all columns
multi_arr[:,1] #To access the value at all row and column 1

x=multi_arr[:3,::2] #Column from 0 to 3 in all selected rows in step of 2
print(x)

#Integer array indexing

#Integer array indexing allows the selection of arbitrary items
arr=np.arange(35).reshape(5,7)
print(arr)

#########################

#Boolean array indexing
'''
This advanced indexing occurs when an object is an array object of 
Boolean types such as may be returned from comparison operators .
Use this method when we want to pick elements from the array which 
satisfy some conditions
'''
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True]) #only 0th index row will not print
wanted_rows=arr[rows, : ]
print(wanted_rows)

######################

#Convert NumPy arrays to python list
#Convert one dim. array to list

#Create array
array=np.array([10,20,30,40])
print("Array:",array)
print(type(array))

#Convert list
lst=array.tolist()
print("List:",lst)
print(type(lst))

#Convert Multi Dimensional Array to list
#Create array
array=np.array([[10,20,30,40],[50,60,70,80],[60,40,20,10]])
print("array:",array)

lst=array.tolist()
print("list:",lst)
print(type(lst))

#######################

#Convert Python list to ARRAY
#1.numpy.array()
#2.numpy.asarray()

list=[20,40,60,80]

#Convert array
array=np.array(list)
print("Array:",array)

array=np.asarray(list)
print("Array:",array)

########################

#Numpy array properties


#Shape
array=np.array([[1,2,3],[4,5,6]])
print(array.shape)

#Resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)

#######################

#Operations using numpy
#This are divided into three main categories:
    
'''
1.Fourier Transform and Shape Manipulation
2.Mathematical and Logical Operations
3.Linear Algebra and Random number Generation
'''
    
#Arithmetic Operations
















































































