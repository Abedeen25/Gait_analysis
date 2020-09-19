import json
import Train
import Test

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConst = data[DATASET]
    genConst = data['general']
    # Training using the dataset
    Train.train(datasetConst['UserCount'], datasetConst, genConst)
    Test.test('u1s1.txt', datasetConst, genConst)