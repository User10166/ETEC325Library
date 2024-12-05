import numpy as np
import pandas as pd
import sys

stdoutInstance = sys.stdout

class Logger(object):
    def __init__(self, file):
        self.terminal = sys.stdout
        self.log = open(file, "w")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

def enableLogging(file):
    sys.stdout = Logger(file)

def disableLogging():
    sys.stdout = stdoutInstance

def createRange(start, stop, step=1):
    inclusiveRange = np.arange(start, stop + step, step)
    rangeShape = inclusiveRange.shape
    return np.reshape(inclusiveRange, (1, rangeShape[0]))
    
def printTable(array, columnNames=None):
    arrayShape = array.shape
    if(len(arrayShape) == 1):
        array = np.reshape(array, (1, arrayShape[0]))
        arrayShape = array.shape
    if(columnNames is None):
        if(len(arrayShape) == 1):
            numRows = int(arrayShape[0])
            blankRows = ['' for i in range(numRows)]
            df = pd.DataFrame(array, index=blankRows, columns=[''])
        elif(len(arrayShape) > 1):
            numRows = int(arrayShape[0])
            blankRows = ['' for i in range(numRows)]
            numColumns = int(arrayShape[1])
            blankColumns = ['' for i in range(numColumns)]
            df = pd.DataFrame(array, index=blankRows, columns=blankColumns)
    else:
        numRows = int(arrayShape[0])
        blankRows = ['' for i in range(numRows)]
        df = pd.DataFrame(array, index=blankRows, columns=columnNames)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    print(df)
    
def printVariable(label, var, columnNames=None):
    if(type(var) is np.ndarray):
        print("\n" + label + ":")
        printTable(var, columnNames)
    else:
        print("\n" + label + ": " + str(var))
        
