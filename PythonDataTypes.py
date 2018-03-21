####DataTypes####


#1. Strings
    #compare
    #substring
    #Concat
    #Repetition
#2. Lists (IMHO-Composite Arrays)
    #sublist
    #concat
#3. Tuples--- read-only lists -- Declare Once, use many times
#4. Dictionary-- Hash table


#Strings ## Also covering python if conditional statement
##if COND:
    ##DO
####if COND:
    ##DO
    #else:
    ##DONE
    
str_="How are you doing!"
str_1="I am fine!"

##String match
if str_ == str_1:
    print("Hey you!!")
else:
    print("You dont match with me!")

print(str_[0:2]) ##Substring
print(str_1[0])  ##Character at an index
print(str_+" "+str_1) ##strings concat + operator
print((str_+" "+str_1)*2) ##strings repetition "How are you doing! I am fine!" is printed twice , *b operator
##Length
print("The length of the string is: " , len(str_))

##Lists
list_=[1,2,3]
list_1=["1","2","3"]
list_2=[1,2,3]

if list_==list_2:
    print("They mathch!")
elif list_==list_1: ###ELse if
        print("No matching lists found!")
else:
    print("Seperation is imminent!")


##Sublist
print(list_[0:2]) ##[start:end]
print(list_1[1])
##COncat -- merge two lists into one, thus forming a new list
print(list_+list_2)
##Merge lists 
list_merge_=list_+list_1 ##[1, 2, 3, 1, 2, 3]
list_merge=(list_+list_2)*2 ##Merge twice with * operator , [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print((list_+list_2)*2) ## Print list twice------[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list_merge) ## Print list twice----------[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

##Assign a new value at an index:
list_[0]=100

##Length of list
print("The length of the list is : ",len(list_merge))

#Tuples
##Tuples are same as lists but immutable
##Only read operations
tuple_=[1,2,3]
print(tuple_[0:4]) ## Note : No out of bounds problem
##tuple_[0]=100 ----- Invalid operation

##Dictionary: {} braces, elements are not ordered by default
##Infamous .keys() and .values() to get list of keys and values respectively

dict_={"name" : "Sasanka","Code" : "Python"}
##Add
dict_["Profession"]="S/W Engineer"
dict_1={1:2,3:4,4:5}
#dict_2=dict_+dict_1
print(dict_["Profession"])
del dict_["Profession"] ##Deletes key value pair

##Merging two Python Dictionaries, while merging duplicate elements are removed
dict_2 = {**dict_,**dict_1}
print(dict_2)
#---------------Data Type Conversions---------------#