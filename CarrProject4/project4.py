"""
Names: Nicky Valdecanas & Michael Carr
Project: 4
Due Date: December 13

"""
import matplotlib.pyplot as plt
import argparse
import time
from dynamic import Dynamic
from greedy import Greedy
from heap import Heap

def graphMaker():
    #Initializing lists
    nonHeap_x = []
    nonHeap_y = []
    heap_x = []
    heap_y = []

    #For 8 files 0 through 8
    for i in range(9):
        #Initialize
        weights_list = []
        values_list = []
        heap_weight = []
        heap_values = []
        used_vals = []
        used_Heapvals = []

        #Reopening and initailizing files
        c_file = "./KnapsackTestData/p0" + str(i) + "_c.txt"
        w_file = "./KnapsackTestData/p0" + str(i) + "_w.txt"
        v_file = "./KnapsackTestData/p0" + str(i) + "_v.txt"

        #Capacity
        file = open(c_file)
        maxCap = int(file.readline())
        file.close()

        #Weights
        file = open(w_file)
        for line in file:
            weights_list.append(int(line))
            heap_weight.append(int(line))
        file.close()

        #Values
        file = open(v_file)
        for line in file:
            values_list.append(int(line))
            heap_values.append(int(line))
        file.close()

        #Greedy non heap
        greedyClass = Greedy()
        greedyClass.quickSort(0, len(values_list) - 1, values_list, weights_list)
        greedyClass.greedyApproach(values_list, maxCap, weights_list, used_vals)
        greedyOps = greedyClass.greedyOperations
        nonHeap_x.append(len(values_list))
        nonHeap_y.append(greedyOps)

        #Greedy heap
        heapClass = Heap()
        heapClass.heapSort(heap_values, heap_weight, len(heap_values))
        heapClass.heapApproach(heap_values, heap_weight, maxCap, used_Heapvals)
        heapGredOps = heapClass.heapOperations
        heap_x.append(len(values_list))
        heap_y.append(heapGredOps)

    #Printing the two graphs one by one.
    print("Printing Non-Heap Greedy")
    plt.title("Greedy Non-Heap")
    plt.xlabel("n")
    plt.ylabel("Time (B-ops)")
    plt.plot(nonHeap_x, nonHeap_y, 'bo')
    plt.show()

    print("Printing Heap Greedy")
    plt.title("Heap Greedy")
    plt.xlabel("n")
    plt.ylabel("Time (B-ops)")
    plt.plot(heap_x, heap_y, 'go')
    plt.show()

def optimalSubset(originalList, optimalValues):
    optimalSubset = []
    #Find indexes from original list
    for i in range(len(optimalValues)):
        for j in range(len(originalList)):
            if(optimalValues[i] == originalList[j]):
                optimalSubset.append(j+1)
                break
    optimalSubset.sort()
    return optimalSubset

def main():

    #For argument passing
    fileargs = argparse.ArgumentParser()
    fileargs.add_argument('file', help ="file number to run", type=int)
    args = fileargs.parse_args()

    #Initialize Knapsack Objects for tasks
    weights = []
    values = []
    valueIndices = [] #Copy of the original order of values
    heapWeights = []
    heapValues = []

    #Concate checks and balances
    if args.file < 10:
        c_file = "./KnapsackTestData/p0" + str(args.file) + "_c.txt"
        w_file = "./KnapsackTestData/p0" + str(args.file) + "_w.txt"
        v_file = "./KnapsackTestData/p0" + str(args.file) + "_v.txt"
    else:
        c_file = "./KnapsackTestData/p" + str(args.file) + "_c.txt"
        w_file = "./KnapsackTestData/p" + str(args.file) + "_w.txt"
        v_file = "./KnapsackTestData/p" + str(args.file) + "_v.txt"

    print("File containing the capacity, weights, and values are:", c_file[19:]+ ", "+w_file[19:]+", "+v_file[19:])
    print()

    #Read in from files
    file = open(c_file)

    #Max weight
    maxCapacity = int(file.readline())
    file.close()

    #Weights
    file = open(w_file)
    for line in file:
        weights.append(int(line))
        heapWeights.append(int(line))
    file.close()
    
    #Values
    file = open(v_file)
    for line in file:
        valueIndices.append(int(line))
        values.append(int(line))
        heapValues.append(int(line))
    file.close()

   
    totalWeights = len(weights)
    totalValues = len(values)
    
    print("Knapsack capacity =", maxCapacity, ". Total number of items =",totalWeights)
    print()
    #Dynamic Programming
    dynamicClass = Dynamic()
    dpTable = [[0 for x in range(maxCapacity + 1)] for x in range(totalWeights + 1)]
    
    begin = time.time()
    dpResult = dynamicClass.dynamicApproach(weights, values, maxCapacity, totalWeights, dpTable)
    dpOptimal = dynamicClass.dynamicOptimal(weights, maxCapacity, totalWeights, dpTable)
    dpTime = time.time() - begin

    print("Traditional Dynamic Programming Optimal value:", dpResult)
    print("Traditional Dynamic Programming Optimal subset:", dpOptimal)
    print("Traditional Dynamic Programming Time Taken:", dpTime)
    print()
    
    
    #Greedy approach using in-built sorting
    greedyOptSubset = []
    greedyOptValues = []
    greedyClass = Greedy()

    greedyClass.quickSort(0, totalValues-1, values, weights)
    greedyResult = greedyClass.greedyApproach(values, maxCapacity, weights, greedyOptValues)
    greedyOptSubset = optimalSubset(valueIndices,greedyOptValues)
    
    print("Greedy Approach Optimal value:", greedyResult)
    print("Greedy Approach Optimal subset:", greedyOptSubset)
    print("Greedy Approach Number of Operations:", greedyClass.greedyOperations)
    print()
    
    #Greedy approach using a max-heap
    heapOptSubset = []
    heapOptValues = []
    totalHeapValues = len(heapValues)
    heapClass = Heap()

    heapClass.heapSort(heapValues,heapWeights,totalHeapValues)
    heapOptValue = heapClass.heapApproach(heapValues,heapWeights,maxCapacity,heapOptValues)
    heapOptSubset = optimalSubset(valueIndices,heapOptValues)
    
    print("Heap-based Greedy Approach Optimal value:", heapOptValue)
    print("Heap-based Greedy Approach Optimal subset:", heapOptSubset)
    print("Heap-based Approach Number of Operations:", heapClass.heapOperations)
    print()
    graphMaker()
    

main()