import math

def calculateAnkleDistance(data, frameCount, datasetConst, genConst):
    ankleDistance = [0] * frameCount

    for frame in range(frameCount):
        xDiff = data[datasetConst['AnkleLeft']][genConst['xCord']][frame] - data[datasetConst['AnkleRight']][genConst['xCord']][frame]
        yDiff = data[datasetConst['AnkleLeft']][genConst['yCord']][frame] - data[datasetConst['AnkleRight']][genConst['yCord']][frame]
        zDiff = data[datasetConst['AnkleLeft']][genConst['zCord']][frame] - data[datasetConst['AnkleRight']][genConst['zCord']][frame]
        

        ankleDistance[frame] = math.sqrt(xDiff ** 2 + yDiff ** 2 + zDiff ** 2)

    return ankleDistance
