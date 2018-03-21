##Lets try multi threading with python
from threading import Thread
import PyClassInherit
import time

def junkie(tid):
    i=10
    log_obj=PyClassInherit.synced_logger("INFO","multi_threading.txt")
    while i>=0:
        msg=str(tid)+" -- Iteration: "+str(i)
        log_obj.log_it(str(msg))
        time.sleep(5)
        i-=1
        
        
##MAIN##
task_list=[]
for i in [1,2]:
    task=Thread(target=junkie, args=(i,))
    print(task)
    task_list.append(task)
    task.start()
    
for task_ in task_list:
    task_.join()
    
##Next Up Dealing with classes having run method