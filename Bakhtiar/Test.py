import os
import Preprocess
import LoadData
import TopNPairIndex

def test(fileName, datasetConst, genConst):
    currentFolderName = os.getcwd()
    fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], fileName)
    preprocessedTestData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
    trainData, metaData = LoadData.loadData(genConst)

    N = metaData["N"]
    topNPairIndex = metaData["TopNPairIndex"]
    topNTestPairFrames = TopNPairIndex.extractTopNIndex(preprocessedTestData, topNPairIndex)
    
    
    
