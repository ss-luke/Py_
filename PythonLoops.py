#####Python loops 

from time import sleep
#1. for
#2. while
#3. Nested loops

#######Loop control statements

##1.break
##2.continue
##3.pass


for _ in range(1,10,2):
    ##Python's range--------- range(0,n) --- iterates starting with 0 and stops with n-1
    ##range is not inclusive of the ending -- n
    ##range(start,end,stp_size) --- all the values should be a valid integer
    print(_)

print("\n")     
#list
list_=[1,2,3,4,5]
for _ in range(len(list_)):
    print(_)

print("\n")  
for _ in list_:
    print(_)
print("\n")


i=10

##while loop
while i>10:
    print(i)
    i=i-1
    
##continue

for i_neg in [-1,-2,-3,-4]:
    if i_neg > 0:
        print(i_neg)
    else:
        continue
######Nested Loops -- break
     
while True:
    for _ in list_:
        print(_)
        print("Sleeping for 1")
        sleep(1)
    break

print("Hi")

##Loops pass-- Tell the instruction to do nothing
##The pass statement is a null operation; nothing happens when it executes.
## The pass statement is also useful in places where your code will eventually go,
## but has not been written yet i.e. in stubs.

while True:
    for _ in list_:
        print(_)
        print("Sleeping for 1")
        sleep(1)
        pass
    break
print("Hi")