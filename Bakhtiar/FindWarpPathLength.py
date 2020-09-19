def findWarpPathLength(train, test):
    maxThetaTrain = -1
    maxThetaTest = -1

    for i in range(len(train)):
        if(maxThetaTrain < abs(train[i])):
            maxThetaTrain = abs(train[i])

    for i in range(len(test)):
        if (maxThetaTest < abs(test[i])):
            maxThetaTest = abs(test[i])

    maxOfBoth = max(maxThetaTrain, maxThetaTest)
    absTrainPlusTest = maxThetaTrain + maxThetaTest

    L = int(round((maxOfBoth + absTrainPlusTest) / 2))
    return L