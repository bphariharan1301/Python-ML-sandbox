import numpy as np

# lets create an numpy array
li = np.array([[1,2,3],[4,5,6]])

print(li)

#shape is numpy attribute which allows programmer to know the shape of the array

print(li.shape)

# lets work with multi dimensional arrays

a=np.array([1,2,3,7])
b=np.array([4,5,6,4])
c=np.array([8,5,6,4])

# the above three arrays are numpy arrays

abc = np.array([a,b,c])

# In the above line we are making a multi dimensional array using 3 one dimmensional array

print(abc)

print(abc.shape)

# size is the function which allows a programer to know the size of the array

print(abc.size)

# lets work with array reshaping and indexing
# reshape is the function which changes the shape of the array

n = abc.reshape(2,6)

print(n)

print(n.shape)

# Indexing

print(abc[0,0]) # This line prints the value of particular indexing

# let's create the array of zeros

zeroarray = np.zeros((3,3)) # np.zeros is the function which creates the array of zeros 

print(zeroarray)

# Similarly we do for array of ones

# Slicing

print(abc[:,3:])


''' :is kept to print every 2 and 3rd row
1:3 is for starting and ending value it prints 2 and 3 rows exluding 1
1 is for step size'''

# Boolean functions in numpy library

hari = abc<3

print(hari) #prints true r false for every value greater then 5 in abc array


#where method
sat=np.where(abc>5,abc,5)

print(sat)

''' lets do sum math operations on numpy array'''

print(a.sum()) #sum() is the function which retuns the sum of the array elements

print(a.cumsum())# cumsum is the function which returns cummulative sum of the elements

print(a.prod())#prod() is the function which returns product of the arrat elements

print(a.cumprod())#cumprod is the function which returs cumulative

''' two array math operations'''

print(a+b)

print(a-b)

print(a*b)
print(a/b)



