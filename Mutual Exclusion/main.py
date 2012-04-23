import LamportBakery
import LamportFast

import random
import sys

# Inputs through command line arguments
numThreads   =  int(sys.argv[1])
numRequests  =  int(sys.argv[2])

# Sequence for storing thread IDs for Bakery Algorithm
threadSeqBakery = [None] * (numThreads + 1)
# Sequence for storing thread IDs for Fast Algorithm
threadSeqFast = [None] * (numThreads + 1)

def bakery():
    
    # Call setup for the required parameters
    LamportBakery.setupLamportBakery(numThreads)
    print( "Running Lamport's Bakery mutual exclusion algorithm -- Threads: " + str( numThreads ) + " Requests: " + str( numRequests ))
    # Create and start the threads
    for threadBakery in range(1, numThreads + 1):
        threadSeqBakery[threadBakery] = LamportBakery.Bakery(threadBakery, [])
    for requestIdBakery in range(1, numRequests + 1):
        threadSeqBakery[random.choice(range(1, numThreads + 1))].requests.append(requestIdBakery)
    for threadBakery in range(1, numThreads + 1):
        threadSeqBakery[threadBakery].start()


    
def fast():
    
    # Call setup the required parameters
    LamportFast.setupLamportFast(numThreads)
    print( "Running Lamport's fast mutual exclusion algorithm -- Threads: " + str( numThreads ) + " Requests: " + str( numRequests ))
    # Create and start the threads
    for threadFast in range(1, numThreads + 1):
        threadSeqFast[threadFast] = LamportFast.Fast(threadFast, [])
    for requestIdFast in range(1, numRequests + 1):
        threadSeqFast[random.choice(range(1, numThreads + 1))].requests.append(requestIdFast)
    for threadFast in range(1, numThreads + 1):
        threadSeqFast[threadFast].start()

def main():        
    bakery()
    fast()  
    
main()  

