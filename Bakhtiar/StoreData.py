import os
import json
from math import comb

def storeData(data, topNPairIndex, genConst):
    userCount = len(data)
    dataForStoring = {}
    pairCount = comb(genConst['TotalJoints'] - 1, 2)
    maxFrames = -1;
    for user in range(1, userCount + 1):
        frameCount = data[str(user)][0]
        maxFrames = max(frameCount, maxFrames)
        dataArray = data[str(user)][1]
        topNPairFrames = []
        for frame in dataArray:
            topNPairs = []
            for idx in topNPairIndex:
                topNPairs.append(frame[idx])
            topNPairFrames.append(topNPairs)
        dataForStoring[str(user)] = []
        dataForStoring[str(user)].append(frameCount)
        dataForStoring[str(user)].append(topNPairFrames)
    currentFolderName = os.getcwd()
    trainingSetFileName = "train.json"
    trainingFileWithPath = os.path.join(currentFolderName, genConst['TrainingSetFolder'], trainingSetFileName)
    with open(trainingFileWithPath, 'w') as outFile:
        json.dump(dataForStoring, outFile)

    meta = {}
    meta["UserCount"] = userCount
    meta["MaxFrames"] = maxFrames
    meta["N"] = len(topNPairIndex)
    meta["TopNPairIndex"] = topNPairIndex
    metadataFileName = "metadata.json"
    metadataFileWithPath = os.path.join(currentFolderName, genConst['TrainingSetFolder'], metadataFileName)
    with open(metadataFileWithPath, 'w') as outFile:
        json.dump(meta, outFile)
        
