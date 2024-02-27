# 14. 10 August 2023

###                     ASSIGNMENTS ON NUMPY                           ###
#                       ====================                             #

'''
1.Write a numpy program to get a numpy version and show the numpy
'''
import numpy as np
print(np.__version__)


'''
2.Write a numpy program to test whether none of the elements of a given
arraya are zero.
'''
import numpy as np
x=np.array([1,2,3,4])
print(x)
print(np.all(x))
#---> np.all()  Used to find if zero is present or not in array

x=np.array([0,1,2,3,4])
print(x)
print(np.all(x))


'''
3.Write a numpy program to test if any of the elements of given array 
are non zero.
'''
import numpy as np
x=np.array([1,0,0,0,0])
print(np.any(x))
#---> np.any()  Used to check if any element in the array is not a zero

x=np.array([0,0,0,0,0])
print(np.any(x))


'''
4.Write a numpy program to test a given array element wise for 
finiteness (not infinity or not a number).
'''
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print(a)
print(np.isfinite(a))


'''
5.Write a numpy program to test a given array element wise for 
NaN of a given array.
'''
import numpy as np
a=np.array([1,2,np.nan,np.inf])
print(a)
print(np.isnan(a))


'''
6.Write a numpy program to create elemet wise comparison  (greater,
greater equal,less and less equal) of two given arrays.
'''
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print(x)
print(y)
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))


'''
7.Write a numpy program to create a 3x3 identity matrix.
'''
import numpy as np
array_2D=np.identity(3)
print(array_2D)


'''
8.Write a numpy program to generate a random number betweeen 0 and 1
'''
import numpy as np
rand_num=np.random.normal(0,1,1)
print(rand_num)


'''
9.Write a numpy program to create a 3x4 array and iterate over it
'''
import numpy as np
a=np.arange(10,22).reshape(3,4)
print(a)
for x in np.nditer(a):
    print(x,end=" ")
    print()
    

'''
10.Write a numpy program to create vector of length 10 with value evenly
distributed between 5 and 50.
'''
#  np.linspace --> called as linespace
#  ( start, end , length of vector)
import numpy as np
v=np.linspace(5,49,10)
print(v)


'''
11.Write a numpy program to create a 3x3 matrix with values ranging 
from 2 to 10.
'''
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)


'''
12.Write anumpy program to reverse an array
 (the first element becomes the last)
'''
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
print(np.flip(x))

x=np.arange(1,10)
x=x[::-1]
print(x)


'''
13.Write a numpy program to compute a multiplication of two given 
matrices.
'''
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print(p)
print(q)
result1=np.dot(p,q)
print(result1)


'''
14.Write a numpy program to compute the cross product of two given
matrices.
'''
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
result1=np.cross(p,q)
result2=np.cross(q,p)
print(result1)
print(result2)


'''
15.Write a numpy program to compute the determinant of a given square 
array.
'''
import  numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))

print(LA.det(a))

'''
16.Write a numpy program to compute the Eigen Values and right eigen 
vectors of a given square array.
'''
import numpy as np
m=np.mat('3 -2;1 0')
print('a\n', m)
w,v=np.linalg.eig(m)
print('EigenValues:',w)
print("EigenVEctors:",v)


'''
17.Write a numpy program to compute the inverse of given matrix.
'''
import numpy as np
m=np.array([[1,2],[3,4]])
print(m)
print(np.linalg.inv(m))


'''
18.Write a numpy program to add,subtract,multiply and divide

'''


































































