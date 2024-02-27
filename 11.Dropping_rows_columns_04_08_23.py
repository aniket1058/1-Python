#11. 04 August 2023
####                 DROPPING  ROWS AND COLUMNS                    ##############

import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
df=pd.DataFrame(technologies,index=row_labels)
df
###################################

#Drop DataFrame Rows and Columns
df=pd.DataFrame(technologies, index=row_labels)
df

#Delete rows by labels
df1=df.drop(['r1','r2'])
df1

#Delete rows by index/position:
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#Delete Rows by Index Range:
df1=df.drop(df.index[2:])

#When we have the default index for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3])  #









####################################

df=pd.DataFrame(technologies)
df

#Drop Column by name
#Drop 'Fee' column
df2=df.drop(['Fee'],axis=1)
print(df2)

#Explicitly using parameter name 'labels'
df2=df.drop(labels=['Fee'], axis=1)
df2

#Alternatively you can also use columns instead of 'labels'
df2 = df.drop(columns=["Fee"],axis=1)


#Drop Columns by Index
print(df.drop(df.columns[1],axis=1))

df = pd.DataFrame(technologies)

# Using inplace = True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

######################################

df = pd.DataFrame(technologies)

#Drop Two or More Columns by label Name
df2 = df.drop(["Courses","Fee"],axis =1)
print(df2)

######################################

#Drop 2 or  more columns by index
df = pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

#####################################

#Drop columns from list of columns
df = pd.DataFrame(technologies)
df.columns
lisCol=['Courses','Fee']
df2=df.drop(lisCol,axis=1)
print(df2)


##############################################################
##############################################################


#Pandas Select Rows by Index use of iloc:
#                                   ====

import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
df=pd.DataFrame(technologies,index=row_labels)
df

#df.iloc[startrow:endrow,startcolumn:endcolumn]

df=pd.DataFrame(technologies,index=row_labels)
#Below are quick examples

df2=df.iloc[:,0:2]
df2
#This line uses the slicing operation to get DataFrame items by index
#The first slice [:] indicates to return all rows
#The secomd slice specifies that only columns between 0 and 2 (excluding 2)
# should be returned

df2=df.iloc[0:2, :]
df2


#Slicing Special rows and columns using iloc
df3=df.iloc[1:2,1:3]
df3

#Select rows by Integer Index
df2=df.iloc[2]          #Select row by index
df2

df2 = df.iloc[[2,3,6]]   #Select Rows by index list
df2 = df.iloc[1:5]       #Select Rows by integer index range
df2 = df.iloc[:1]        #Select First row
df2 = df.iloc[:3]        #Select first 3 rows
df2 = df.iloc[-1:]       #Select last row
df2 = df.iloc[-3:]       #Select last 3 row
df2 = df.iloc[::2]       #Select alternate rows


###############################################
#Select rows by index labels using loc
#                                  ===

df2=df.loc['r2']               #Select row by label
df2=df.loc[['r1','r2','r6']]   #Select row by index label
df2=df.loc['r1':'r5']          #Select rows by label undex range
df2=df.loc['r1':'r5':2]        #


########################################

#Pandas select columns by Name or Index


#Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
##Select multiple columns
df2=df.loc[:,['Courses','Fee','Duration']]

#Select random columns
df2=df.loc[:,['Courses','Fee','Duration']]

#Select column betn two columns
df2=df.loc[:,'Fee':'Discount']

#Select column  by range
#All the columns upto Duration
df2=df.loc[:,'Duration':]

