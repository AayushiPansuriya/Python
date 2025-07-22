
#unit-1


#operators:

#it return 1, if both bits are 1,else0
# a=28
# b=19
# print(a&b)

#(ii).bitwise or operator:
#it return o,if both bits are 0,else 1
# a=28
# b=19
# print(a|b)

#(iii).bitwise xor operator:
#return 1,if both bits are different,otherwise 0.
# a=28
# b=19
# print(a^b)

#(iv).bitwise not operator:
#it work on one operand
#it does 2s complement
# a=28
# print(~a)

#while loop

#using a while lop,make the program that accepts numeric values from the users until user press 0.
#give the sum of all inserted values.

# sum=0
# num=int(input('enter the number:'))
# while num!=0:
# 	sum=sum+num
# 	num=int(input('enter the num:'))
# print("The sum of all enterd number is:",sum)	


#using while loop diplay the table of 2 
# n=2
# counter=1
# print('The table of n is as follow:')
# while counter<=10:
# 	ans=n*counter
# 	print(n,'x',counter,'=',ans)
# 	counter=counter+1

#display even numbers between 1-10
# a=2
# while a>=1 and a<=10:
# 	print(a)
# 	a=a+2

#display odd numbers between 1-10
# a=1
# while a>=1 and a<=10:
# 	print(a)
# 	a=a+2	

#ask user whether they want odd numbers or even numbers
# n=int(input('enter your choice:1 for odd numbers and 2 for even numbers:'))
# if n==1:
# 	print('All the odd numbers between 1-10 are as follow:')
# 	while n>=1 and n<=10:
# 		print(n)
# 		n=n+2
# elif n==2:
#     print('All the even numbers between 1-10 are as follow:')
# 	while n>=1 and n<=10:
# 		print(n)
# 		n=n+2		

#display numbers and their associated sequare.
# to=2
# frm=20
# n=1
# while(n<=10):
#     print(n,'\t',n**2)
#     n=n+1		


#to find only even numbers the list
# lst=[4,5,6,7,8,9,2,3,4,1]
# a=0
# while(a<len(lst)):
# 	if lst [a]%2==0:
# 		print(lst[a])
# 	a=a+1	

#len()
# a='welcome to the lab'
# print(len(a))

# a='Rajkot'
# b=0
# while(b<len(a)):
# 	print(a[b])
# 	b=b+1




#while-loop

# a=int(input('enter the number:'))
# while a<=10:
#     print(a)
#     a=a+1
# print('while loop ended')    


# #loop with in the loop is cosidered as nested loop
# for i in range(3):
# 	for j in range(4):
# 		print(i,j)


# #break statement
# #terminate the loop when 6 is found
# a=1
# while a<=10:
#     print(a)
#     a=a+1
#     if a++6:
#         break
# print('loop has ended incidently')      

# #telling user whether the number is found in the list or not
# lst=[4,8,6,7,9]
# num=int(input('what you want to serch?:'))
# for n in lst:
# 	if num=n:
# 		print('the number you wanted to serch is found in the list')
# 		break
# else:
#    print('the number you wanted to serch is not found in the list')	

# #terminate the loop when'k'
# a='rajkot'
# for b in a:
#     print(b)
#     if b=='k':
#       break

# #continue statement
# a='RajkotGujaratIndia'
# for i in a:
# 	if (i=='a'):
# 		continue
#     print(i,end='')


# #skip when'a'is found in the string
# a=1
# while a<=10:
# 	print(a)
# 	a=a+1
# 	if a++6:
# 		break
# 		print('a')

# #print 1-10,skip 5
# for i in range(1,11):
# 	if i==5:
# 		continue
# 	print(i)

# #pass statement
# it is considered as a placeholder for the code to be writen in the future
# a=0
# while a<10:
# 	a=a+1
# 	if a>5:
# 		pass
# 	print(a)	



#python if..elif.py


#program to print the biggest number from the fourn numbers
#using if statement

# n1=int(input('enter the value for number-1:'))
# n2=int(input('enter the value for number-2:'))
# n3=int(input('enter the value for number-3:'))
# n4=int(input('enter the value for number-4:'))

# if n1n2 and n1n3 and n1n4:
#     print('Number-1 is the biggest out of all entered numbers')

# if n2n1 and n2n3 and n2n4:
#     print('Number-2 is the biggest out of all entered numbers')

# if n3n1 and n3n2 and n3n4:
#     print('Number-3 is the biggest out of all entered numbers')

# if n4n1 and n4n2 and n4n3:
#     print('Number-4 is the biggest out of all entered numbers') 

# else:
#    print('enter the valid number') 


#python nested-if.py

#nested-if

# n1=int(input('enter the value for number-1:'))
# n2=int(input('enter the value for number-2:'))
# n3=int(input('enter the value for number-3:'))
# n4=int(input('enter the value for number-4:'))

# if n1>n2:
#     if n1>n3:
#       if n1>n4:
#           print('N-1 is biggest number')

# if n2>n1:
#     if n2>n3:
#       if n2>n4:
#           print('N-2 is biggest number')

# if n3>n2:
#     if n3>n1:
#       if n3>n4:
#           print('N-3 is biggest number')          

# if n4>n2:
#     if n4>n3:
#       if n4>n1:
#           print('N-4 is biggest number')   
