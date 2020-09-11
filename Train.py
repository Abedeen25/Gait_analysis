import Constants
import numpy as np

def Train(userCount):
    maxFrame = 0
    for id in range (0,userCount+1):
        userName = str(id+1)
        FileLocation = Constants.Constants.DataSetFolder+"UPCV\action_"
        fileID = open(FileLocation+str((id*2)+1)+'.txt','r')
        frameCount = float(fileID.readline().rstrip())
        data = np.zeros(Constants.Constants.TotalJoints, Constants.Constants.Coordinates , frameCount)

        for i in range(0,frameCount+1):
            arr = fileID.readline().rstrip()
            x = [float(x) for x in arr.split()]
            for j in range(0,Constants.Constants.TotalJoints+1):
                data[j, 1, i] = x[3*j - 2, 1]
                data[j, 2, i] = x[3*j - 1, 1]
                data[j, 3, i] = x[3*j , 1]
            