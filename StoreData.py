import Constants as C
import numpy as np

def StoreData(userID, userName, angleArray):
    fileName = str(C.Constants.TrainingSetFolder)+str(C.Constants.TrainingFileNamePrefix)+str(userID)+'.txt'
    fileID = open(fileName, 'w')
    sz = np.shape(angleArray)
    totalFrame = sz[0]
    totalAngle = sz[1]

    fileID.write(str(userName)+'\n'+str(totalFrame)+'\n')

    for i in range(totalFrame):
        for j in range(totalAngle):
            fileID.write(str(angleArray[i][j])+' ')
        fileID.write('\n')

    fileID.close()