import random
import math
import numpy as np
import matplotlib.pyplot as plt
import functools

"""
Names: Michael Carr, Bryant Pinto
Class: CS415
Project 1
"""

def ConInit(x, y):

    """
       Parameters
       ----------
       x : int
           one of the two values being passed in
       y : int
           one of the two values being passed in
        Description: Used to find the GCD of two numbers using a consecutive integer sequence.
    """
    # Will keep track of the number of operations
    numOfOperations = 0

    # The minimum value of the two values passes in assigned to t.
    t = min(x, y)

    # While t is greater than 0
    while (t > 0):
        numOfOperations += 1
        if (y % t == 0):
            numOfOperations += 1
            if (x % t == 0):
                return numOfOperations, t
        t -= 1


def ConInitAvgOperations(n):
    """
        Parameters
        ----------
        n : int

        Description: Used to calculate number of operations in consecutive integer checking
    """
    totalOperations = 0.0
    for i in range(1, n + 1):
        v, gcd = ConInit(i, n)
        totalOperations += v
    return totalOperations / n


def Euclids(x, y):
    """
        Parameters
        ----------
        x : int
           one of the two values being passed in
        y : int
           one of the two values being passed in
        Description: Used to find the GCD of two numbers using Euclid's recursive algorithm.
    """
    # If x is equal to 0, return y.
    if(x == 0):
        return 0

    # Else mod y with x to get your new x and put x in y spot and recursive ca

    # call the function again
    return Euclids(y % x, x)+1


def EuclidsAvgOpertions(n):
    """
        Parameters
        ----------
        n : int

        Description: Used to calculate number of operations done by Euclid's algorithm
    """
    totalOperations = 0.0
    for i in range(1, n + 1):
        totalOperations += Euclids(i, n)
    return totalOperations / n


def FibSeq(n):
    """
        Parameters
        ----------
        n : int
           used to find the Fibonacci sequence to that n-1 element

        Description: Used to find a Fibonacci sequence ie [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    # Empty list used to store the sequence
    FibList = []

    if (n == 1):

        FibList.append(0)

    elif (n == 2):
        FibList.append(0)
        FibList.append(1)

    else:
        # If n is not less than of equal to 2 than put the values in FibList [0, 1 and then start adding element [i -2]
        # with element [i-1] to get n, then put it into FibList
        FibList.append(0)
        FibList.append(1)
        for i in range(2, n):
            NextElem = FibList[i-2] + FibList[i-1]
            FibList.append(NextElem)

    # What is in the list print to screen.
    return FibList[n - 1]


def EuclidsConCompare(n):

    """
    Parameters
    ----------
    n : int

    Description: Used to find out how many operations in average (modulo) to either the Euclids algorithm
                or the Consecutive numbers algorithm.
    """

    # Pass value into these functions to get the average operations
    conInit = ConInitAvgOperations(n)
    euclidAvg = EuclidsAvgOpertions(n)
    return conInit, euclidAvg


def EuclidsGCD(k):
    """
    Parameters
    ----------
    k : int

    Description: simple function to find GCD with two lists of prime numbers
    """

    M = FibSeq(k+1)
    N = FibSeq(k)
        
    numOfDivisions, GCD = ConInit(M, N)
    return GCD
        

def SieveGCD(m, n):

    """
    Parameters
    ----------
    No input values

    Description: Used to ask the user for two inputs m and n. Both m and n are passed to SieveMaker and return a list.
                The two lists are compared and a new list is made with the elements that are in both (combolist). At the
                end the combolist elements are multiplied together to get the GCD.
    """

    operations = 0
    mlist = SieveMaker(m)
    nlist = SieveMaker(n)

    largerList = []
    smallerList = []
    if len(mlist) > len(nlist):
        largerList = mlist
        smallerList = nlist
    else:
        largerList = nlist
        smallerList = mlist

    combolist = []
    for i in largerList:
        for j in smallerList:
            operations += 1
            if (i == j):
                combolist.append(i)
                smallerList.remove(i)
                break

    GCD = 0
    if len(combolist) == 0:
        GCD = 0
    else:
        GCD = functools.reduce(lambda x, y: x*y, combolist)
    return operations, GCD
    
    
def SieveMaker(x):

    """
    Parameters
    ----------
    x : int
        x is either m or no from SieveGCD.

    Description: Where the magic happens. A list is compiled to make a list of prime numbers that, when are multiplied,
                together give you either m or n.
    """

    # Initialize a list
    temp_list = []
    i = 2
    while i <= x:
        if (x % i) == 0:
            temp_list.append(i)
            x = x/i
            i = 2
        else:
            i += 1
    return temp_list


def ScatterTask1():

    """
        Parameters
        ----------
        No inputs

        Description: Scatter plot Euclid's algorithm versus consecutive integer checking
    """

    # Initialize lists
    dev_x = []
    Euclid = []
    Consecutive = []

    # Input of 100 between range 1 to 1000
    for i in range(100):
        n = random.randrange(1, 1000)
        
        # Euclid's Algorithm
        dev_x.append(n)

        # Consecutive Integer GCD
        Euclid.append(EuclidsAvgOpertions(n))
        Consecutive.append(ConInitAvgOperations(n))

    img = plt.figure()
    ax1 = img.add_subplot(111)
    plt.xlabel("n")
    plt.ylabel("Avg Divisions")
    area = np.pi * 3
    ax1.scatter(dev_x, Euclid, area, c='b', alpha=0.5, marker="s", label='MDavg')
    ax1.scatter(dev_x, Consecutive, area, c='r', alpha=0.5, marker="o", label='Mavg')
    plt.legend(loc='upper left')
    plt.show()

    # If ran on a terminal uncomment
    #img.savefig('task1.png')

    
def ScatterTask2():

    """
        Parameters
        ----------
        No inputs

        Description: Scatter plot for worst case of Euclid's Algorithm
    """

    # Initialize two lists
    dev_x = []
    dev_y = []

    # Random input of 100 between range 2 to 500
    for i in range(100):
        n = random.randrange(2, 50)
        
        # Euclid's Algorithm
        dev_x.append(FibSeq(n+1))

        # Consecutive Integer GCD
        M = FibSeq(n+1)
        N = FibSeq(n)
        
        numOfDivisions = Euclids(M, N)
        dev_y.append(numOfDivisions)
        
    img = plt.figure()    
    plt.xlabel("Max (m, n)")
    plt.ylabel("# of Divisions")
    colors = (0, 0, 0)
    area = np.pi * 3
    plt.scatter(dev_x, dev_y, area, colors, alpha=0.5)
    plt.show()

    # If ran on a terminal uncomment
    # img.savefig('task2.png')

def ScatterTask3():

    """
        Parameters
        ----------
        No inputs

        Description: Prints the scatter plot for task 3 aka middle school
    """
    #Initialize two lists
    dev_x = []
    dev_y = []

    #5000 inputs between 2 to 500
    for i in range(5000):
        m = random.randrange(2, 500)
        n = random.randrange(2, 500)

        # Make two prime lists
        pListM = SieveMaker(m)
        pListN = SieveMaker(n)

        # Get the operations
        operations, GCD = SieveGCD(m, n)
        dev_x.append(max(len(pListM), len(pListN)))
        dev_y.append(operations)
    
    img = plt.figure()    
    plt.xlabel("Max (m, n)")
    plt.ylabel("# of Comparisons")
    colors = (0, 0, 0)
    area = np.pi * 3
    plt.scatter(dev_x, dev_y, area, colors, alpha=0.5)
    plt.show()

    # If ran on a terminal uncomment
    #img.savefig('task3.png')
 
    
def main():
    ans = 'y'
    while (ans != 'n'):
        # Request user input of two modes: User Testing Mode or Scatter Plot mode
        print("Choose one of the following modes:")
        print("    User Testing (t)")
        print("    Scatter Plot (s)")

        while True:
            userInput = str(input("Enter: ").lower())

            # Error checking for certain strings
            if userInput.isalpha() or userInput == "t" or userInput == "user testing" or userInput == "s" or userInput == "scatter plot":
                break

        if ((userInput == "t") or (userInput == "user testing")):
            print("(1) MDavg(n) and Davg(n)")
            print("(2) Worst case of Euclids Algorithm")
            print("(3) Compute GCD using Sieve of Eratosthenes")

            # Error checking for ints
            while True:
                try:
                    choice = int(input("Please choice an option to compute: "))
                    break

                except ValueError:
                    print("No valid integer")

            if (choice == 1):

                # Error checking for numbers only
                while True:
                    try:
                        n = int(input("Give me a number: "))
                        break
                    except ValueError:
                        print("Only numbers!!!")
                        print("Try again")

                conInit, euclidAvg = EuclidsConCompare(n)
                # Print the averages
                print("The average operations using Euclid's algorithm is ", conInit)
                print("The average operations using Consecutive integer algorithm is ", euclidAvg)


            elif (choice == 2):

                #Error checking for numbers only
                while True:
                    try:
                        k = int(input("Give me a number: "))
                        break

                    except ValueError:
                        print("Only numbers!!!")
                        print("Try again")

                GCD = EuclidsGCD(k)
                print("GCD(m, n) (where m = F(k+1) and n = F(k) are consecutive elements of the Fibonacci sequence) = ", GCD)

            elif (choice == 3):

                while True:
                    # Error checking for numbers only
                    while True:
                        try:
                            m = int(input("Give me a value for m: "))
                            break

                        except ValueError:
                            print("Only numbers!!!")
                            print("Try again")

                    # Error checking for a lower value of n
                    while True:
                        try:
                            n = int(input("Give me a value for n (that less than m): "))
                            break

                        except ValueError:
                            print("Only numbers!!!")
                            print("Try again")
                    if m > n:
                        break

                operations, GCD = SieveGCD(m, n)
                print("The GCD is:", GCD)


        elif ((userInput == "s") or (userInput == "scatter plot")):

            # Trying to keep it simple in the main
            print("Computing Task 1...")
            ScatterTask1()
            print("Task 1 DONE")
            print("Computing Task 2...")
            ScatterTask2()
            print("Task 2 DONE")
            print("Computing Task 3...")
            ScatterTask3()
            print("Task 3 DONE")

        ans = input("Would you like to do another? (y or n): ")
main()
