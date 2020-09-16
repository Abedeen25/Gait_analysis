import Constants as C
import operator as op
from functools import reduce
import numpy as np
import itertools

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def LoadData():
    fileID = open((C.Constants.TrainingSetFolder+'metadata.txt'), 'r')
    x = fileID.readline().rstrip()
    print(x)
    userCount = int(fileID.readline().rstrip())
    maxFrame = int(fileID.readline().rstrip())
    fileID.close()

    maxAngleCount = ncr(C.Constants.TotalJoints-1, 2)
    #angleDataArray = list(maxFrame, maxAngleCount, userCount)
    userNameArray = ['']*userCount
    userFrameArray = [0]*userCount
    angleDataArray = [[[0 for k in range(userCount)] for j in range(maxAngleCount)] for i in range(maxFrame)]


    for i in range(userCount):
        if(i+1 == 21):
            break
        fileName = C.Constants.TrainingSetFolder+C.Constants.TrainingFileNamePrefix+str(i+1)+'.txt'
        fileID = open(fileName, 'r')
        userName = fileID.readline().rstrip()
        frameCount = int(fileID.readline().rstrip())
       
        userNameArray[i] = userName
        userFrameArray[i] = frameCount
        #print('Username: ',userName)

        for j in range(frameCount):
            temp = fileID.readline().rstrip()
            angleArray = [float(x) for x in temp.split()]
            #angleArray = np.transpose(angleArray)
            #angleDataArray[j,_,i] = angleArray
            for k in range(len(angleArray)):
                angleDataArray[j][k][i] = angleArray[k]
        fileID.close()

    return angleDataArray, userNameArray, userFrameArray,maxFrame,maxAngleCount

