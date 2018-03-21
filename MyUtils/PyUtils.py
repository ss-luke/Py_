'''
Created on 19-Mar-2018

@author: Sai
'''
from builtins import int
from subprocess import call, Popen, PIPE
from sys import stdout
##Functions in python

_global_module_num=1 ##Private variable by default
_py_devl_name="Sasanka"

def addtwoNums(a,b):
    print("The inputs are: ",a,b)
    print("The sum of : ",a,b,"is: ")
    return a+b

def addtwoStrings(str_1,str_2):
    return int(str_1)+int(str_2)

def execCmd(cmd,args):
    call(cmd+" "+args)
    
def retvalExecCmd(cmd,args):
    retval=call(cmd + " " + args,shell=True)
    return retval

def execCmd_Stdout(cmd,args):
    process = Popen(cmd + " " + args,stdout=PIPE)
    (output, err) = process.communicate() #########In python a method can return more than 1 value
    return (output,err)
    #return retVal
##Accepting command line arguments:.