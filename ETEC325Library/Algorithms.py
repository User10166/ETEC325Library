import numpy as np

def encodeBacon(word):
    a = np.array([0, 0, 0, 0, 0])
    b = np.array([0, 0, 0, 0, 1])
    c = np.array([0, 0, 0, 1, 0])
    d = np.array([0, 0, 0, 1, 1])
    e = np.array([0, 0, 1, 0, 0])
    f = np.array([0, 0, 1, 0, 1])
    g = np.array([0, 0, 1, 1, 0])
    h = np.array([0, 0, 1, 1, 1])
    i = np.array([0, 1, 0, 0, 0])
    j = np.array([0, 1, 0, 0, 1])
    k = np.array([0, 1, 0, 1, 0])
    l = np.array([0, 1, 0, 1, 1])
    m = np.array([0, 1, 1, 0, 0])
    n = np.array([0, 1, 1, 0, 1])
    o = np.array([0, 1, 1, 1, 0])
    p = np.array([0, 1, 1, 1, 1])
    q = np.array([1, 0, 0, 0, 0])
    r = np.array([1, 0, 0, 0, 1])
    s = np.array([1, 0, 0, 1, 0])
    t = np.array([1, 0, 0, 1, 1])
    u = np.array([1, 0, 1, 0, 0])
    v = np.array([1, 0, 1, 0, 1])
    w = np.array([1, 0, 1, 1, 0])
    x = np.array([1, 0, 1, 1, 1])
    y = np.array([1, 1, 0, 0, 0])
    z = np.array([1, 1, 0, 0, 1])

    alphabetTable = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    encodedList = []
    for index in range(len(word)):
        ithLetter = word[index].upper()
        ithLetterIndex = letterList.index(ithLetter)
        ithTable = alphabetTable[ithLetterIndex]
        encodedList.append(ithTable)

    encodedArray = np.vstack(encodedList)

    return encodedArray

def decodeBacon(arr):
    a = np.array([0, 0, 0, 0, 0])
    b = np.array([0, 0, 0, 0, 1])
    c = np.array([0, 0, 0, 1, 0])
    d = np.array([0, 0, 0, 1, 1])
    e = np.array([0, 0, 1, 0, 0])
    f = np.array([0, 0, 1, 0, 1])
    g = np.array([0, 0, 1, 1, 0])
    h = np.array([0, 0, 1, 1, 1])
    i = np.array([0, 1, 0, 0, 0])
    j = np.array([0, 1, 0, 0, 1])
    k = np.array([0, 1, 0, 1, 0])
    l = np.array([0, 1, 0, 1, 1])
    m = np.array([0, 1, 1, 0, 0])
    n = np.array([0, 1, 1, 0, 1])
    o = np.array([0, 1, 1, 1, 0])
    p = np.array([0, 1, 1, 1, 1])
    q = np.array([1, 0, 0, 0, 0])
    r = np.array([1, 0, 0, 0, 1])
    s = np.array([1, 0, 0, 1, 0])
    t = np.array([1, 0, 0, 1, 1])
    u = np.array([1, 0, 1, 0, 0])
    v = np.array([1, 0, 1, 0, 1])
    w = np.array([1, 0, 1, 1, 0])
    x = np.array([1, 0, 1, 1, 1])
    y = np.array([1, 1, 0, 0, 0])
    z = np.array([1, 1, 0, 0, 1])

    alphabetTable = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = ''
    for index in range(len(arr)):
        ithArray = arr[index]
        searchedIndex = 0
        while searchedIndex < len(alphabetTable) - 1:
            if np.array_equal(ithArray, alphabetTable[searchedIndex]):
                break
            searchedIndex = searchedIndex + 1
        ithAlphabetIndex = searchedIndex
        ithLetter = letterList[ithAlphabetIndex]
        answer = answer + ithLetter

    return answer

def runCentralLimitTheorem(A, sampleSize):
    sampleMeans = []
    for i in range(sampleSize):
        sample = np.random.choice(A, size=len(A), replace=True)
        sampleMeans.append(np.mean(sample))

    return np.array(sampleMeans)

def runBayesTheorem(likelihood, prior, marginal):
    posterior = (likelihood * prior) / marginal
    return posterior

def getLineEquation(xValues, yValues, y="y"):
    if len(yValues.shape) == 1:
        y2 = int(yValues[-1] + 0.5)
        y1 = int(yValues[0] + 0.5)
    elif len(yValues.shape) == 2:
        dim0, dim1 = yValues.shape
        if dim0 == 1:
            yValues = np.squeeze(yValues, axis=0)
        elif dim1 == 1:
            yValues = np.squeeze(yValues, axis=1)
        y2 = int(yValues[-1] + 0.5)
        y1 = int(yValues[0] + 0.5)

    if len(xValues.shape) == 1:
        x2 = int(xValues[-1] + 0.5)
        x1 = int(xValues[0] + 0.5)
    elif len(xValues.shape) == 2:
        dim0, dim1 = xValues.shape
        if dim0 == 1:
            xValues = np.squeeze(xValues, axis=0)
        elif dim1 == 1:
            xValues = np.squeeze(xValues, axis=1)
        x2 = int(xValues[-1] + 0.5)
        x1 = int(xValues[0] + 0.5)

    mn = y2 - y1
    md = x2 - x1
    m = mn / md
    if mn % md == 0:
        if int(m) == 1:
            mString = ''
        elif int(m) == -1:
            mString = '-'
        else:
            mString = str(int(m))
    else:
        if mn < 0 or md < 0:
            mn = abs(mn)
            md = abs(md)
            nf = [i for i in range(1, mn + 1) if mn % i == 0]
            df = [i for i in range(1, md + 1) if md % i == 0]
            cf = [f for f in nf if f in df]
            gcf = cf[-1]
            mn = int(mn / gcf)
            md = int(md / gcf)
            mString = '-' + str(mn) + '/' + str(md)
        else:
            nf = [i for i in range(1, mn + 1) if mn % i == 0]
            df = [i for i in range(1, md + 1) if md % i == 0]
            cf = [f for f in nf if f in df]
            gcf = cf[-1]
            mn = int(mn / gcf)
            md = int(md / gcf)
            mString = str(mn) + '/' + str(md)
    b = -(m * x1) + y1
    if b.is_integer():
        b = int(b)
    else:
        b = int(b * 10.0 + 0.5) / 10.0
    if b < 0:
        bString = ' - ' + str(abs(b))
    elif b > 0:
        bString = ' + ' + str(abs(b))
    elif b == 0:
        bString = ''
    eqnString = y + ' = ' + mString + 'x' + bString
    return eqnString

def getLineFromCoefficients(m, x, b):
    if len(x.shape) == 2:
        dim0, dim1 = x.shape
        if dim0 == 1:
            x = np.squeeze(x, axis=0)
        elif dim1 == 1:
            x = np.squeeze(x, axis=1)
    xSorted = np.sort(x)
    xUnique = np.unique(xSorted)
    y = np.array([m * xValue + b for xValue in xUnique])
    return xUnique, y

def findCommonItemsInLists(primary, secondary):
    return [item for item in primary if item in secondary]

def findUniqueItemsInLists(primary, secondary):
    return [item for item in primary if item not in secondary]
    
    
