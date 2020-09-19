import os
import Preprocess
import LoadData

def test(fileName, datasetConst, genConst):
    currentFolderName = os.getcwd()
    fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], fileName)
    preprocessedTestData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
    trainData, metaData = LoadData.loadData(genConst)

    N = metaData["N"]
    topNPairIndex = metaData["TopNPairIndex"]
    topNTestPairFrames = []
    for frame in preprocessedTestData:
        topNTestPair = []
        for idx in topNPairIndex:
            topNTestPair.append(frame[idx])
        topNTestPairFrames.append(topNPairs)
    
