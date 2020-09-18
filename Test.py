import Constants
import LoadData
import numpy as np
import CalculateAnkleDistance
import CalculateAngle
import DTW
import math
from findpeaks import findpeaks
from matplotlib import pyplot as plt
import findWarpPathLength

def smooth(iterable, size):
    i = 0
    moving_aves = []
    cumsum = [0]
    for i, x in enumerate(iterable, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=size:
            moving_ave = (cumsum[i] - cumsum[i-size])/size
            moving_aves.append(moving_ave)
    return moving_aves

def Test(testfile):
    angleDataArray, userNameArray, userFrameArray,maxFrame,maxAngleCount = LoadData.LoadData()
    userCount = len(userNameArray)

    testFileLocation = Constants.Constants.TestSetFolder+testfile
    fileID = open(testFileLocation,'r')

    testFrameCount = int(fileID.readline().rstrip())
    testData = np.zeros((Constants.Constants.TotalJoints,Constants.Constants.Coordinates,testFrameCount))

    for i in range(testFrameCount):
        arr = fileID.readline().rstrip()
        x = [float(x) for x in arr.split()]
        for j in range(Constants.Constants.TotalJoints):
            testData[j][0][i] = x[3*j - 2]
            testData[j][1][i] = x[3*j - 1]
            testData[j][2][i] = x[3*j]
    fileID.close()

    testAnkleDistance = CalculateAnkleDistance.CalculateAnkleDistance(testData)
    span = math.floor(len(testAnkleDistance)/Constants.Constants.SpanDivide)
    smoothAnkleDistance = smooth(testAnkleDistance,span)
    fp = findpeaks(method='peakdetect',lookahead=5)
    peakDict=  fp.fit(smoothAnkleDistance)
    peak_indices = []
    valley_indices = []

    index = 0
    for i in peakDict['df']['peak']:
        if(i == True):
            peak_indices.append(index)
        index += 1

    index = 0
    for i in peakDict['df']['valley']:
        if(i == True):
            valley_indices.append(index)
        index += 1
    if(len(peak_indices)>= 3 ):
        locs = peak_indices
    elif(len(valley_indices) >= 3):
        locs = valley_indices
    else:
        print('NOT ENOUGH DATA!')

    start = locs[0]
    if(len(locs)<3):
        fin = len(smoothAnkleDistance)
    else:
        fin = locs[2]

    testAngleArray = CalculateAngle.CalculateAngle(testData[:,:,start:fin])

    fileID = open(Constants.Constants.TrainingSetFolder+'metadata.txt','r')
    arr = int(fileID.readline().rstrip())
    arr = int(fileID.readline().rstrip())
    length = int(fileID.readline().rstrip())
    arr = fileID.readline().rstrip()
    fileID.close()

    topNIndex = [int(x) for x in arr.split()]

    testData = []
    # for i in topNIndex:
        #testData.append(testAngleArray[i])
    
    # topNIndex = np.transpose(topNIndex)
    voteCount = [0] * userCount
    storeMismatch = [0] * userCount

    print("DIm1 ", len(angleDataArray), "DIM2 ", len(angleDataArray[0]), "DIM3", len(angleDataArray[0][0]))

    N = len(topNIndex)
    for pairIndex in topNIndex:
        testData = []
        for frame in testAngleArray:
            testData.append(frame[pairIndex])
        mismatchScore = []
        trainData = []
        for user in range(userCount):
            #trainData = angleDataArray[:][pairIndex][user]
            for i in range(maxFrame):
                trainData.append(angleDataArray[i][pairIndex][user])
            #mismatchScore.append(DTW.DTW(trainData, testData))
            storeMismatch[user] += DTW.DTW(trainData, testData)
    minMismatch = min(storeMismatch)
    idx = storeMismatch.index(minMismatch)
    voteCount[idx] += 1
    print(storeMismatch)
    maxVoted = max(voteCount)
    maxVotedUser = []
    for i in range(userCount):
        if maxVoted == voteCount[i]:
            maxVotedUser.append(i)

    print(voteCount)
    return maxVotedUser

"""
    for i in range(length):
        index = int(topNIndex[i])
        angles = testAngleArray[:,index]
        # angles = np.transpose(angles)
        # mismatchScore = np.zeros((1,userCount))
        mismatchScore = []
        for j in range(userCount):
            anglesToBeMatchedWith = angleDataArray[:][index][j]
            print(anglesToBeMatchedWith)
            # anglesToBeMatchedWith = np.transpose(anglesToBeMatchedWith)
            anglesToBeMatchedWith = anglesToBeMatchedWith[np.min(np.nonzero(anglesToBeMatchedWith)) : np.max(np.nonzero(anglesToBeMatchedWith))]
            # mismatchScore[0][j] = DTW.DTW(angles,anglesToBeMatchedWith)
            mismatchScore.append(DTW.DTW(angles,anglesToBeMatchedWith))
            # mismatchScore.append(dtw(angles,anglesToBeMatchedWith,keep_internals=True))
            # d = dtw(angles, anglesToBeMatchedWith,dist=findWarpPathLength.findWarpPathLength(angles,anglesToBeMatchedWith))
            # print(d)
        
        # plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
        # plt.plot(path[0], path[1], 'w')
        storeMismatch[0] = storeMismatch[0] + mismatchScore[0]
        minMismatch = np.min(mismatchScore)
        minMismatchedUser = np.min(np.nonzero(mismatchScore))
        voteCount[0][minMismatchedUser] = voteCount[0][minMismatchedUser] + 1

    maxVoteCount = max(voteCount)
    maxVotedUser = np.max(np.nonzero(voteCount))

    userID = maxVotedUser[0][0]
    userName = userNameArray[maxVotedUser[0][0]]

    return userID, userName

"""
