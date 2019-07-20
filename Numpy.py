import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
#resize the ndarray
a.shape = (3,2) #(row,column)
print("a:")
print(a)
print("\n")

#ndarray object that contains evenly spaced values within a range
b = np.arange(10,30,5) #(start,stop,step)
print("b:")
print(b)
print("\n")

c = np.linspace(10,30,3) #(start,stop,number of samples)
print("c:")
print(c)
print("\n")

#slice items
print("array of items in the second column:")
print(a[...,1])
print("\n")

print("array of items in the second row:")
print(a[1,...])
print("\n")

print("items greater than 3:")
print(a[a>3])
print("\n")

print("flatten the array a:")
print(a.flatten())
