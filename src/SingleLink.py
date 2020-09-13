import numpy as np
from Utils import Utils

class SingleLink:

    def __init__(self, data):
        self.data = data


    def execute(self):
        utils = Utils()
        distanceMatrix = utils.calcDist(self.data)
        n = len(distanceMatrix)

        valid = set()
        for i in range(n):
            valid.add(i)

        ans = {}

        for i in range(n):
            s = set()
            s.add(i)
            ans[i] = s

        flag = False
        for value in ans:
            if flag:
                print(', ', end='')
            print(ans[value], end='')
            flag = True
        print()

        for i in range(n-1):
            a,b = self.findLowest(distanceMatrix, valid)

            ans[min(a,b)] = ans[a].union(ans[b])
            del ans[max(a,b)]

            flag = False
            for value in ans:
                if flag:
                  print(', ', end='')
                print(ans[value], end='')
                flag = True
            print()
            for x in valid:
                distanceMatrix[x][a] = distanceMatrix[a][x] = distanceMatrix[x][b] =  min(distanceMatrix[x][a], distanceMatrix[x][b])

            valid.remove(max(a,b))



    def findLowest(self, data, valid):
        it = iter(valid)

        x = next(it)
        y = next(it)

        for i in valid:
            for j in valid:
                if i == j:
                    continue

                if data[i][j] < data[x][y]:
                    x,y = i,j

        return x,y


        
    
