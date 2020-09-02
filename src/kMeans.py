import numpy as np
from Utils import Utils

class kMeans:

    def __init__(self, data, K):
        self.data = data
        self.K = K

    # Return: None | [N] with the cluster id of the n-th instance
    def execute(self):
        if(len(self.data) < self.K):
            print('Oh no! DataSize (%d) it is smaller than number of clusters (%d). Check input, nº clusters and duplicate data.' %(len(self.data), self.K))
            return None

        centroid = self.getFirstsCentroids()
        # debug
        # print('first centroids')
        # print(centroid)
        # print()
        dist = self.calcDist(centroid)
        iteration = self.assignToCluster(centroid, self.data, dist)

        for i in range (1,100):
            centroid = self.generateCentroids(iteration)
            if centroid == None:
                # debug
                # print('iteration %d' %i)
                break
            dist = self.calcDist(centroid)
            iteration = self.assignToCluster(centroid, self.data, dist)
            # debug
            # print(iteration)
            # print()
    
        return iteration

    # Return: [K] with centroids data
    def getFirstsCentroids(self):
        return self.__getRandomCentroids(self.data, self.K) 

    # Params: [K] with centroid data
    # Return: [K][N] with distance to k-th centroid to n-th instance
    def calcDist(self, centroid):
        return self.__calcDist(centroid, self.data, self.__euclidianDist)

    # Params: [K] with centroid data 
    #         [N] with instaces data
    #         [K][N] with distance to k-th centroid to n-th instance
    # Return: [N] with the cluster id of the n-th instance
    def assignToCluster(self, centroid, data, dist): 
        n = len(data)
        k = len(centroid)

        ans = [-1 for j in range(n)]

        for instIdx in range(n):
            closerCentroidIdx = 0
            
            for centroidIdx in range(1,k):
                if dist[centroidIdx][instIdx] < dist[closerCentroidIdx][instIdx]:
                    closerCentroidIdx = centroidIdx

            ans[instIdx] = closerCentroidIdx

        return ans

    # Params: [N] with the cluster id of the n-th instance
    # Return: [K] with the new centroids data
    def generateCentroids(self, clusterId):
        return self.__generateCentroids(self.data, clusterId , len(self.data[0]), self.K)

    def __generateCentroids(self,data, clusterId, instSize, K):
        k = K

        dataSize = len(clusterId)

        centroid = [ [0 for j in range(instSize)] for i in range(k)]

        for centroidIdx in range(k):
            count = 0

            for instIdx in range(dataSize):
                if centroidIdx == clusterId[instIdx]:
                    for attrIdx in range(instSize):
                        centroid[centroidIdx][attrIdx]+=data[instIdx][attrIdx]
                    count+=1

            if count == 0:
                print('Oh no! We have a empty cluster. This algo is not ready for this.')
                # debug
                # instIdx = dataSize
                # print("............")
                # clusterId.sort()
                # xxx = set()

                # for xx in clusterId:
                #     xxx.add(xx)
                # print(xxx)
                # print("............")

                return None

            for attrIdx in range(instSize):
                centroid[centroidIdx][attrIdx] /= count


        return centroid

    def __getRandomCentroids(self, data, k):
        randPerm = np.random.permutation(len(data))
        randPerm = randPerm[0:k]

        centroid = []

        for idx in randPerm:
            centroid.append(data[idx])


        return centroid

    def __calcDist(self,centroid, data, method):
        n = len(data)
        k = len(centroid)
        
        matDist = [ [-1 for j in range(n)] for i in range(k)]

        for i in range(k):
            for j in range(n):
                matDist[i][j] = method(centroid[i], data[j])
            
        return matDist

    def __euclidianDist(self, a, b):
        return Utils.euclidianDist(a, b, len(self.data[0]))

   