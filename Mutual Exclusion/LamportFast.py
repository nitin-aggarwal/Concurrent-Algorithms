# Lamport's Fast shared memory mutual exclusion algorithm for n processes
 
# Import required modules
import random
import threading

# Declare global variables required by Lamport's Fast Algorithm
x = 0
y = 0
b = []
numThreads = 0

# Define a class Fast for implementing Lamport's Fast Algorithm
class Fast( threading.Thread ):
    def __init__(self, threadId, requestList):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.requests = requestList
        
    def func(self):
        return 0
        
    def CS(self, task):
        global b
        global x
        global y
        
        print( str(self) + " requesting CS" )
        while self.requests.__len__() > 0:
            b[self.threadID] = 1
            x = self.threadID
    
            if y != 0:  
                b[ self.threadID ] = 0
                while y != 0: pass
                continue
    
            y = self.threadID
    
            if x != self.threadID:
                b[ self.threadID ] = 0
                for thread in range(1, numThreads+1 ):
                    while b[ thread ] != 0: pass
                            
                if y != self.threadID:
                    while y != 0:  pass
                            
                continue
    
            reqId = random.choice(self.requests)
            self.requests.remove(reqId)
                
            print(str(self) + " "+str(reqId)+" entering CS" )
            task
            print(str(self) + " "+str(reqId)+ " exiting CS" )
                
            y = 0
            b[ self.threadID ] = 0
            break
            
            
    def run(self):
        while self.requests.__len__() > 0:
            self.CS(self.func())
            
#  Setup function for initializing the required parameters
def setupLamportFast(Threads):
    
    global x
    global y
    global b
    global numThreads 
     
    x = 0
    y = 0
    b = [0] * (Threads + 1)
    numThreads = Threads
    
