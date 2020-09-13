import math
import sys
from SingleLink import SingleLink
from Utils import Utils
from InputOutput import InputOutput


if __name__ == "__main__":
    io = InputOutput()
    utils = Utils()

    data = io.csvLoader()

    dist = utils.calcDist(data)

    SingleLink(data).execute()
