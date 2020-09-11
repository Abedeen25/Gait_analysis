import Constants as C
import numpy as np

def CalculateAnkleDistance(data):
    sz = np.shape(data)
    frameCount = sz[0][2]
    ankleDistance = np.zeros(0, frameCount)

    for i in range(frameCount):
        xDiff = data[C.Constants.AnkleLeft][C.Constants.xCord][i] - data[C.Constants.AnkleRight][C.Constants.xCord][i]
        yDiff = data[C.Constants.AnkleLeft][C.Constants.yCord][i] - data[C.Constants.AnkleRight][C.Constants.yCord][i]
        zDiff = data[C.Constants.AnkleLeft][C.Constants.zCord][i] - data[C.Constants.AnkleRight][C.Constants.zCord][i]

        ankleDistance[0][i] = np.sqrt( xDiff**2 + yDiff**2 + zDiff**2)

    return ankleDistance    