
# 1. write a program that prints your name and your college name.

# #use dot format
name=input("enter your name: ")
college=input("enter your college:")
print("My name is{0},My college is{1}".format(name,college))

# #use eval
ex=eval(input('enter the expression:'))
print('the result of expression %s'%ex)

#use comandline
import sys
print(sys.argv)


#2.write a program that prints your address with name,all in new line.

 #use dot format
address=input('enter your address:')
name=input('enter your name:')
print("address{0},\n My name is{1}".format(address,name))

# #use eval
ex=eval(input('enter the expression:'))
print('the result of expression %s'%ex)

#use comandline
import sys
print(sys.argv)


#3. write a program that accept two number and perform all basic mathematical operations.

a=input("enter value a:")
b=input("enter value b:")
#print('the addition of {0} and {1} is'.format(a,b,a+b))
#print('the subtraction of {0} and {1} is'.format(a,b,a-b))
print('the multiplication of {0} and {1} is'.format(a,b,a*b))
#print('the division of {0} and {1} is'.format(a,b,a/b))
#print('the moduls of {0} and {1} is'.format(a,b,a%b))
