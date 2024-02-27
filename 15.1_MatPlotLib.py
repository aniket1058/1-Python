#Date ==> 11/08/2023

#########       Matplotlib     ################
#            =================               #

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()


#Multiline plots
import matplotlib.pyplot as plt
x =range(2,5)
plt.plot(x, [xi*1.5 for xi in x],color='g')

plt.plot(x, [xi*3.0 for xi in x],color='r')

plt.plot(x, [xi/3.0 for xi in x],color='b')

plt.show()


#############################################
#Grid,axes, and labels
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()

#####################
#Handling axes :=>
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

plt.axais()  #shows the current axis limits values

plt.axis([0,5,-1,13])  # set new axes limits
# [xmin , xmax , ymin , ymax ]
# [ 0 , 5 , -1 , 13]

plt.show()

##########################
#Adding labels ::=>
import matplotlib.pyplot as plt
plt.xlabel("This is the X axis")
plt.ylabel("This is the Y axis")
plt.show()

##################################
##################################

#Adding a Titles
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple Plot')
plt.show()

#Matplotlib provides a simple function ,plt.title()

#################################
#Adding a legend

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5, label='Normal')
plt.plot(x, x*3.0, label='Fast')
plt.plot(x, x/3.0, label='Slow')
plt.legend()
plt.show()

####################################
#Control colors
#Color abbreviations
'''
b  Blue 
c  Cyan
g  Green
k  Black
m  Magenta
r  Red
w  White
y  Yellow

'''
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')
plt.show()

####################################

#Specifying styles in multiline plots

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c')
plt.show()

###################################

#Control line styles
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show()

###################################

'''
   Style abbrevation
    -     solid line
   --     double dash
   -.      dash dot 
   :      dotted line
      
'''
'''




'''
'''




'''

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()

######################################

#Histogram Charts
import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.grid()
plt.show()

####################

#Bar Plot
import matplotlib.pyplot as plt
import numpy as np
plt.bar([1,2,3],[3,2,5])
plt.show()

########################
#Scatter plot(Also called as Bivarient Analysis)

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

##
size = 50*np.random.randn(1000)
colors = np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()

##########################

#Adding Text
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(-4,4,1024)
Y=.25*(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard Minimum')
plt.plot(X,Y,c='k')
plt.show()

#########################
#How to use Seaborn for Data Visualization
# pip install seaborn
#Seaborn has 18 in built databases that can be found using the 
# following commands

import seaborn as sns
import pandas
import matplotlib.pyplot as plt

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

##
#Count Plot
'''
countplot is used to plot the frequency of different categories
'''

sns.countplot(x='sex', data=df)
#x=name of the column
#data= the dataframe

sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

#hue-->name of categorical column to split the bars
#palette--> The color palette to be used

#########################################################

#KDE plot
#KDE(Kernel Density Estimate) is used to plot the distribution of
# continuous data

sns.kdeplot(x='age',data=df,c='k')
#x-->name of the column

sns.displot(x='age',kde=True,bins=6,data=df)

  #kde-->It is set to False by default
  #bins-->The number of bins/bars
  
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)


###############################
#Scatter plot 
'''
For this plot And the plots below. 
We will be working With the iris data set.
The iris data set contains. Data set, Data related. 
'''
df=sns.load_dataset('iris')
df.head()

#scatter plot help understand corelation between data
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')


########################################

#     JOINT PLOT    #

#A joint plot is also used to plot the corelation between data

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

#Pair Plot
sns.pairplot(df)








































































































