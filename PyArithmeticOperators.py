######## Operators in Python


#     Arithmetic Operators
#     Comparison (Relational) Operators
#     Assignment Operators
#     Logical Operators
#     Bitwise Operators
#     Membership Operators
#     Identity Operators


############### Increment and Decrement operators ( both pre and post) are not allowed in it.###############

#Add
i=10+2
#Sub
i=i-2
#Mul
i=i*2
##Expo
i=i**2
##Percentile
i_per=i%2
i_div=i/2
#Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
i_floor=-10/3 ## gives 4
i_floor_1=10/3 ## Gives 3


###########Python Comparison Operators###########
if 1==1:
    print(True)
if 2!=3:
    print(True)
if (2>=2):
    print(True)
if 3>2:
    print(True)
if 2<4:
    print(True)
if(3<=4):
    print(True)
    
    
#######################Python Assignment Operators###################
##Add and assign , sub and assign, so on so forth
i_assign=2
i_assign+=2
i_assign-=3
i_assign*=-1
i_assign/=1
i_assign%=1
i_assign**=5
i_assign//=-1

print(i_assign)

#######################Python Bitwise Operators##################
i_bin=1010
i_bin_1=1010
i_hex=0xffff

##And Operation##
i_and=i_bin&i_bin_1
print(i_and)
#OR
i_or=i_bin|i_bin_1
print(i_or)
#XOR
i_xor=i_bin^i_bin_1
print(i_xor)
#Binary Ones Complement
i_1c=~i_bin
print(i_1c)

########Shift
i_left=i_bin << 2
print(i_left)
i_right=i_bin >> 2
print(i_right)


###############Python Logical Operators##############
i_c=1010
i_d=1101

#logical AND

if i_c and i_d :
    print(True)

#Logical OR

if i_c or i_d:
    print(True)
    
#####Not logical - Reverse the logical state 

if not(i_c and i_d):
    print(False)
    
    
    
##################Python Membership Operators##################

####### "in" and "not in"

for i_mem in range(5):
    print(i_mem)

list_exclusion=[2,3,4,5]

for i_notin in range(25) :
        print(i_notin)
  
i_notin=6      
if i_notin not in list_exclusion:
    print(i_notin,"not in",list_exclusion)
    



######################Python Identity Operators##################
i_int=1
i_str="Hola"

if(i_int is i_str):
    print("They are the same type of the object!")
elif(i_int is not i_str):
    print("They are different")
else:
    print("I don't know what they are")