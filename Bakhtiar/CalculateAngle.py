import numpy as np
import itertools
from math import comb, sqrt, acos

def calculateAngle(data, start, fin, datasetConst, genConst):
    data = np.array(data)
    data = data[:, :, start : fin]
    frameCount = data.shape[2]
    pairCount = comb(genConst['TotalJoints'] - 1, 2)
    angleArray = [[[0] for i in range(pairCount)] for j in range(frameCount)]

    for frame in range(frameCount):
        idx = 0
        spineX = data[datasetConst['HipCenter']][genConst['xCord']][frame]
        spineY = data[datasetConst['HipCenter']][genConst['yCord']][frame]
        spineZ = data[datasetConst['HipCenter']][genConst['zCord']][frame]

        for joint1 in range(genConst['TotalJoints']):
            for joint2 in range(genConst['TotalJoints']):
                if joint1 != datasetConst['HipCenter'] and joint2 != datasetConst['HipCenter'] and joint1 > joint2:
                    j1X = data[joint1][genConst['xCord']][frame]
                    j1Y = data[joint1][genConst['yCord']][frame]
                    j1Z = data[joint1][genConst['zCord']][frame]
                    j2X = data[joint2][genConst['xCord']][frame]
                    j2Y = data[joint2][genConst['yCord']][frame]
                    j2Z = data[joint2][genConst['zCord']][frame]

                    # Law of Cosines
                    Psj1 = sqrt((spineX - j1X) ** 2 + (spineY - j1Y) ** 2 + (spineZ - j1Z) ** 2)
                    Psj2 = sqrt((spineX - j2X) ** 2 + (spineY - j2Y) ** 2 + (spineZ - j2Z) ** 2)
                    Pj1j2 = sqrt((j2X - j1X) ** 2 + (j2Y - j1Y) ** 2 + (j2Z - j1Z) ** 2)

                    numerator = (Psj1 ** 2 + Psj2 ** 2 - Pj1j2 ** 2)
                    denominator = 2 * Psj1 * Psj2
                    angleArray[frame][idx] = acos(numerator / denominator)
                    idx += 1

    return angleArray

