import math
import sys
from Utils import Utils
from InputOutput import InputOutput
from kMeans import kMeans


def removeCopies(data):
    s = set()

    for instance in data:
        s.add(tuple(instance))

    ans = list(s)
    return ans


if __name__ == "__main__":
    io = InputOutput()
    data = io.csvLoader()
    K = int(sys.argv[1])

    dataHasSet = removeCopies(data)
    
    ansNoCopies = kMeans(dataHasSet, K).execute()

    s = {}

    for i in range(len(dataHasSet)):
        instance = dataHasSet[i]
        s[instance] = ansNoCopies[i]

    ans = []

    for instance in data:
        ans.append(s[tuple(instance)])

    io.csvPrint(ans)