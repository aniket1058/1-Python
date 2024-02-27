#10.  03 August 2023
##################       SERIES ASSIGNMENTS        #####################
#                        ==================                            #

'''
1.Write a pandas program to create aand display a one dimensional array like 
containing an array of data
'''
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)

'''
2.Write a pandas program to convert a panda module series to python list
and its types
'''
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print('Pandas Series and type')
print(ds)
print(type(ds))
print('Convert Pandas Series to python list')
print(ds.tolist())
print(type(ds.tolist()))


'''
3.Write a pandas program to add ,subtract ,multiple and 
sample Series=[2,4,6,8,10],[1,3,5,7,9]
'''
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print('Add two series')
print(ds)
print('Subtract two Series')
ds=ds1-ds2
print(ds)
print('Multiply two series')
ds=ds1*ds2
print(ds)
print('Divide series 1 by series 2')
ds=ds1/ds2
print(ds)


'''
4.Write a panda program to compare the elements of the series
sample series=[2,4,6,8,10],[1,3,5,7,10]
'''
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,10])
print('Series1')
print(ds1)
print('Series2')
print(ds2)
print('Compare elements:')
print('Equals:')
print(ds1==ds2)
print('Greater than:')
print(ds1>ds2)
print('Less than:')
print(ds1<ds2)


'''
5.Write a pandas program to convert a dictionary to a Pandas Series.
Original Dictionary:
{'a':100,'b':200,'c':300,'d':400,'e':800}
'''
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print('Original Dictionary')
print(d1)
new_series=pd.Series(d1)
print('Converted Series')
print(new_series)


'''
6.Write a pandas program to convert a Numpy array to a Panda Series
'''
import pandas as pd
import numpy as np
n_a=np.array([10,20,30,40,50])
print('Numpy Array:')
print(n_a)
new_series=pd.Series(n_a)
print('Converted Panda Series:')
print(new_series)


'''
7.Write a pandas program to change the datatype of given a column or
a series
'''
import pandas as pd
s1=pd.Series(['100','200','Python','300.12','400'])
print('Original Data Series:')
print(s1)
print('Change the solid data type to numeric:')
s2=pd.to_numeric(s1,errors='coerce')
print(s2)


'''
7.Write a pandas program to convert a the fist column of dataframe as series
'''
#For name of columns use 'loc' and for index of column use 'iloc'
#Converting dataframe into series, iloc and loc

import pandas as pd
d={'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df=pd.DataFrame(data=d)
print('Original Dataframe:')
print(df)
s1=df.iloc[:,0]
print('\n1st column as a series:')
print(s1)


'''
###############################################################
'''
import pandas as pd
s=pd.Series([['Red','Green','White'],['Red','Black',],['Yellow']])
print('Original Series of List')
print(s)
s=s.apply(pd.Series).stack().reset_index(drop=True)
print('One Series')
print(s)


import pandas as pd
s=pd.Series([['Red','Green','White'],['Red','Black',],['Yellow']])
print('Original Series of List')
print(s)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print('One Series')
print(s3)

'''
##############################################################
'''

'''
9.Write a Pandas program to add some data to an existing Series
'''
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print('Original Series of List')
print(s)
print('\nData series afterv adding some data:')
new_s=pd.concat([s,pd.Series([500,'php'])], ignore_index=True)
print(new_s)


'''
10.Write a pandas program to to sort a given series
'''
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print('Original Series of List')
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)


'''
11.Write a pandas program to change the order of index of a given series
'''
import pandas as pd
s=pd.Series([1,2,3,4,5],['A','B','C','D','E'])
print('Original Series of List')
print(s)
s=s.reindex(['B','A','C','D','E'])
print('Data series after changing the order of index')
print(s)







