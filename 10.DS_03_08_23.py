#10.     03 August 2023


import pandas as pd
#Create DataFrame from Dictionary
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas'],
              'Fee':[20000,12000,35000,10000,23000],
              'Duration':['30Days','40Days','20Days','90Days','45Days'],
              'Discount':[12,34,21.8,10,20]}
df=pd.DataFrame(technologies)
df

#############################
#Convert DataFrame to CSV
df.to_csv('data_file.csv')
df.to_excel('data_file.xlsx')

#############################
#Create DataFrame from CSV file

df=pd.read_csv('data_file.csv')
df

##############################
#Pandas DataFrame Basic Operations

import pandas as pd
import numpy as np
technologies=({'Courses':['Spark','Pyspark','Hadoop',None,'Pandas'],
              'Fee':[20000,12000,np.nan,10000,23000],
              'Duration':['30Days','40Days','20Days','90Days',''],
              'Discount':[12,34,21.8,10,20]})
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies, index=row_labels)
df
print(df)

#######################################
#DataFrame Properties:
df.shape
#(5,4)
df.size
#20
df.columns
df.columns.values
df.index
df.dtypes
    
####################################
#Accessing one column contents
df['Fee']

#Accessing two columns contents
df[['Fee','Duration']]

#Select certain rows and assign it to another DataFrame
df2=df[3:]
df2

#Access certain cell from column 'Duration'
df['Duration'][3]

#Subtracting specific value from column
df['Fee']=df['Fee']-1500
df['Fee']

#Adding specific value from column
df['Fee']=df['Fee']+1500
df['Fee']

#Pandas to manipulate DataFrames
#Describe DataFrame
#Describe Dataframe for all Numeric columns
df.describe()
#It will show 5 number summary

################################

#rename() -Rename Pandas DF columns
df=pd.DataFrame(technologies,index=row_labels)

#Assign new header by setting new column names
df.columns=['A','B','C','D']
df

###############################

#Rename column name using rename() method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'}, axis=1)
df2=df.rename({'C':'c3','D':'c4'}, axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})


df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'}, axis=1)
df2=df.rename({'C':'c3','D':'c4'}, axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2','C':'c3','D':'c4'})








