import json
import train

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConst = data[DATASET]
    genConst = data['general']
    print(type(datasetConst))
    # Training using the dataset
    train.train(datasetConst['UserCount'], datasetConst, genConst)