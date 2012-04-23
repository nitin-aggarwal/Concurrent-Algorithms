#Lamport's Bakery Algorithm for n processes
 
#Import required modules
import random
import sys
import threading

# Scan command line arguments for inputs
noOfThreads   =  int(sys.argv[1])
noOfRequests  =  int(sys.argv[2])

# Declare global variables required by Lamport's Bakery Algorithm
choosing = []
num = []
requestListBakery = []

# Initialize a sequence for storing thread IDs
threadListBakery = [None] * (noOfThreads + 1)

# Define a class Bakery for implementing Lamport's Bakery Algorithm
class Bakery( threading.Thread ):
    def __init__(self, threadId):
        threading.Thread.__init__(self)
        self.threadID = threadId

    def func(self):
        return 0
        
    def CS(self, task):
        task
            
    def run(self):
        global choosing
        global num
        reqId = 0

        while requestListBakery.__len__() > 0:
            print(str(self) + " requesting CS" )
            
            choosing[self.threadID] = 1
            num[self.threadID] = 1 + max(num)
            choosing[self.threadID] = 0

            for j in range (1, noOfThreads + 1):
                while (not (choosing[j] == 0)): pass
                while ((not (num[j] == 0 )) and 
                         ((num[j] < num[self.threadID]) or ((num[j] == num[self.threadID]) and (j < self.threadID))) ):pass          
            
            if requestListBakery.__len__() > 0:
                reqId = random.choice(requestListBakery)
                requestListBakery.remove(reqId)
            else:
                break
                       
            print(str(self) + " "+str(reqId)+" entering CS" )
            self.CS(self.func())
            print(str(self) + " "+str(reqId)+ " exiting CS" )
            num[self.threadID] = 0
            
# Define setup function for setting up the required parameters
def setupLamportBakery():
    
    # Initialize variables required by the algorithm
    global choosing
    global num
    global requestListBakery
    
    choosing = [0] * (noOfThreads + 1)
    num = [0] * (noOfThreads + 1)
    for i in range(1, noOfRequests + 1):
        requestListBakery.append(i)
    
# setup the required parameters
setupLamportBakery()
print( "Running Lamport's Bakery mutual exclusion algorithm -- Threads: " + str( noOfThreads ) + " Requests: " + str( noOfRequests ))

# Create and start the threads
for threadIdBakery in range( 1, noOfThreads + 1 ):
    threadListBakery[threadIdBakery] = Bakery(threadIdBakery)
    threadListBakery[threadIdBakery].start()
