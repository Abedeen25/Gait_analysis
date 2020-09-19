import os
import math
import json
import Preprocess
import TopNPairIndex
import StoreData

def train(userCount, datasetConst, genConst):
    dataFromFile = {}
    for userID in range(1, userCount + 1):
        currentFolderName = os.getcwd()
        currentFileName = "u" + str(userID) + "s1.txt"
        fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], currentFileName)
        preprocessedTrainData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
        dataFromFile[str(userID)] = []
        dataFromFile[str(userID)].append(frameCount)
        dataFromFile[str(userID)].append(preprocessedTrainData)
    topNPairIndex = TopNPairIndex.topNPairIndex(dataFromFile, genConst)
    StoreData.storeData(dataFromFile, topNPairIndex, genConst)

        
    
