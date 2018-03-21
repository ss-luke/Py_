##!/usr/bin/python

import subprocess ##Inport necessary libraries


##The above is the shebang for python interpreter
##Hello world##
print ("Hello World! ")

###Variables

#1.Assignment
a=1
b="Hello World"
c=d=2

print(a,b,c,d)
#Unset a var

del a
## Error- print(a,b,c,d) -------NameError: name 'a' is not defined

###Input streams### The input Method and printing read variable onto console
##print ("Ok the entered number is : " + x)
##The above will throw an error, TypeError: Cannont concatinate str type and int type , for that the below can be used.
#print ("Ok the entered number is :" + str(x))
## But I find print "Ok the entered number is :",x easy to use often so as to not use str(_object)
##str(_object) will not miutate _object , but will  return a new string object

print ("Enter the number you would like to display: ")
x=input()
print ("Ok the entered number is :",x)
