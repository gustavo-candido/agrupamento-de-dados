import math
import sys
from SingleLink import SingleLink
from Utils import Utils
from InputOutput import InputOutput


if __name__ == "__main__":
    io = InputOutput()
    utils = Utils()
    
    # abrindo arquivo csv
     data = io.csvLoader()
   
    # executando single link
    SingleLink(data).execute()
