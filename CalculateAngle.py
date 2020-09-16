import Constants as C
import itertools
import numpy as np
import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def CalculateAngle(data):
    totalFrame = data.shape[2]
    
    totalCombination = ncr(C.Constants.TotalJoints - 1, 2)

    angleArray = np.zeros((totalFrame, totalCombination))

    for FrameNumber in range(0, totalFrame):
        count = 0
        spineX = data[C.Constants.HipCenter][C.Constants.xCord][FrameNumber]
        spineY = data[C.Constants.HipCenter][C.Constants.yCord][FrameNumber]
        spineZ = data[C.Constants.HipCenter][C.Constants.zCord][FrameNumber]

        for i in range(0, C.Constants.TotalJoints):
            for j in range(0, C.Constants.TotalJoints):
                if i != C.Constants.HipCenter and j != C.Constants.HipCenter and i != j and i > j:
                    iX = data[i][C.Constants.xCord][FrameNumber]
                    iY = data[i][C.Constants.yCord][FrameNumber]
                    iZ = data[i][C.Constants.zCord][FrameNumber]
                    jX = data[j][C.Constants.xCord][FrameNumber]
                    jY = data[j][C.Constants.yCord][FrameNumber]
                    jZ = data[j][C.Constants.zCord][FrameNumber]

                    Psi = math.sqrt((spineX - iX) * (spineX - iX) + (spineY - iY) * (spineY - iY) + (spineZ - iZ) * (spineZ - iZ))
                    Psj = math.sqrt((spineX - jX) * (spineX - jX) + (spineY - jY) * (spineY - jY) + (spineZ - jZ) * (spineZ - jZ))
                    Pij = math.sqrt((iX - jX) * (iX - jX) + (iY - jY) * (iY - jY) + (iZ - jZ) * (iZ - jZ))
                    numerator = (Psi * Psi) + (Psj * Psj) - (Pij * Pij)
                    denominator = 2 * Psi * Psj
                    angle = math.acos(numerator/ denominator)
                    angleArray[FrameNumber][count] = angle
                    count  = count + 1
    return angleArray