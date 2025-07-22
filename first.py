
#.input staements
#input() takes a value from the keyboard and returns it as a string.
a=input()
print(a)

a=input('Enter your name:')
print(a)

#restricting the user to enter the integer value only.
num=input('Enter any integer number:')
print(num)

num=int(input('Enter any integer number:'))
print(num)

num=int(input('Enter any integer number:'))
print(num)

num=float(input('Enter any float number:'))
print(num)

#storing only the 1st character from the string
character=input("Enter the string:")[4]
print(character)

#finding sum and product of tow integer numbers.
a=int(input('Enter the value for a:'))
b=int(input('Enter the value for b:'))
print('the sum of{0} and {1} is {2}'.format(a,b,a+b))
print('the product of{0} and {1} is {2}'.format(a,b,a*b))

#use of split()
#by default the entered numbers are cosidered and accepted as string.
#these strings are divided wherever a space is found by split().
#these strings are read by loop and converted into integers using int().

#accepting 3 values from the user and printing it using split()
n1,n2,n3=[int(no)for no in input("Enter three number by living space in between:").split()]
print(n1,n2,n3)

#take 3 integer values from the user and return sum of it.
n1,n2,n3=[int(no)for no in input("Enter three number by living space in between:").split()]
print('the sum of three values:',n1+n2+n3)

#take group of strings
a=[a for a in input('Enter strings:').split(',')]
print(a)