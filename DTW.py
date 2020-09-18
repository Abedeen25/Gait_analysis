import findWarpPathLength as FWPL
import numpy as np

def DTW(train, test):
    warpPathLength = FWPL.findWarpPathLength(train, test)
    lengthTrain = len(train)
    lengthTest = len(test)

    warpPathLength = max(warpPathLength, abs(lengthTrain - lengthTest))
    #print("warpPathLength: ",warpPathLength)
    distanceMatrix = np.zeros((lengthTrain + 1, lengthTest + 1))

    for i in range(1, lengthTrain):
        # for j in range(max(i-warpPathLength, i), min(i + warpPathLength, lengthTest)):
        for j in range(1, lengthTest):
            cost = abs(train[i] - test[j])
            distanceMatrix[i][j] = cost + min(distanceMatrix[i][j-1], distanceMatrix[i-1][j], distanceMatrix[i-1][j-1])
    #print(distanceMatrix)
    distance = distanceMatrix[lengthTrain - 1, lengthTest - 1]
    return distance

