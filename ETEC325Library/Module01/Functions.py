import pandas as pd
import matplotlib.pyplot as plt

def readExcelSpreadsheet(file, useColumnNames=True, useRowLabels=False):
    if(useColumnNames):
        headerIndex = 0
    else:
        headerIndex = None

    if(useRowLabels):
        rowIndex = 0
    else:
        rowIndex = None
    data = pd.read_excel(file, header=headerIndex, index_col=rowIndex)
    dataNumbers = data.to_numpy()
    indexList = list(data.index)
    namesList = list(data.columns)

    return dataNumbers, indexList, namesList

    
def plotHistogram(data, bins=None, title=None, xAxisTitle=None, yAxisTitle=None, save=False, saveDir=None):
    plt.hist(data, bins=bins)
    if(title is not None):
        plt.title(title)
    if(xAxisTitle is not None):
        plt.xlabel(xAxisTitle)
    if(yAxisTitle is not None):
        plt.ylabel(yAxisTitle)

    if(save and saveDir is not None):
        plt.savefig(saveDir)

    plt.show()

    plt.clf()
    plt.gcf()