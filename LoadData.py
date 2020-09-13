import Constants as C
import numpy as np
import itertools

def LoadData():
    fileID = open((C.Constants.TestSetFolder+'metadata.txt'), 'r')
    userCount = float(fileID.readline().rstrip())
    maxFrame = float(fileID.readline().rstrip())
    fileID.close()

    maxAngleCount = itertools.combinations(C.Constants.TotalJoints-1, 2)
    angleDataArray = np.zeros(maxFrame, maxAngleCount, userCount)
    userNameArray = ['']*userCount
    userFrameArray = np.zeros(0, userCount)

    for i in range(userCount):
        fileName = C.Constants.TrainingSetFolder+C.Constants.TrainingFileNamePrefix+str(i)+'.txt'
        fileID = open(fileName, 'r')
        userName = fileID.readline().rstrip()
        frameCount = float(fileID.readline().rstrip())
        userNameArray[i] = userName
        userFrameArray[i] = frameCount

        for j in range(frameCount):
            temp = fileID.readline().rstrip()
            angleArray = [float(x) for x in temp.split()]
            angleArray = np.transpose(angleArray)
            angleDataArray[j][:][i] = angleArray
        fileID.close()

    return angleDataArray, userNameArray, userFrameArray