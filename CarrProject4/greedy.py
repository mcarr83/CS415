

class Greedy:
    def __init__(self):
        #Used for operation counting
        self.greedyOperations = 0


    def greedyApproach(self,values, maxWeight, weights, greedyValues):
        totalValue = 0
        totalWeight = 0
        for i in range(len(values)):
            if (totalWeight + weights[i]) >= maxWeight:
                break
            else:
                totalWeight += weights[i]
                totalValue += values[i]
                #Append values used for optimal value    
                greedyValues.append(values[i])

        return totalValue

    def partition(self,left, right, values, weights):
        """
        Partition step for quickSort
        """
        i = (left-1)
        pivot = values[right]/weights[right]

        for j in range(left, right):
            self.greedyOperations += 1
            if values[j]/weights[j] >= pivot:
                i+=1

                #Swap values
                vTemp = values[i]
                values[i] = values[j]
                values[j] = vTemp

                #Swap weights to match values
                wTemp = weights[i]
                weights[i] = weights[j]
                weights[j] = wTemp

        #Swap values
        vTemp = values[i+1]
        values[i+1] = values[right]
        values[right] = vTemp

        #Swap weights to match values
        wTemp = weights[i+1]
        weights[i+1] = weights[right]
        weights[right] = wTemp

        return i+1

    def quickSort(self,left, right, values, weights):
        self.greedyOperations += 1
        if left < right:
            part = self.partition(left, right, values, weights)
            self.quickSort(left, part - 1, values, weights)
            self.quickSort(part + 1, right, values, weights)

