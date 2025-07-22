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

#graph
#bar graph
# import pandas as pd
# import matplotlib.pyplot as plt 
# df=pd.read_cexcel('pop.xlsx')
# print(df)

# x=df['Year']
# y=df['Population']
# plt.bar(x,y,label='Population growth',color="blude")
# plt.xlable('Years')
# plt.ylable('Population')
# plt.title('Population growth')
# plt.legend()
# plt.show()

#pie chart

import matplotlib.pyplot as plt
sales_perc=[15,20,25,30,10]
prod=['pencil','eraser','sharpner','scale','pen']
col=['blue','green','red','yellow','pink']
plt.pie(sales_perc,lables=prod,colors=col)
plt.title('sales of product in percentage')
plt.legend()
plt.show()

