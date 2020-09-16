import numpy as np
from Utils import Utils

class SingleLink:

    def __init__(self, data):
        self.data = data


    def execute(self):
        utils = Utils()
        # calcula-se a matriz de distância
        distanceMatrix = utils.calcDist(self.data)
        n = len(distanceMatrix)
        # Valid é um conjunto iniciado com todos os índices de 0 até n-1, sendo a matriz de distância nxn
        valid = set()

        for i in range(n):
            valid.add(i)

        ans = {}
        # Inicializa-se o dicionário de respostas 
        for i in range(n):
            s = set()
            s.add(i)
            ans[i] = s
        
        # Print do primeiro grupo formado por todos os elementos
        flag = False
        for value in ans:
            if flag:
                print(', ', end='')
            print(ans[value], end='')
            flag = True
        print()

        # A cada iteração deste loop, encontra-se o par de grupos a e b com menor distância,  
        # os quais são agrupados no dicionário de resposta.
        # Para cada elemento x que ainda está no set valid, atualiza-se a matriz de distância na posição
        # [x][a], [x][b] e [a][x] para o mínimo entre os valores atuais de [x][a] e [x][b].
        # Por fim, é retirado (arbitrariamente) do set valid o maior índice (a ou b). 
        for i in range(n-1):
            a,b = self.findLowest(distanceMatrix, valid)

            ans[min(a,b)] = ans[a].union(ans[b])
            del ans[max(a,b)]

            # É printado o estado atual dos grupos
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


    # Encontra-se a menor distância da matriz de distância
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


        
    
