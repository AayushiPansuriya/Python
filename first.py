#unit-3

##to work with reguler expression, module 're' must  be imported.
#r:-reguler expression,row string
#m:-first charecter must be 'm'
#\w:-'m' must be followed by alpha numeric value
#string=r'm\w\w' 

# string1='this will be printed on the \n next line'
# print(string1)

# string2=r'this will be printed on the \n next line'
# print(string2)

#using compile() of 're' module

# import re
# abc=re.compile(r'm\w\w')
# string1='mat matter mount mountain river'
# result=abc.search(string1)
# print(result.group())


#defining and calling function 
#syntax:-
  # def function_name(part-1,part-2,part-n):
  # 	function statement

#sum of two numbers using function
# def sum(a,b):
#   total=a+b
#   print('the sum of two numbers is:',total)
# #calling the function
# sum(2,5)
# sum(2.5,5.2)  

#returning the result from a funtion(sum of two digits)
# def sum(a,b):
#    total=a+b
#    return(total)
# #calling the funtion
# x=sum(2,5)
# print('the sum is:',x)
# y=sum(2.5,5.2)
# print('the sum is:',y)

#program to find whether the number is even or odd using function
# def eve_odd(no):
# 	if no%2==0:
# 		print('the number is even')
# 	else:
# 		print('the number is odd')
# #calling the function
# eve_odd(4)
# eve_odd(15)  

#program to find whether the number is positive,negative,or zero
#using function
# def pos_neg_zer(no):
#    if no>0:
#    	print('the number entered is positive')
#    elif no==0:
#    	print('the number entered is zero')
#    else:
#    	print('the number entered is negative')
# #calling the function
# no=int(input('enter a number to check:'))
# pos_neg_zer(no)


#returning multiple values from a function
#program to perform basic arthmatic operations using function
# def arith(a,b):
# 	add=a+b
# 	sub=a-b
# 	mul=a*b
# 	div=a/b
# 	return add,sub,mul,div
# p,q,r,s=arith(20,5)
# print('the addition of two numbers:',p)
# print('the subtraction of two numbers:',q)	
# print('the multiplication of two numbers:',r)		
# print('the division of two numbers:',s)	

#* pass by object:--

# def modify(x):
# 	a=25
# 	print('the value of x inside the function is',x,id(x))
# #calling the funtion
# x=52
# modify(x)
# print('the value of x inside the function is',x,id(x))	

#*imp* formal and actual arguments
# def modify(x,y):-->formal argument
#    ----
#    ----
#  #calling the function
#  a=2,b=5-->actual argument  

#*imp*four types actual arguments:-
# 1.position argument
# 2.keyword argument
# 3.default argument
# 4.variable length argument

# 1.position argument
 
# def combine (str1,str2):
#     str3=str1+str2
#     print(str3)
# #calling the function
# combine('Atmiya','University')     


# 2.keyword argument

# def stud(name,roll):
# 	print('the name of student is',name)
# 	print('the roll number of student is',roll)
# #calling the function
# stud(name='abc',roll=1)
# stud(roll=1,name='abc')


# 3.default argument

# def stud(roll,name='xyz'):
# 	print('the name of student is',name)
# 	print('the roll number of student is',roll)
# #calling the function
# stud(roll=1)
# stud(roll=2,name='abc')


# 4.variable length argument

# def add(farg,*args):
# 	sum=0
# 	for i in args:
# 		sum=sum+i
# 		print('sum of all numbers is:',(farg+sum))
# #calling the function
# add(10,20)
# add(1,2,3,4)		

#passing a group of elements to a function
# def disp(lst):
# 	for i in lst:
# 		print(i)
# #take the input from the user
# print('enter the string:')
# lst=[a for a in input().split()]		
# disp(lst)

#annonymous functions/lambda





#file hendaling:-
#1.text file
 #file hendling in python
 #formate:-file hendler=open('file_name','open mode')

 #to write in the file

 # f=open('abc.txt','w')
 # str=input('enter the text:')
 # f.write(str)
 # f.close()

 #to read the file
 # f=open('abc.txt','r')
 # str=f.read()
 # print(str)
 # f.close()


#talking multiple inputs from the user

# f=open('xyz.txt','w')
# print('enter the string')
# while str!='$':
# 	str=input()
# 	if str!='$':
# 		f.write(str+'\n')
# f.close()	

#append

f=open('abc.txt','a+')
str=' ,rajkot'
f.write(str)
f=open('abc.txt','r')
a=f.read()
print(a)	



#2.binary file
