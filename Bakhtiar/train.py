import os

def train(userCount, datasetConst, genConst):
    maxFrameCount = 0
    for fileName in range(1, userCount + 1):
        currentFolderName = os.getcwd()
        currentFileName = "u" + str(fileName) + "s1.txt"
        fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], currentFileName)
        
        dataFile = open(fileNameWithPath, "r")
        frameCount = int(dataFile.readline().rstrip())
        data = [[[[0] for k in frameCount] for j in genConst['CoordinatesCount']] for i in genConst['TotalJoints']]
        for frame in range(frameCount):
            framePoints = dataFile.readline().rstrip()
            framePoints = [float(x) for x in framePoints.split()]
            for joint in range(genConst['TotalJoints']):
                data[joint][genConst['xCoord']][frame] = framePoints[3 * joint]
                data[joint][genConst['yCoord']][frame] = framePoints[3 * joint + 1]
                data[joint][genConst['yCoord']][frame] = framePoints[3 * joint + 2]
        



