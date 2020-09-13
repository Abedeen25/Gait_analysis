import Constants as C
import numpy as np

def StoreData(userID, userName, angleArray):
    fileName = C.Constants.TrainingSetFolder+C.Constants.TrainingFileNamePrefix+str(userID)+'.txt')
    fileID = open(fileName, 'w')
    sz = np.shape(angleArray)
    totalFrame = sz[0][0]
    totalAngle = sz[0][1]

    fileID.write('{str(userName)}\n{totalFrame}')

    for i in range(totalFrame):
        for j in range(totalAngle):
            fileID.write(angleArray[i][j])
        fileID.write('\n')

    fileID.close()