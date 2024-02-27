# 8. 01 August 2023

############             SHALLOW COPY AND DEEP COPY        ############
#                        ==============================                   #

#Assignment Operation
#This will only create a new variable with the same reference
#Modifying
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)

###################################

####              SHALLOW COPY---
#                 ============
                  

#One level deep . Modifying on level 1 does not affect the other list
#Use copy.copy()

import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
#not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)

#Drawbacks
#But with nested objects modifying on level 2 or deeper does affect the other

import copy
list_a=[1,2,3,4,5], [6,7,8,9,10]
list_b=copy.copy(list_a)

#Affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

#o/p:([-10, 2, 3, 4, 5], [6, 7, 8, 9, 10])
#    ([-10, 2, 3, 4, 5], [6, 7, 8, 9, 10])

##############################################

###          DEEP COPY        ##########


import copy
list_a=[[1,2,3,4,5], [6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#does not Affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































