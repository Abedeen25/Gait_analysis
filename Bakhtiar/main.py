import json

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConstants = data['constants'][DATASET]
    constants = data['constants']['general']
    