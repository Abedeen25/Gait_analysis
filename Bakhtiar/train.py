import os
import math
import json
import Preprocess

def train(userCount, datasetConst, genConst):
    maxFrameCount = 0
    dataFromFile = {}
    for userID in range(1, userCount + 1):
        currentFolderName = os.getcwd()
        currentFileName = "u" + str(userID) + "s1.txt"
        fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], currentFileName)
        preprocessedTrainData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
        maxFrameCount = max(frameCount, maxFrameCount)
        dataFromFile[str(userID)] = []
        dataFromFile[str(userID)].append(frameCount)
        dataFromFile[str(userID)].append(preprocessedTrainData)
    
        
    
