import sys
import os
import Preprocess
import LoadData
import TopNPairIndex
import DTW

def test(fileName, datasetConst, genConst):
    currentFolderName = os.getcwd()
    fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], fileName)
    preprocessedTestData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
    trainData, metaData = LoadData.loadData(genConst)

    topNPairIndex = metaData["TopNPairIndex"]
    topNTestPairFrames = TopNPairIndex.extractTopNIndex(preprocessedTestData, topNPairIndex)
    
    userCount = len(trainData)
    storeMismatch = [sys.float_info.max] * (userCount + 1)
    
    for user in range(1, userCount + 1):
        storedTrainFrameCount = trainData[str(user)][0]
        storedTrainData = trainData[str(user)][1]
        testData = topNTestPairFrames
        testFrameCount = frameCount
        totalMismatch = 0
        for idx in range(metaData["N"]):
            trainDTW = []
            testDTW = []
            for frame in range(storedTrainFrameCount):
                trainDTW.append(storedTrainData[frame][idx])
            for frame in range(testFrameCount):
                testDTW.append(testData[frame][idx])
            totalMismatch += DTW.dtw(trainDTW, testDTW)
        storeMismatch[user] = totalMismatch
    
    detectedUser = storeMismatch.index(min(storeMismatch))
    print(detectedUser)
