#  13. 09 August 2023 Wednesday

#Pandas apply function to a column
#Using DataFrame.apply() to apply function add column

import pandas as pd
import numpy as np
data={'A':[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]
      }
df=pd.DataFrame(data)
print(df)

df2=df.apply(lambda x:x+3)
print(df2)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3))
df2

#######################################

#Using .apply function single column

def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)
df['B']

#Apply to multiple columns

df[['A','B']]=df[['A','B']].apply(add_4)
df[['A','B']]

df[['A','B','C']]=df[['A','B','C']].apply(add_4)
df[['A','B','C']]

###########################################

#Apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2

############################################

#apply() function on selected list of multiple columns
df[['A','B']]=df[['A','B']].apply(lambda x:x+10)
df2

############################################

#Using pandas .DataFrame.transform() to apply function column
#Using DataFrame.tansform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)

#########################################
#Using pandas .DataFrame.map() to single column
df['A']=df['A'].map(lambda A:A/2)
print(df)

########################################

#Using numpy function on single column
#Using DataFrame.apply() and [] operator
import numpy as np
df['A']=df['A'].apply(np.square)
print(df)

df['A']=np.square(df['A'])
print(df)

#######################################

#Pandas groupby() with examples

import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas','Hadoop','Spark','Python','NA'],
              'Fee':[20000,12000,35000,10000,23000,24000,25000,22000,1500],
              'Duration':['30Days','40Days','20Days','90Days','45Days','20Days','60Days','45Days','35Days'],
              'Discount':[12,34,21.8,10,20,None,12,15,13]}
df=pd.DataFrame(technologies)
print(df.dtypes)

#Use groupby() to compute the sum
df2=df.groupby(['Courses']).sum()
print(df2)

#Group by multiple columns
df2=df.groupby(['Courses','Duration']).sum()
print(df2)

###########################################

#Pandas get column name from dataframe
import pandas as pd
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas'],
              'Fee':[20000,12000,35000,10000,23000],
              'Duration':['30Days','40Days','20Days',None,np.nan],
              'Discount':[1200,1000,2100,1000,2000]}
df=pd.DataFrame(technologies)
print(df)


#Get the list of all column names from headers
column_headers=list(df.columns.values)
print(column_headers)

###########################################################

#pandas shuffle DataFrame rows
import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas','Oracle','Java'],
              'Fee':[20000,12000,35000,10000,23000,24000,25000],
              'Duration':['30Days','40Days','20Days','90Days','45Days','20Days','60Days'],
              'Discount':[1000,2300,1500,1200,2500,2100,2000]}
df=pd.DataFrame(technologies)
df

#pandas shuffle DataFrame rows
#Shuffle the dataframe rows and return all the rows
df1=df.sample(frac=0.5)
print(df1)

df1=df.sample(frac=0.5)
print(df1)

###############################################
#Create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

###################################################
#Drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)

##################################################
#################################################


##          JOINS--->
#           =========

import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Python','Pandas'],
              'Fee':[20000,25000,22000,30000],
              'Duration':['30Days','40Days','35Days','50Days']
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
df1

technologies2={'Courses':['Spark','Java','Python','Go'],
              'Discount':[2000,3000,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
df2

#Pandas inner join is mostly used join,
#It is used to join two dataframes on indexes
#When indexes dont natch the rows get dropped from bloth dataframe

#Pandas join , by default it will join the table left join
df3=df1.join(df2,lsuffix="_left", rsuffix="_right")
print(df3)

#inner join
df3=df1.join(df2,lsuffix="_left", rsuffix="_right",how='inner')
print(df3)

#Pandas left join dataframe
df3=df1.join(df2,lsuffix="_left", rsuffix="_right",how='left')
print(df3)

#Right join
df3=df1.join(df2,lsuffix="_left", rsuffix="_right",how='right')
print(df3)

##########################################################
#Pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df3)

df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='outer')
print(df3)

##########################################################

#Pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='left')
print(df3)

#Pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='right')
print(df3)

#Inner join

#Pandas merge dataframe
import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Python','Pandas'],
              'Fee':[20000,25000,22000,30000],
              'Duration':['30Days','40Days','35Days','50Days']
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
df1

technologies2={'Courses':['Spark','Java','Python','Go'],
              'Discount':[2000,3000,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
df2

#Using pandas.merge() for inner join
df3=pd.merge(df1,df2)

#####################################################
#Use pandas.concat() to cancat two dataframes
import pandas as pd
df=pd.DataFrame({'Courses':['Spark','Pyspark','Python','Pandas'],
                 'Fee':[20000,25000,22000,24000]
                 })
df1=pd.DataFrame({'Courses':['Pandas','Hadoop','Hyperion','Java'],
                  'Fee':[25000,25200,24500,24900]
                  })

#Use pandas.concat() to cancat two dataframes
data=[df,df1]
df2=pd.concat(data)
df2

data=[df,df1]
df3=pd.concat(data).reset_index(drop=True)
df3

################################################

#Concatenate multiple dataframes using pandas.concat
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,24000]})
df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})
df2 = pd.DataFrame({'Duration':["30days","40days","35days","60days","55days",],
                  'Discount':[1000,2300,2500,2000,3000]})

#Appending multiple dataframes
df3=pd.concat([df,df1,df2])


































































































































































































































