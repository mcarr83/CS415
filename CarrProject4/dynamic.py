# A Dynamic Programming based Python
    # Program for 0-1 Knapsack problem
    # Returns the maximum value that can
    # be put in a knapsack of capacity W
class Dynamic:
    def dynamicApproach(self,weights, values, capacity, totalWeights, table):
        """

        :param weights: Values from input w file
        :param vals: Values from input v file
        :param maxWeight: Value from c file
        :param n: number of things
        :param dt: modified from geeksforgeeks version to keep track of subset
        :return:
        """
        # Build table K[][] in bottom up manner
        for i in range(totalWeights+1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    table[i][w] = 0
                elif weights[i-1] <= w:
                    table[i][w] = max(values[i-1] + table[i-1][(w - weights[i-1])], table[i-1][w])
                else:
                    table[i][w] = table[i-1][w]

        return table[totalWeights][capacity]


    def dynamicOptimal(self,weights, capacity, totalWeights, table):
        """

        :param weights: From getting the optimal value
        :param cap: From the c file
        :param n: number of item
        :param dt:
        :return: A subset, in the right order, of optimum.

        Note: Weights are in the wrong order that is why these are iterated in reverse.
        """
        optimal = []
        i = totalWeights
        j = capacity

        while i > 0 and j > 0:
            if table[i][j] > table[i-1][j]:
                optimal.insert(0, i)
                i -=1
                j -= weights[i]
            else:
                i -= 1

        return optimal
