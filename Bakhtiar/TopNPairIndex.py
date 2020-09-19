from operator import itemgetter
from math import pi, comb

def topNPairIndex(data, genConst):
    topNIndexRet = []
    pairCount = comb(genConst['TotalJoints'] - 1, 2)
    rankArray = rankArray = [[0 for x in range(2)] for y in range(pairCount)]
    userCount = len(data)
    for pair in range(pairCount):
        pairArray = []
        histogram = [0 for x in range(181)]
        maxPairAngle = -1
        for user in range(1, userCount + 1):
            frameCount = data[str(user)][0]
            frames = data[str(user)][1]
            for frame in range(frameCount):
                pairArray.append(frames[frame][pair])
        pairCount = len(pairArray)
        for pairIndex in range(pairCount):
            pairAngle = int(round((pairArray[pairIndex] * 180) / pi))
            maxPairAngle = max(pairAngle, maxPairAngle)
            histogram[pairAngle] += 1
        binCount = 0
        for histogramIdx in range(maxPairAngle + 1):
            if histogram[histogramIdx] != 0:
                binCount += 1
        rankArray[pair][0] = pair
        rankArray[pair][1] = binCount
    rankArray = sorted(rankArray, key = itemgetter(1), reverse = True)

    for rank in rankArray:
        if rank[1] > genConst['MinBin']:
            topNIndexRet.append(rank[0])
    
    return topNIndexRet

def extractTopNIndex(data, topNPairIndex):
    topNPairFrames = []
    for frame in data:
        topNPairs = []
        for idx in topNPairIndex:
            topNPairs.append(frame[idx])
        topNPairFrames.append(topNPairs)
    return topNPairFrames