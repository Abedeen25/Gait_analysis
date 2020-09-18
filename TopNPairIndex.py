import LoadData
import Constants
import numpy as np
from operator import itemgetter
import math

def TopNPairIndex(mmaxFrame):
    DEBUG = 1
    topNIndexRet = []
    angleDataArray, userNameArray, userFrameArray, maxFrame, maxJRACount = LoadData.LoadData()
    maxFrame = mmaxFrame
    userCount = len(userNameArray)
    JRACount = maxJRACount
    rankArray = [[0 for x in range(2)] for y in range(JRACount)]
    if DEBUG == 1:
        print("angleDataArray Size: ", len(angleDataArray), len(angleDataArray[0]), len(angleDataArray[0][0]))
        print("userCount", len(userNameArray))
        print("maxFrame", maxFrame)
        print("maxJRACount", maxJRACount)

    for JRA in range(JRACount):
        if DEBUG == 2:
            print("JRA Value: ", JRA)
        JRAArray = []
        histogram = [0 for x in range(181)]
        maxJRAValue = -1
        for user in range(userCount):
            for frame in range(userFrameArray[user]):
                JRAArray.append(angleDataArray[frame][JRA][user])
        if DEBUG == 2:
            print("JRAArray Size: ", len(JRAArray))
        JRACount = len(JRAArray)
        for angleIndex in range(JRACount):
            angle = JRAArray[angleIndex]
            angle = int(round((angle * 180) / math.pi))
            maxJRAValue = max(angle, maxJRAValue)
            histogram[angle] += 1
        if DEBUG == 2:
            print("MaxJRAValue: ", maxJRAValue)
        binCount = 0
        for histogramIndex in range(maxJRAValue + 1):
            if histogram[histogramIndex] != 0:
                binCount += 1
        if DEBUG == 2:
            print("binCount:", binCount)
        rankArray[JRA][0] = JRA
        rankArray[JRA][1] = binCount

    rankArray = sorted(rankArray, key = itemgetter(1), reverse = True)
    if DEBUG == 3:
        print(rankArray)

    for rank in rankArray:
        if rank[1] > Constants.Constants.MinBin:
            topNIndexRet.append(rank[0])
    
    if DEBUG == 3:
        print(TopNPairIndex)

    return topNIndexRet

# print(TopNPairIndex.TopNPairIndex())
            