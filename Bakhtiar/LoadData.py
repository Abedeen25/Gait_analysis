import os
import json

def loadData(genConst):
    data = {}
    currentFolderName = os.getcwd()
    trainingSetFileName = "train.json"
    trainingFileWithPath = os.path.join(currentFolderName, genConst['TrainingSetFolder'], trainingSetFileName)
    with open(trainingFileWithPath) as inFile:
        data = json.load(inFile)
    meta = {}
    metadataFileName = "metadata.json"
    metadataFileWithPath = os.path.join(currentFolderName, genConst['TrainingSetFolder'], metadataFileName)
    with open(metadataFileWithPath) as inFile:
        meta = json.load(inFile)
    return data, meta