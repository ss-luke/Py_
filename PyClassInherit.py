#Lets look into inheritance in python
from MyUtils.PyClasses import logger
import threading

class synced_logger(logger):
    lock = threading.Lock()
            
    def log_it(self, msg):
        self.lock.acquire()
        logger.log_it(self, msg)
        self.lock.release()