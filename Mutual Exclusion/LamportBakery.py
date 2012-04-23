#Lamport's Bakery Algorithm for n processes
 
#Import required modules
import random
import threading

# Declare global variables required by Lamport's Bakery Algorithm
choosing = []
num = []
numThreads = 0

# Define a class Bakery for Lamport's Bakery Algorithm
class Bakery( threading.Thread ):
    def __init__(self, threadId, requestList):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.requests = requestList
        
    def func(self):
        return 0
        
    def CS(self, task):
        global choosing
        global num
        
        print(str(self) + " requesting CS")
        choosing[self.threadID] = 1
        num[self.threadID] = 1 + max(num)
        choosing[self.threadID] = 0

        for j in range (1, numThreads + 1):
            while (not (choosing[j] == 0)): pass
            while ((not (num[j] == 0)) and 
                         ((num[j] < num[self.threadID]) or ((num[j] == num[self.threadID]) and (j < self.threadID)))):pass          
            
        requestNum = random.choice(self.requests)
        self.requests.remove(requestNum)
                               
        print(str(self) + " " + str(requestNum) + " entering CS")
        task
        print(str(self) + " " + str(requestNum) + " exiting CS")
        num[self.threadID] = 0
        
                        
    def run(self):
        while self.requests.__len__() > 0:
            self.CS(self.func())
            
# Setup function for initializing the required parameters
def setupLamportBakery(Threads):
    
    global choosing
    global num
    global numThreads
    
    choosing = [0] * (Threads + 1)
    num = [0] * (Threads + 1)
    numThreads = Threads
    
    
