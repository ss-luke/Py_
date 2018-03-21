

#####try:
    #except:
    #else:

try:
    op_=open("NOSuchfile_11.txt","r")
except Exception as e:
    print("Exception Occured " , e)
else:
    print("Everythig failed!")
    
    
##Different types of exceptions (Popular)
##RuntimeError is the super class of all exceptions
