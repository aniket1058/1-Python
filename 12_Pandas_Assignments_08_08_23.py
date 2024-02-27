# 12 08 August 2023

'''
1.Write pandas program to create dataframe from a dictionary and display
Sample Data:{'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
'''
import pandas as pd
abc={'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
df=pd.DataFrame(abc)
print(df)


'''
2.Write pandas program to create and display a dataframe from a specified
Sample python dictionary data and list labels:
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
           labels=['a','b','c','d','e']
           
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df2=pd.DataFrame(exam_data,index=row_labels)
print(df2)


'''
3.Write pandas program to display summary of basic info about the dataframe 
and its data.
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
           labels=['a','b','c','d','e']

'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
df=pd.DataFrame(exam_data)
df.describe()


'''
4.Write pandas program to to get the first  3 rows of given dataframe
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df.iloc[:3])


'''
5.Write a pandas progarm to select the 'name ' and 'score' column from the 
dataframe
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df[['name','score']])


'''
6.Write a pandas program to select the specified columns and 
rows from a dataframe
Select specific columns and rows:
    
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df2=df.iloc[2:4,1:3]
print(df2)


'''
7.Write a pandas program to select rows where the no. of attempts of 
examination is greater than 2
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print('Attempts in examination greater than 2:')
print(df[df['attempts']>2])

'''OR'''

df2=df.loc[df.attempts>2]
print(df2)


'''
8.Write a pandas program to count the number of rows and columns in 
dataframe.
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df.shape
rows_count=len(df.index)
print(rows_count)
rows_count=len(df.axes[0])
print("Total Rows:"+str(rows_count))
column_count=len(df.axes[1])
print(column_count)

row_count=df.shape[0]   
print(row_count)
col_count=df.shape[1]
print(col_count)


'''
9.Write pandas program to select the row where the score is missing
i.e. NaN
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,np.nan,21,np.nan],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df2=(df[df['score'].isnull()])
print(df2)

'''
10.Write a pandas program to select rows the score is between 15 and 20
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df2=df[df['score'].between(15,20)]   ##  20 inclusive
print(df2)


'''
11.Write pandas program to select the rows where the number of attempts 
in the examination is less than 2 and score greater than 15
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df2=df[(df['score']>15) & (df['attempts']<2)]   
print(df2)


'''
12.Write a panda program to change the score in row d to 11.5
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df.loc['d','score']=11.5    #'d' id row and 'score' is column
print(df)


'''
13.Write a pandas program to calculate the sum of the examination
attempts  by the students.
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df['attempts'].sum())


'''
14.Write pandas program to calculate mean of all students score
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df['score'].mean())

df.describe()


'''
15.Write a pandas program to append new row 'k' to dataframe with given
values for each column
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df.loc['k']=['Suresh',22,3,'No']
print(df)


'''
16.Write a pandas program to to sort the dataframe first by 'name'
in descending order ,then by 'score 'in ascending order.
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df=df.sort_values(by=['name'] ,ascending=[False])
print(df)
df=df.sort_values(by=['score'] ,ascending=[True])
print(df)


'''
17.Write pandas program to replace qualify column content values yes and
no with true and false
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df['qualify']=df['qualify'].map({'Yes':True,'No':False})
print(df)

'''OR'''

df.qualify=df.qualify.map({'Yes':True,'No':False})
print(df)


'''
18.Write a pandas program to change name 'Ganesh' to 'James' in name 
column of the dataframe
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)

df.name=df.name.replace('Ganesh','James')
print(df)

'''OR'''

df['name']=df['name'].replace('Ganesh','James')
print(df)


'''
19.Write a pandas program to insert a new column to
a existing dataframe
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
color=['Red','Orange','Blue','Yellow','Black']
df['color']=color
print(df)


'''
20.Writea pandas program to iterate over rows in a
dataframe
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,np.nan,21,20],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df
for index,row in df.iterrows():
    print(row['name'],row['score'])
















