# -*- coding: utf-8 -*-
"""
Numpy

Complex Numerical Operations
>> Origin of Numpy -- Numeric Library -- Jim Hugunin
>> Numpy ----> Travis Oliphant & others 2005
Open Source and Freeware
>> Written in Python and C
>> Fundamental Data Type :  nd Array
object of class ndimensional array (ndarray)
"""


import numpy as np

a=np.array([10,20,30])
b=np.array([1,2,3])


def dot_product(a,b):
    result=0
    for i,j in zip(a,b):
        result+=i*j        
    return result
dot_product(a,b)

import time
start_time=time.time()
for i in range(10000):
    dot_product(a,b)
end_time=time.time()
print(f"Time taken for traditional dot product calculation is {end_time-start_time}")

# or 
from datetime import datetime
start_time=datetime.now()
for i in range(10000):
    dot_product(a,b)
end_time=datetime.now()
print(f"Time taken for dot product is {end_time-start_time}")

# or
from datetime import datetime
start_time=datetime.now()
c=np.dot(a,b)
print(c)
end_time=datetime.now()
print(f"Time taken for dot product using Numpy is {end_time-start_time}")


# Q1- A boy is charged 3$ and Girls *$ for worskhop. 2200 attded the seesion
# and total 10100$ were collected. FInd the number of boys and girls
import numpy as np
a=np.array([[1,1],[3,8]])
b=np.array([2200,10100])
np.linalg.solve(a,b)


# Array:
# -------
# An indexed collection of homogeneous data elements

# How to create array in python
# 1. By using Numpy Module
# 2. By using Array Module (Much Library support is not there)
import array
a=array.array('i',[1,2,3]) # i represests int
print(type(a))
for x in a:
    print(x)


import numpy as np
a=np.array([1,2,3]) 
print(type(a))
for x in a:
    print(x)


# Python List Vs Numpy nd array

# 1. Both are mutable
# 2.Both can be use to store data
# 3. The order is preserved so, can be indexed and sliced

# Difference:
# 1. List is  Inbuilt in python while need to seperatly import Numpy
# 2. List can have heterogenous elements while Numpy can not have
# 3. All operation are not supported
# e.g Vector operation on list not possible
l=[10,20,30]
l+2 #TypeError: can only concatenate list (not "int") to list
l*2 #[10, 20, 30, 10, 20, 30]
a=np.array([10,20,30])
a+2 #array([12, 22, 32])
a*2 #array([20, 40, 60])

# 4. Numpy Array consume less memory than list
# e.g. 
import numpy as np
import sys
a=list(range(30))
b=np.array(a)
print('The size of list:',sys.getsizeof(a))
print('The size of ndarray:',sys.getsizeof(b))

# 5. Numpy array operations are fasters
# 6. Numpy array are convenient to use
# =============================================================================
# How to create Numpy Arrays
# 1.array()
# 2.arange()
# 3.linspace()
# 4.zeros()
# 5.ones()
# 6.full()
# 7.eye()
# 8.identity()
# 9.empty()
# 10. numpy.random library
#             1.randint
#             2.rand
#             3.uniform
#             4.randn
#             5.normal
#             6.shuffle
#             7.Choice
# =============================================================================
# 1.Array

import numpy as np

help(np.array)


l=[10,20,30]
type(l)

a=np.array(l)
type(a)
a.ndim #-- To know dimension of array
a.dtype #-- To know data type of element

## 2 D array Creation

lst=[[10,20,30],[40,50,60],[70,80,90]]

a=np.array(lst)
a.ndim
a.shape
a.size
len(a)


# 1 D array from tuple

a=np.array((1,2,3))

a=np.array(('John','Tim','Tom'))
a.dtype


## Change Data type


a=np.array(['10','20','a'])
print(a)

a=np.array([10,20,30.5])
print(a)

a=np.array([10,20,30.5],dtype=int)
print(a)

a=np.array([10,20,30.5],dtype=float)
print(a)

a=np.array([10,20,30.5],dtype=bool)
print(a)

a=np.array([10,20,30.5,0],dtype=bool)
print(a)

a=np.array([10,20,30.5,0],dtype=complex)
print(a)

a=np.array([1,2,True,'John'],dtype=object)
print(a)

a=np.array([''])


# =============================================================================
# # Using Arange function
# =============================================================================

a=np.arange(10)
a.dtype

a=np.arange(1,11)
a.dtype

a=np.arange(1,11,2)
a.dtype

a=np.arange(1,10,2,dtype=float)
a.dtype


# =============================================================================
# # Linspace()
# # --------------
# =============================================================================
np.linspace(0,1) # Default 50 values
np.linspace(0,1).shape


np.linspace(0,1,3)
np.linspace(0,1,4)


np.linspace(1,100,10,dtype=int)

# array([  1,  12,  23,  34,  45,  56,  67,  78,  89, 100])


# =============================================================================
# zeros(shape,dtype=float,order='C',*,like=None)
# 
# =============================================================================

np.zeros(5)
np.zeros((5,0))
np.zeros((5,2))

# =============================================================================
# ones()
# =============================================================================
np.ones(10)

np.ones((10,2))

# =============================================================================
# Full()
# =============================================================================


np.full(10,8)

np.full((1,2),3)

np.full((1,2),fill_value=3)



# =============================================================================
# eye(N,M=None)
# 
# N=-- No. of rows
# M=No. of columns
# No of columns and rows may not be equal
# =============================================================================

np.eye(2,3)


np.eye(5,k=1)

# k which diagonal ones can contain 1

np.identity(3)



# =============================================================================
# np.empty()
# To store uinitilized data 
# =============================================================================
np.empty(5) # garbage value
# array([0.00000000e+000, 9.73006471e-312, 9.73006470e-312, 9.73006471e-312,
#        1.37728685e-281])
np.empty((3,3))
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
np.empty((3,2))
# array([[2.35541533e-312, 2.33419537e-312],
#        [2.22809558e-312, 5.38531554e-322],
#        [2.35541533e-312, 5.38531554e-322]])


# =============================================================================
# zeros vs empty
# ---------------------------
# If we required an arrray only with zeros, then we should go with zeros
# If we never worry about data, we required an empty array for future purpose,
# we should go for empty()
# The time required to create empty array is very less as compared to zeros i.e 
# performance wise empty is prefered over zero function
# 
# =============================================================================

from datetime import datetime
start_time=datetime.now()
a=np.zeros((25000,300,400))
end_time=datetime.now()
print(f"Time taken for dot product using Zeros is {end_time-start_time}")

from datetime import datetime
start_time=datetime.now()
b=np.empty((25000,300,400))
end_time=datetime.now()
print(f"Time taken for Empty using Zeros is {end_time-start_time}")



a.shape
a.size
print(sys.getsizeof(a))
print(sys.getsizeof(b))


# =============================================================================
# Array creation by using random library
# 1. ranint()
# 2.rand()
# 3. uniform()
# 4. randn()
# 5. shuffle()
# 6. Choice 
# =============================================================================

help(np.random.randint)


# =============================================================================
# # 1. randint()
# # -- To generate random int values in the given range
# # randint(low,high=None,size=None,dtype=int)
# #    return random integers from 'low'(inclusive) to 'high'(exclusive)
# #   [low,high]
# =============================================================================
np.random.randint(10,20)# random value between 10 and 20 i.e. 10 to 19 only


np.random.randint(1,9,size=10)
# array([7, 1, 4, 1, 3, 8, 1, 7, 3, 5])

np.random.randint(100,size=(3,5))

np.random.randint(10,100,size=(2,3,4))


np.random.randint(10,100,size=(5,100))


#Type casting from int to float type
a=np.random.randint(100,size=(3,5))
b=a.astype('float')


# =============================================================================
# 2. rand():
    # it will generated random float values
    # in the range (0,1) from uniform distribution
# uniform distribution
# normal distribution
# =============================================================================

np.random.rand() # Single float value

np.random.rand(10) # 10 values in range 0 to 1 from uniform distribution

np.random.rand(3,5)


# Customize range
# rand() ---> Range is always 0 to 1 
# uniform() ---> Customize range

# =============================================================================
# 3. Uniform ()
# =============================================================================
np.random.uniform() #0.8337019506251115 -- range 0 to 1

# Customized range
np.random.uniform(1,10,size=None) #2.2030786332269012

np.random.uniform(10,20,size=10) 
# array([15.77940329, 18.17853868, 12.51446277, 15.95268679, 19.51978633,
#        14.36798581, 16.19980976, 11.68930769, 18.79984254, 14.82534857])


s=np.random.uniform(10,20,size=10) 
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
counts,bins,ignored=plt.hist(s,15,density=True)
plt.plot(bins,np.ones_like(bins),linewidth=2,color='r')
plt.show()

# It will be more uniform
s=np.random.uniform(10,20,size=100000) 
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
counts,bins,ignored=plt.hist(s,15,density=True)
plt.plot(bins,np.ones_like(bins),linewidth=2,color='r')
plt.show()




# =============================================================================
# 4. randn
# mean=0 and variance=1
# =============================================================================
np.random.randn()

np.random.randn(10)
# array([ 0.97385248,  0.381062  , -1.64341583,  0.58526548,  0.93611911,
#        -0.17661256, -1.12100144,  0.9678681 ,  0.77948945,  1.49958857])
# Customize The mean and variance
# Go for normal () function



# =============================================================================
# 5. normal()# 
# normal(loc=0.0,scale=1.0,size=None)
# loc - Mean
# scale= standard deviation of distribution
# =============================================================================

# np.random.normal() 1.6868605506757
np.random.normal(10,4,size=10)
# Mean=10 and variane =4
# array([11.8652502 ,  6.66205326,  6.26512132,  5.14434408,  8.12169155,
#         7.6040149 ,  9.01118682,  5.08260151, 11.23067308,  8.75511666])

np.random.normal(10,4,size=(2,3,4))

# array([[[12.96951557,  7.20034975, 14.94995147, 21.69089784],
#         [12.44248915,  6.98941721, 16.85619101, 11.19929489],
#         [16.99635595, 15.89926491,  8.31693686,  7.45886407]],

#        [[ 5.79714395,  6.23691817, 10.84505421,  9.61860033],
#         [13.4285855 ,  6.89079208,  7.41678842, 12.38650098],
#         [ 8.47532651,  6.74266897, 15.0533224 ,  4.56956762]]])


s=np.random.normal(10,4,size=100000) 
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
counts,bins,ignored=plt.hist(s,15,density=True)
plt.plot(bins,np.ones_like(bins),linewidth=2,color='r')
plt.show()

s.var()
s.std()
s.mean()


# shuffle():
x=[1,2,3,4]
print(np.random.shuffle(x)) #None

a=np.arange(9)
print(a)
np.random.shuffle(a) 
print('#'*20)
print(a)




