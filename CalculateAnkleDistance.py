import Constants as C
import numpy as np

def CalculateAnkleDistance(data):
    sz = len(data)
    frameCount = sz[1][3]
    ankleDistance = np.zeros(1, frameCount)

    for i in range(frameCount):
        xDiff = data[C.Constants.AnkleLeft][C.Constants.xCord][i] - data[C.Constants.AnkleRight][C.Constants.xCord][i]
        yDiff = data[C.Constants.AnkleLeft][C.Constants.yCord][i] - data[C.Constants.AnkleRight][C.Constants.yCord][i]
        zDiff = data[C.Constants.AnkleLeft][C.Constants.zCord][i] - data[C.Constants.AnkleRight][C.Constants.zCord][i]

        ankleDistance[1][i] = np.sqrt( xDiff**2 + yDiff**2 + zDiff**2)

    return ankleDistance    