##Lets take a look at classes in Python

##OOP concepts in python:

#     Abstraction
#     Encapsulation
#     Polymorphism
#     Inheritance

import time
from asyncio.locks import Lock
from pathlib import Path


##A class constructor is named "__init__"

##The first parameter of the constructor or the memeber functions of the class must be "self"

##So what is self in python?
    ##Self is the current instance of the class.
    ##In other OOP Languages like Java there is no explicit mentioning of "self"
    ##self is not a reserved keyword in python.
    ##There was even a petition to remove explicit assignment of self
    ##http://neopythonic.blogspot.in/2008/10/why-explicit-self-has-to-stay.html    

################NO Access specifiers in Python!!!################
#####Synchronization is there 



class logger:
    ##Define some variables
    classname="logger"
    default_log_level="INFO"
    log_file=""
    default_delimiter="\n"
    def __init__(self,instance_log_level,log_file):
        if instance_log_level != "":
            self.default_log_level=instance_log_level
        if log_file == "":
            raise Exception("Undefined Log file to initialize logger class, Logger class init failed")
        else:
            self.log_file=log_file
            self.checkAndTouchLogFile()
            print("Class: ", self,"initialized Succesfully with log level: ",self.default_log_level," for the file: ",self.log_file)
      
    def checkAndTouchLogFile(self):
        if  Path(self.log_file).is_file() != True:
            print("WARN: The logfile: ",self.log_file," deosn't exist, Creating it!")
    def log_it(self,msg):
        date=time.asctime( time.localtime(time.time()) )
        self.write_log(str(date+" -- " + self.default_log_level+" -- "+msg+"\n"))
        
    def write_log(self,log_msg):
#        with Lock:
            #Lock.acquire(self)
            fh_=open(self.log_file,"a+")
            fh_.write(log_msg)
            fh_.close()
            #Lock.release(self)
        
    def __add(self,a,b):
        print(a+b)
        return 