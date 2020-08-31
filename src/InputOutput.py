import math

class InputOutput:
    def csvLoader(self):
        data = []

        while True:
            try:
                line = input()
                data.append(list(map(float,line.strip().split(','))))

            except EOFError:
                break
        
        return data
    
    def csvPrint(self,cluster):
        flag = False

        for instanceCluster in cluster:
            if flag:
                print(', ', end='')
            print(instanceCluster, end='')
            flag = True
        print()
