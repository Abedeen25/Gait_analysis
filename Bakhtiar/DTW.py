import FindWarpPathLength as FWPL
import numpy as np

def dtw(train, test):
    lenTrain = len(train)
    lenTest = len(test)
    warpPathLength = max(FWPL.findWarpPathLength(train, test), abs(lenTrain - lenTest))

    distanceMatrix = np.zeros((lenTrain + 1, lenTest + 1))

    for i in range(1, lenTrain):
        #for j in range(max(i - warpPathLength, i), min(i + warpPathLength, lenTest)):
        for j in range(1, lenTest):
            cost = abs(train[i] - test[j])
            distanceMatrix[i][j] = cost + min(distanceMatrix[i][j-1], distanceMatrix[i-1][j], distanceMatrix[i-1][j-1])
    return distanceMatrix[lenTrain - 1][lenTest - 1]
    