import LoadData
import Constants
import numpy as np
import math
from functools import reduce
import operator as op

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def TopNPairIndex():
    topNIndex = []
    angleDataArray, userNameArray, userFrameArray,maxFrame,maxAngleCount = LoadData.LoadData()
    userCount = len(userNameArray)
    angleCount = maxAngleCount
    rankArray = np.zeros((angleCount,2))
    
    
    for i in range(angleCount):
        angleArray = []
        histogram = np.zeros((181))
        maxAngle = -1
        for user in range(userCount):
            for j in range(maxFrame):
                angleArray.append(angleDataArray[j][i][user])
        #angleArray = np.transpose(angleArray)
        angleArray = angleArray[np.min(np.nonzero(angleArray)) : np.max(np.nonzero(angleArray))]
        frameCount = len(angleArray)
        for k in range(frameCount):
            angle = int((round((angleArray[k]) * 180 )) / math.pi)
            angle = angle + 1
            maxAngle = max(angle , maxAngle)
            histogram[angle] = histogram[angle] + 1
        count = 0
        for j in range(maxAngle):
            if(histogram[j] != 0):
                count = count + 1
        rankArray[i][0] = i
        rankArray[i][1] = count

    for b in range(angleCount):
        for j in range(angleCount-1):
            if(rankArray[j][1] < rankArray[j+1][1]):
                temp = rankArray[j]
                rankArray[j] = rankArray[j+1]
                rankArray[j+1] = temp      
    
    for a in rankArray:
        if (a[1] > Constants.Constants.MinBin):
            topNIndex.append(a[0])

    return topNIndex