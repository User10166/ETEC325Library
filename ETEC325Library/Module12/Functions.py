import pandas as pd


def getMLDataFromExcelSpreadsheet(file, useColumnNames=True, categoriesRow=-1, useNumericCategories=False):
    if(useColumnNames):
        headerIndex = 0
    else:
        headerIndex = None

    data = pd.read_excel(file, header=headerIndex, index_col=categoriesRow)
    X = data.to_numpy()
    Y = None
    indexList = list(data.index)
    uniqueIndexesList = list(data.index.unique())
    numClasses = len(uniqueIndexesList)
    if(useNumericCategories):
        Y = [int(idx) for idx in indexList]
    else:
        Y = [uniqueIndexesList.index(idx) for idx in indexList]
    namesList = list(data.columns)

    return X, Y, uniqueIndexesList, numClasses, namesList