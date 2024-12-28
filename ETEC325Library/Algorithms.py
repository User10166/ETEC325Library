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
        while(searchedIndex < len(alphabetTable) - 1):
            if(np.array_equal(ithArray, alphabetTable[searchedIndex])):
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

def getLineEquation(xValues, yValues):
    y2 = yValues[-1]
    y1 = yValues[0]
    x2 = xValues[-1]
    x1 = xValues[0]

    mn = y2 - y1
    md = x2 - x1
    m = mn / md
    if mn % md == 0:
        mString = str(int(m))
    else:
        if mn < 0 or md < 0:
            mString = '-' + str(abs(mn)) + '/' + str(abs(md))
        else:
            mString = str(mn) + '/' + str(md)
    b = -(m * x1) + y1
    if(b < 0):
        bString = '- ' + str(b)
    else:
        bString = '+ ' + str(b)
    eqnString = 'y = ' + mString + 'x ' + bString
    return eqnString
    
    
