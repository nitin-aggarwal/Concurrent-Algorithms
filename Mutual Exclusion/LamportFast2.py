#Lamport's Fast Algorithm for n processes
 
#Import required modules
import random
import sys
import threading

# Scan command line arguments for inputs
noOfThreads   =  int(sys.argv[1])
noOfRequests  =  int(sys.argv[2])

# Declare global variables required by Lamport's Fast Algorithm
b = []
x = 0
y = 0
requestListFast = []

# Initialize a sequence for storing thread IDs
threadListFast = [None] * (noOfThreads + 1)

# Define a class Fast for implementing Lamport's Fast Algorithm
class Fast( threading.Thread ):
    def __init__(self, threadId):
        threading.Thread.__init__(self)
        self.threadID = threadId

    def func(self):
        return 0
        
    def CS(self, task):
        task
            
    def run(self):
        global b
        global x
        global y
        reqId = 0

        while requestListFast.__len__() > 0:
            print( str(self) + " requesting CS" )
            while requestListFast.__len__() > 0:
                b[self.threadID] = 1
                x = self.threadID
    
                if y != 0:
                    b[ self.threadID ] = 0
                    while y != 0: pass
                    continue
    
                y = self.threadID
    
                if x != self.threadID:
                    b[ self.threadID ] = 0
                    for thread in range(1, noOfThreads+1 ):
                        while b[ thread ] != 0: pass
                            
                    if y != self.threadID:
                        while y != 0:  pass
                            
                    continue
    
                reqId = random.choice(requestListFast)
                requestListFast.remove(reqId)
                
                print(str(self) + " "+str(reqId)+" entering CS" )
                self.CS(self.func())
                print(str(self) + " "+str(reqId)+ " exiting CS" )
                
                y = 0
                b[ self.threadID ] = 0
                break
            
            

# Define setup function for setting up the required parameters
def setupLamportFast():
    
    # Initialize variables required by the algorithm
    global x
    global y
    global b
    global requestListFast
    
    x = 0
    y = 0
    b = [0] * (noOfThreads + 1)
    for i in range(1, noOfRequests + 1):
        requestListFast.append(i)
    
# setup the required parameters
setupLamportFast()
print( "Running Lamport's fast mutual exclusion algorithm -- Threads: " + str( noOfThreads ) + " Requests: " + str( noOfRequests ))

# Create and start the threads
for threadIdFast in range( 1, noOfThreads + 1 ):
    threadListFast[threadIdFast] = Fast(threadIdFast)
    threadListFast[threadIdFast].start()
