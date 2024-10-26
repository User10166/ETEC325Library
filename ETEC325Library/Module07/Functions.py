import numpy as np

def runCentralLimitTheorem(A, sampleSize):
    sampleMeans = []
    for i in range(sampleSize):
        sample = np.random.choice(A, size=len(A), replace=True)
        sampleMeans.append(np.mean(sample))

    return np.array(sampleMeans)