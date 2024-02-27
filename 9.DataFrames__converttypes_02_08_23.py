#9. 02 August 2023

#To check version of pandas
import pandas as pd
pd.__version__

#Create using constructor
#Create pandas dataframe from list
import pandas as pd
technologies=[["Spark",20000,"30 Days"],["Pandas",20000,"40 Days"]]
df=pd.DataFrame(technologies)
print(df)

#Add columns and rows labels to the dataframe
column_names=['Courses','Fees','Duration']
row_labels=['a','b']
df=pd.DataFrame(technologies,columns=column_names,index=row_labels)
print(df)

df.dtypes

############################################
#You can also assign custom data types to columns
#Set custom types to DataFrame

import pandas as pd
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas'],
              'Fee':[20000,12000,35000,10000,23000],
              'Duration':['30Days','40Days','20Days','90Days','45Days'],
              'Discount':[12,34,21.8,10,20]}
df=pd.DataFrame(technologies)
print(df.dtypes)

#COnvert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)

#Change all columns to same type
df=df.astype(str)
print(df.dtypes)

#Change type for one or multiple columns
df=df.astype({'Fee':int,'Discount':float})
print(df.dtypes)

#Convert data type for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#Ignores error
df=df.astype({'Courses':int},errors='ignore')
df.dtypes

#Generates error
df=df.astype({'Courses':int},errors='raise')
df.dtypes

#Converts feed column to numeric type
df=df.astype(str)

























