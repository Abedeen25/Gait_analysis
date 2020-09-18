import os
import math
import CalculateAnkleDistance
import AverageFilter

def train(userCount, datasetConst, genConst):
    maxFrameCount = 0
    for fileName in range(1, userCount + 1):
        currentFolderName = os.getcwd()
        currentFileName = "u" + str(fileName) + "s1.txt"
        fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], currentFileName)
        
        dataFile = open(fileNameWithPath, "r")
        frameCount = int(dataFile.readline().rstrip())
        data = [[[[0] for k in range(frameCount)] for j in range(genConst['CoordinatesCount'])] for i in range(genConst['TotalJoints'])]
        for frame in range(frameCount):
            framePoints = dataFile.readline().rstrip()
            framePoints = [float(x) for x in framePoints.split()]
            for joint in range(genConst['TotalJoints']):
                data[joint][genConst['xCord']][frame] = framePoints[3 * joint]
                data[joint][genConst['yCord']][frame] = framePoints[3 * joint + 1]
                data[joint][genConst['zCord']][frame] = framePoints[3 * joint + 2]
        ankleDistance = CalculateAnkleDistance.calculateAnkleDistance(data, frameCount, datasetConst, genConst)
        smoothAnkleDistance = AverageFilter.averageFilter(data, math.floor(len(ankleDistance)/datasetConst['SpanDivide']))
        print(smoothAnkleDistance)



