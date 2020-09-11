import findWarpPathLength as FWPL
import numpy as np

def DTW(train, test):
    warpPathLength = FWPL.findWarpPathLength(train, test)
    lengthTrain = len(train)
    lengthTest = len(test)

    warpPathLength = max(warpPathLength, abs(lengthTrain - lengthTest))

    distanceMatrix = np.zeros(lengthTrain + 1, lengthTest + 1)

    for i in range(lengthTrain):
        for j in range(max(i-warpPathLength, i), min(i + warpPathLength, lengthTest)):
            cost = abs(train[0][i] - test[0][j])
            distanceMatrix[i][j] = cost + min(distanceMatrix[i][j+1], distanceMatrix[i+1][j], distanceMatrix[i][j])
    
    distance = distanceMatrix[lengthTrain, lengthTest]
    return distance
