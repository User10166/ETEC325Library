import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def getRawTextMLDataFromExcelSpreadsheet(file, useColumnNames=True, categoriesRow=-1, useNumericCategories=False):
    if(useColumnNames):
        headerIndex = 0
    else:
        headerIndex = None

    data = pd.read_excel(file, header=headerIndex, index_col=categoriesRow)
    XRaw = data[data.columns[0]].tolist()
    XRaw = [str(s) for s in XRaw]
    XRaw = [s.replace("\\n", "\n") for s in XRaw]
    XRaw = [s.replace("\\r", "\r") for s in XRaw]
    XRaw = [s.replace("\\t", "\t") for s in XRaw]
    Y = None
    indexList = list(data.index)
    uniqueIndexesList = list(data.index.unique())
    numClasses = len(uniqueIndexesList)
    if(useNumericCategories):
        Y = [int(idx) for idx in indexList]
    else:
        Y = [uniqueIndexesList.index(idx) for idx in indexList]
    namesList = list(data.columns)

    return XRaw, Y, uniqueIndexesList, numClasses, namesList
