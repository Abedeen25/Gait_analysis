import LoadData
import Constants
import numpy as np
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def TopNPairIndex():
    angleDataArray, userNameArray, _ = LoadData.LoadData()
    userCount = len(userNameArray)
    angleCount = ncr(Constants.Constants.TotalJoints,2)
    rankArray = np.zeros((angleCount,2))
    for i in range(angleCount):
        histogram = np.zeros((1,181))
        maxAngle = -1
        for user in range(userCount):
            for j in (angleDataArray):
                print(j[i][user])

TopNPairIndex()
# angleDataArray, userNameArray, _ = LoadData.LoadData()
# print(angleDataArray.shape)