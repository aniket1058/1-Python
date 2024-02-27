#10   03 August 2023

'''
loan.csv
'''
import pandas as pd
import numpy as np
df=pd.read_csv('loan.csv')
df
df.dtypes

df.describe()

df.shape
#(39717,111)
df.size
#4408587
df.columns
df.columns.values
df.index
df.dtypes


df2=df[10:]
df2

#For 1 column
s=df['loan_amnt']
s

#For 2 columns
d=df[['loan_amnt','term']]
d

#certain cell
df['term'][8]

#Subtracting values
df['loan_amnt']=df['loan_amnt']-500
df['loan_amnt']


#Adding values
df['loan_amnt']=df['loan_amnt']+500
df['loan_amnt']


###rename()
##rename the specific column 
df.rename(columns = {"id": "id's"},  inplace = True)
df
df2=df.iloc[2] #select row by index
df2
df2=df.iloc[:,0:2]
df2
df2=df.iloc[0:2, :]
df2


#Slicing Special rows and columns using iloc
df3=df.iloc[1:2,1:3]
df3

df2=df.iloc[[2,3,6]]#select rows by index list
df2=df.iloc[1:5] # select rows by integer index range
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]# select first 3 rows
df2=df.iloc[-1:]# select last row
df2=df.iloc[-3:]# select last 3 rows
df2=df.iloc[::2]# select alternate rows

df2=df.loc[6]               #Select row by label
df2=df.loc[[1,2,6]]   #Select row by index label
df2=df.loc[1:5]          #Select rows by label undex range
df2=df.loc[1:5:2]


df2=df.loc[:,['loan_amnt','term','int_rate']]

df2=df.loc[:,'term':'int_rate']


df2=df.loc[:,'int_rate':]



'''
bank_data.csv
'''
import pandas as pd
import numpy as np
df3=pd.read_csv('bank_data.csv')
df3
df3.dtypes

df3.describe()

df3.shape
#(45211, 32)
df3.size
#1446752
df3.columns
df3.columns.values
df3.index
df3.dtypes

df4=df3[10:]
df4

#For 1 column
s=df3['pdays']
s

#For 2 columns
d=df3[['age','balance']]
d

#certain cell
df3['duration'][8]

#Subtracting values
df3['balance']=df3['balance']-500
df3['balance']


#Adding values
df3['balance']=df3['balance']+500
df3['balance']

###rename()
##rename the specific column 
df3.rename(columns = {"id": "id's"},  inplace = True)
df3
df4=df3.iloc[2] #select row by index
df4
df4=df3.iloc[:,0:2]
df4
df4=df3.iloc[0:2, :]
df4


#Slicing Special rows and columns using iloc
df4=df3.iloc[1:2,1:3]
df4

df4=df3.iloc[[2,3,6]]#select rows by index list
df4=df3.iloc[1:5] # select rows by integer index range
df4=df3.iloc[:1]#select first row
df4=df3.iloc[:3]# select first 3 rows
df4=df3.iloc[-1:]# select last row
df4=df3.iloc[-3:]# select last 3 rows
df4=df3.iloc[::2]# select alternate rows

df4=df3.loc[6]               #Select row by label
df4=df3.loc[[1,2,6]]   #Select row by index label
df4=df3.loc[1:5]          #Select rows by label undex range
df4=df3.loc[1:5:2]


df4=df3.loc[:,['default','housing','duration']]

df4=df3.loc[:,'housing':'duration']


df4=df3.loc[:,'housing':]


'''
crime_data.csv
'''
import pandas as pd
import numpy as np
df5=pd.read_csv('crime_data.csv')
df5
df5.dtypes

df5.describe()

df5.shape
#(50, 5)
df5.size
#250
df5.columns
df5.columns.values
df5.index
df5.dtypes

df6=df5[10:]
df6

#For 1 column
s3=df5['Murder']
s3

#For 2 columns
df6=df5[['Murder','Assault']]
df6

#certain cell
df5['UrbanPop'][8]

#Subtracting values
df5['Assault']=df5['Assault']-30
df5['Assault']


#Adding values
df5['Assault']=df5['Assault']+25
df5['Assault']

###rename()
##rename the specific column 
df5.rename(columns = {"id": "id's"},  inplace = True)
df5
df6=df5.iloc[2] #select row by index
df6
df6=df5.iloc[:,0:2]
df6
df6=df5.iloc[0:2, :]
df6


#Slicing Special rows and columns using iloc
df6=df5.iloc[1:2,1:3]
df6

df6=df5.iloc[[2,3,6]]#select rows by index list
df6=df5.iloc[1:5] # select rows by integer index range
df6=df5.iloc[:1]#select first row
df6=df5.iloc[:3]# select first 3 rows
df6=df5.iloc[-1:]# select last row
df6=df5.iloc[-3:]# select last 3 rows
df6=df5.iloc[::2]# select alternate rows

df6=df5.loc[6]               #Select row by label
df6=df5.loc[[1,2,6]]   #Select row by index label
df6=df5.loc[1:5]          #Select rows by label undex range
df6=df5.loc[1:5:2]


df6=df5.loc[:,['Murder','Assault','Rape']]

df6=df5.loc[:,'Assault':'Rape']

df6=df5.loc[:,'UrbanPop':]












