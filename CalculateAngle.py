import Constants as C
import itertools

def CalculateAngle(data):
    len_of_dim1 = len(data[0])
    len_of_dim2 = len(data[2])
    totalFrameList = list()
    totalFrameList.append(len_of_dim1)
    totalFrameList.append(len_of_dim2)
    totalFrame = tuple(totalFrameList)
    totalCombination = itertools.combinations(C.Constants.TotalJoints - 1, 2)

    angleArray = zeros(totalFrame, totalCombination);

    for FrameNumber in range(0, totalFrame):
        count = 0
        spineX = data[C.Constants.HipCenter][C.Constants.xCord][FrameNumber]
        spineY = data[C.Constants.HipCenter][C.Constants.yCord][FrameNumber]
        spineZ = data[C.Constants.HipCenter][C.Constants.zCord][FrameNumber]

        for i in range(0, C.Constants.TotalJoints):
            for j in range(0, C.Constants.TotalJoints):
                if i != C.Constants.HipCenter && j != C.Constants.HipCenter && i != j && i > j:
                    iX = data[i][C.Constants.xCord][FrameNumber]
                    iY = data[i][C.Constants.yCord][FrameNumber]
                    iZ = data[i][C.Constants.zCord][FrameNumber]
                    jX = data[j][C.Constants.xCord][FrameNumber]
                    jY = data[j][C.Constants.yCord][FrameNumber]
                    jZ = data[j][C.Constants.zCord][FrameNumber]

                    Psi = sqrt((spineX - iX) * (spineX - iX) + (spineY - iY) * (spineY - iY) + (spineZ - iZ) * (spineZ - iZ))
                    Psj = sqrt((spineX - jX) * (spineX - jX) + (spineY - jY) * (spineY - jY) + (spineZ - jZ) * (spineZ - jZ))
                    Pij = sqrt((iX - jX) .* (iX - jX) + (iY - jY) .* (iY - jY) + (iZ - jZ) .* (iZ - jZ))
                    numerator = (Psi * Psi) + (Psj * Psj) - (Pij * Pij)
                    denominator = 2 * Psi * Psj
                    angle = acos(numerator/ denominator)
                    angleArray[FrameNumber][count] = angle
                    count  = count + 1
    return angleArray