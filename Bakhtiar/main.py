import json
import Train

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConst = data[DATASET]
    genConst = data['general']
    # Training using the dataset
    Train.train(datasetConst['UserCount'], datasetConst, genConst)