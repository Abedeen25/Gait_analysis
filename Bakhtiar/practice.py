import json

data = {}
data['UTKinect'] = {
        'UserCount' : 10,
        'SpanDivide' : 10,
        'HipCenter' : 1,
        'Spine' : 2,
        'ShoulderCenter' : 3,
        'Head' : 4,
        'ShoulderLeft' : 5,
        'ElbowLeft' : 6,
        'WristLeft' : 7,
        'HandLeft' : 8,
        'ShoulderRight' : 9,
        'ElbowRight' : 10,
        'WristRight' : 11,
        'HandRight' : 12,
        'HipLeft' : 13,
        'KneeLeft' : 14,
        'AnkleLeft' : 15,
        'FootLeft' : 16,
        'HipRight' : 17,
        'KneeRight' : 18,
        'AnkleRight' : 19,
        'FootRight' : 20,
        'Folder' : 'UTKinect',
    }
data['UPCV'] = {
        'UserCount' : 15,
        'SpanDivide' : 5,
        'Head' : 1,
        'ShoulderCenter' : 2,
        'ShoulderLeft' : 3,
        'ShoulderRight' : 4,
        'ElbowLeft' : 5,
        'ElbowRight' : 6,
        'WristLeft' : 7,
        'WristRight' : 8,
        'HandLeft' : 9,
        'HandRight' : 10,
        'Spine' : 11,
        'HipCenter' : 12,
        'HipLeft' : 13,
        'HipRight' : 14,
        'KneeLeft' : 15,
        'KneeRight' : 16,
        'AnkleLeft' : 17,
        'AnkleRight' : 18,
        'FootLeft' : 19,
        'FootRight' : 20,
        'Folder' : 'UPCV',
    }
data['general'] = {
        'TotalJoints' : 20,
        'CoordinatesCount' : 3,
        'xCord' : 0,
        'yCord' : 1,
        'zCord' : 2,
        'MinBin' : 20,
        'DatasetFolder' : 'DataSet',
        'TrainingSetFolder' : 'TrainingSet',
        'TestSetFolder' : 'TestSet',
        'TrainingFileNamePrefix' : 'User_Information_',
        'LookAhead' : 3
    }


with open('constants.json', 'w') as outfile:
    json.dump(data, outfile)