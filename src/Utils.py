import math

class Utils:
    def euclidianDist(a, b, attrSize):
        sum = 0.0
        n = attrSize

        for i in range(n):
            sum+=(a[i]-b[i])*(a[i]-b[i])

        return math.sqrt(sum)

    