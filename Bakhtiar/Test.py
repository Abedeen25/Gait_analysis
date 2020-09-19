import os
import Preprocess

def test(fileName, genConst):
    currentFolderName = os.getcwd()
    fileNameWithPath = os.path.join(currentFolderName, genConst['DatasetFolder'], datasetConst['Folder'], fileName)
    preprocessedTestData, frameCount = Preprocess.preprocess(fileNameWithPath, datasetConst, genConst)
    