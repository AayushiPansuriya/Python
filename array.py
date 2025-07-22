# #unit-2

# #array:-

# #syntax:-
# #array_name=array(type_code,[array_elements])

# #there are three ways to delcare an array
# #1st

# # import array
# a=array.array('i',[2,,3,4,5,6,7])
# print(a)

# # #2nd
# # import array as ar
# a=ar.array('i',[2,,3,4,5,6,7])
# print(a)

# # #3rd
# from array import* 
# a=array('i',[2,,3,4,5,6,7])
# print(a)

# #indexing and slicing array

# #indexing
# from array import*
# a=array('i',[2,3,4,6,8])
# print(a)
# n=len(a )
# for i in range(n):
# 	print(a[i],end='')

# i=0
# while i<n:
# 	print(a[i])
# 	i=i+1

# from array import*
# a=array('c',[2,3,4,6,8])
# print(a) #ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)

# from array import*
# a=array('d',[2.2,3.3,4.4,6,8.8])
# print(a)

# from array import*
# a=array('u',['a',''d','o','v'',j'])
# print(a)

# #slicing

# from array import*
# a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t']
# b=a[1:13]
# print(b)


# from array import*
# a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t']
# for i in a[0:16]:
# 	print(i,end=' ')

# a.append(10)
# print(a)

# a.append(0,0)
# print(a)

# a.remove(6)
# print(a)

# b=a.pop()
# print('the poped element was',b)
# print(a)

# b=a.pop()
# print('the element 7 is found at the position:',b)

#types of array

#1. single dimension array
#2. multi dimension array

#1st  way to declare an array
# import numpy
# a=numpy.array([2,3,4,5,6])
# print(a)

#2nd way to declare an array
# import numpy as nu 
# a=nu.array([2,3,4,5,6])
# print(a)

#3rd way to declare an array
# from numpy import*
# a=array([2,3,4,5,6])
# print(a)

#it can also create array of other types
# from numpy import*
# a=array(['rose','lotus','sunflower','mogra','lily'])
# print(a)

#creating an array using linspace()
# from numpy import*
# arr=linspace(1,10,5)
# print(arr)

# operations on array
# from numpy import*
# a=array([10,20,30,40,50])
# print(a)
# print('the answer is:',a+5)
# print('the answer is:',a-5)
# print('the answer is:',a*5)
# print('the answer is:',a/5)
# print('the answer is:',sum(a))
# print('the answer is:',max(a))
# print('the answer is:',min(a))
# print('the answer is:',mean(a))

#comparing array
# from numpy import*
# a1=array([1,2,13,4,5])
# a2=array([10,2,3,4,15])
# print('the comparison:',a1==a2)
# print('the comparison:',a1<=a2)
# print('the comparison:',a1>=a2)
# print('the comparison:',a1!=a2)

#using where()
# from numpy import*
# a1=array([1,2,13,4,5])
# a2=array([10,2,3,4,15])
# a3=where(a2<a1,a2,a1)
# print(a1)
# print(a2)
# print(a3)

#using nonzero()
# from numpy import*
# a1=array([1,2,13,4,5])
# a2=nonzero(a1)
# print(a1)
# print(a2)

#view()
# from numpy import*
# a1=array([1,2,0,4,5])
# a2=a1.view()
# print(a1)
# print(a2)

#copy()
# from numpy import*
# a1=array([1,2,0,4,5])
# a2=a1.copy()
# print(a1)
# print(a2)
# a1[3]=40
# print(a1)
# print(a2)


#slicing and indexing in numpy array
#formate:-array_name(start:stop:stepsize)

from numpy import*
a1=array([1,2,0,4,5])
print(a1[0:5])