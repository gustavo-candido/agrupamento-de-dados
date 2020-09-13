import math

class Utils:
 
    def euclidianDist(self, a, b):
        sum = 0.0
        n = len(a)

        for i in range(n):
            sum+=(a[i]-b[i])*(a[i]-b[i])

        return math.sqrt(sum)

    def calcDist(self,data):
        #return [[0,2,6,10,9], [2,0,5,9,8], [6,5,0,4,5], [10,9,4,0,3], [9,8,5,3,0]]

        n = len(data)        
        matrix = [[(1<<32) for j in range(n)] for i in range(n)]

        for i in range(n):
            matrix[i][i] = 0

        for i in range(n):
            for j in range(n): 
                matrix[i][j] = self.euclidianDist(data[i], data[j])

        return matrix
    
    
    