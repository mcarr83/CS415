class Heap:
    def __init__(self):
        #Used for operation counting
        self.heapOperations = 0

    def deleteMax(self,values,weights):
        totalValues = len(values)
        maxIndex = totalValues -1

        #Swap first and last items
        valueTemp = values[0]
        values[0] = values[maxIndex]
        values[maxIndex] = valueTemp

        weightTemp = weights[0]
        weights[0] = weights[maxIndex]
        weights[maxIndex] = weightTemp

        #Delete max value
        values.pop()
        weights.pop()
        totalValues = len(values)
        #Resort the Heap
        self.heapSort(values,weights,totalValues)

    def heapApproach(self,values, weights, maxWeight, optValues):
        totalValue = 0
        totalWeight = 0
        for i in range(len(values)):
            if (totalWeight + weights[0]) >= maxWeight:
                break
            else:
                totalWeight += weights[0]
                totalValue += values[0]
                #Append values used for optimal value    
                optValues.append(values[0])
            self.deleteMax(values,weights)

        return totalValue
    def createMaxHeap(self, values, weights, totalValues, root):
        """
        :param values: Values from input v file
        :param weights: Values from input w file
        :param totalValues: The number of values
        :param root:
        :return: None
        """

        max = root
        leftChild = 2 * root + 1
        rightChild = 2 * root + 2
    
        self.heapOperations+=1
        if (leftChild) < totalValues and (values[root] / weights[root] > values[leftChild] / weights[leftChild]):
            max = leftChild

        if (rightChild) < totalValues and (values[max] / weights[max] > values[rightChild] / weights[rightChild] ):
            max = rightChild

        if max != root:
            #Swap values
            valueTemp = values[root]
            values[root] = values[max]
            values[max] = valueTemp
            #Swap weights to match values
            weightTemp = weights[root]
            weights[root] = weights[max]
            weights[max] = weightTemp

            #recursively sift root
            self.createMaxHeap(values, weights, totalValues, max)

    
    def heapSort(self, values, weights, totalValues):
        """
        :param values: Values from input v file
        :param weights: Values from input w file
        :param totalValues: Number of items
        :return:
        """

        # Create max heap
        for i in range(totalValues, -1, -1):
            self.createMaxHeap(values, weights, totalValues, i)

        for i in range(totalValues-1, 0, -1):
            #Swap values
            valueTemp = values[i]
            values[i] = values[0]
            values[0] = valueTemp

            #Swap weights to match values
            weightTemp = weights[i]
            weights[i] = weights[0]
            weights[0] = weightTemp
            self.createMaxHeap(values, weights, i, 0)

    

    
