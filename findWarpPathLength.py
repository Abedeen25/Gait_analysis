
def findWarpPathLength(train, test):
    maxThetaTrain = -1
    maxThetaTest = -1

    for i in range(len(train)):
        if(maxThetaTrain < abs(train[1][i])):
            maxThetaTrain = abs(train[1][i])

    for i in range(len(test)):
        if (maxThetaTest < abs(test[1][i])):
            maxThetaTest = abs(test[1][i])

    maxOfBoth = max(maxThetaTrain, maxThetaTest)
    absTrainPlusTest = maxThetaTrain + maxThetaTest

    L = round((maxOfBoth + absTrainPlusTest) / 2)
    return L