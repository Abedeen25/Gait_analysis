import Constants as C
import math

def TopNPairIndex():
    totalFrame = list()
    totalFrame.append(len(angleArray[0]))
    totalFrame.append(len(angleArray[0]))
    totalFrame = tuple(totalFrame)
    angleCount = list()
    angleCount.append(len(angleArray[0]))
    angleCount.append(len(angleArray[1]))
    angleCount = tuple(angleCount)
    rankArray = zeros(angleCount,2)

    for i in range (0, angleCount):
        histogram = zeros(1, 181)
        for j in range (0, totalFrame):
            angle = (angleArray[j][i] * 180) / math.pi
            angle = round(angle) + 1
            histogram[angle] = histogram[angle] + 1
        count = 0
        for j in range (0, 90):
            if histogram[j] != 0:
                count = count + 1
        rankArray[i][0] = i
        rankArray[i][1] = count

    for i in range (0, angleCount):
        for j in range(0,angleCount-1):
            if rankArray[j][2]<rankArray[j][2]:
                temp = rankArray[j:]
                rankArray[j:] = rankArray[j+1:]
                rankArray[j+1:] = temp

    topNIndex = rankArray[rankArray[:2] > C.MinBin][1]





       

    return topNIndex
