
#9. 02 August 2023

###########            PYTHON FOR DATA SCIENCE            ###############
#                      =======================                          #


#Series
'''A series is used to model one dimensional data, similar to a list in 
 python .  The series object also have a few more bits of data, including
  an #index and name.
  '''
import pandas as pd
songs2=pd.Series([123,34,22,39],name='counts')
#it is easy to ispect the index of a series (or data)
songs2.index

#The index can be string based as well
#in which case pandas indicates that the data types for the index is onject

songs3=pd.Series([123,34,22,39],name='counts',index=['John','Paul','George','Ringo'])
songs3.index
songs3

#The NaN value (Null value)
#Stands for Not A Number and is usyually ignored in arithmetic 
# operations.(Similar to Null in SQl)
# If you load data from csv file an empty value for an otherwise

#Numeric column will be NaN
import pandas as pd
f1=pd.read_csv('c:/1-Python/age.csv') #Absolute path if WD is not selected
f1


import pandas as pd
f2=pd.read_excel('Bahaman.xlsx') #Relative path if WD is selected
f2

#############################################
#The series object behaves similarly to a numpy array

import numpy as np
numpy_ser=np.array([123,34,22,39])
songs3[1]
numpy_ser[1]
songs3.mean()
numpy_ser.mean()

########################################
#The PANDA SERIES DATA STRUCTURE provides support for the basic crud
# operations-create, read, update and delete
#CReation

george = pd.Series([10,7,1,22],
index = ['1968','1769','1970','1970'],
name = 'George Songs')
george

'''
The previous example illustrates an interesting 
feature of pandas-the index value are strings and they
are not unique. this can cause some confusion, but can also be useful 
when duplicate index items are needed.
'''
####################################
#Reading
#to read or select the data from series
george['1968']

george['1970']

#We can iterate over data in series as well , when iterating over series
for item in george:
    print(item)
    
#######################################
#Updating
#Updating
#Updating values in a series can be little tricky as well
#To update a value for a given index label,the standard
#index assignment operation works
george['1969']=68
george['1969']

#Deletion
#Deletion
# The del statement appers to have
# problems with duplicate index
s=pd.Series([2,3,4], index=[1,2,3])
del s[1]
s

##########################################
#convert Types
#string use .astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#Note that this will fail with NaN datetime use pd.to_dateline
import pandas as pd
songs_69=pd.Series([3,None,11,9],index=['John','Paul','George','Ringo'],name='Counts')                                
songs_69.dtypes

#dtype('float64)
#pd.to_numeric(songs_69.apply(str))
#There will be error
pd.to_numeric(songs_69.astype(str),errors='coerce')

#if we pass errors='coerce'
#We can see that it supports many formats

songs_69.dtype

#Dealing with none
#The fillna. method will replace will replace them with given value
songs_69.fillna(-1)

#NaN values can be dropped using .dropna
songs_69.dropna()


###############################################

#Append,combining and joining two series
songs_68=pd.Series([7,16,21,39],index=['Ram','Sham','Ghanshyam','Krishna'],name='Counts')
#to concatenate simply use the .append function
songs=songs_69.append(songs_68)

################################################

#Plotting two series
#Normal Graph
import matplotlib.pyplot as plt
fig=plt.figure()
songs_68.plot()
plt.legend()

#################################################
#Bargraph
fig=plt.figure()
songs_68.plot(kind='bar',title='ABC')
songs_69.plot(kind='bar', color='r')
plt.legend()

###############################################
#Histogram
import numpy as np
data=pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()



