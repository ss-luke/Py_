
####Importance of _ in Python 

###The usage of _ in Python can become quite significant depending upon the usage

# There are 5 cases for using the underscore in Python.
# 
#     For storing the value of last expression in interpreter.
#     For ignoring the specific values.
#     To give special meanings and functions to name of vartiables or functions.
#     To use as Internationalization i18n or Localization l10n  functions.
#     To separate the digits of number literal value.

##1. _ can be used to store last used value in Python interpreter, ($_ in the case of perl)

from MyUtils import PyUtils
from MyUtils import PyClasses
import PyClassInherit
for _ in [1,2,3,4]:
    print(_)


print(_+5) #-gives u 9 because _ has stored a value of 4 , 4+5=9

for _ in range(1,10):
    print(_)
    
####For Ignoring the values####

x,_,_,y=(1,2,3,4)
print(x,y) ## Gives u 1,4


####Give special meanings to name of variables and functions####


################ _single_leading_underscore #################

####Private variables#### But not truly private
##Anything with this convention are ignored in from module import *. 
#Still once can access them using  module.<_variable_>
_py_version_=3.6
#_py_devl_name="Sai"


## print(_py_devl_name) throws an error _py_devl_name is not defined

print(PyUtils._py_devl_name)


##single_trailing_underscore_
##Just to avoid collision with Python kewords

class_="Py_Underscore"

####__double_leading_underscore####
##In a class anything starting with __ , the interpreter changes the method name, by adding the class name in which
##it is present
##ClassName.__method fails as the method name is no longer __method

first_class=PyClasses.logger("INFO","pyLog.txt") #Creating the Object of PyClasses
first_class.log_it("Hi This is my first logmessage")
##first_class.__add(2,4) --- will throw an error first_class.__add(2,4)
##AttributeError: 'logger' object has no attribute '__add'

child_class=PyClassInherit.synced_logger("INFO","pyLog_1.txt")
child_class.log_it("Hi This is child class")
 
 
 ####__double_leading_and_trailing_underscore__####
 
 ##__init__ is the constructor for the given class
 ##__eq__ is executed for 3 == 3
 
 
 ##### To separate the digits of number literal value #####
 
 ##For readability use _ to seperate digits in the number -- from Python 3.6 ##
 
i_1=2_3
i_2=3_5
 
print(i_1+i_2)  ####### Gives u 58

###This is especially useful when working with binary numbers
 
bin=1_00_001
bin_1=1_00_000

print(bin&bin_1) 