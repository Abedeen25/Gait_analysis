import json
import train

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConstants = data['constants'][DATASET]
    constants = data['constants']['general']
    # Training using the dataset
    