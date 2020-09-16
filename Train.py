import Constants
import CalculateAnkleDistance
import CalculateAngle
import math
import statistics as stat
import numpy as np
import TopNPairIndex
import scipy.signal as ss
from findpeaks import findpeaks

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

def Train(userCount):
    maxFrame = 0
    for id in range (userCount):
        locs = []
        userName = str(id+1)
        
        FileLocation = Constants.Constants.DatasetFolder+"UPCV\\action_"
        fileID = open(FileLocation+str((id*2)+1)+'.txt','r')
        frameCount = int(fileID.readline().rstrip())
        data = np.zeros((Constants.Constants.TotalJoints, Constants.Constants.Coordinates , frameCount))

        for i in range(frameCount):
            arr = fileID.readline().rstrip()
            x = [float(x) for x in arr.split()]
            for j in range(Constants.Constants.TotalJoints):
                data[j][0][i] = x[3*j - 2]
                data[j][1][i] = x[3*j - 1]
                data[j][2][i] = x[3*j]
        ankleDistance = CalculateAnkleDistance.CalculateAnkleDistance(data)
        span = math.floor(len(ankleDistance)/Constants.Constants.SpanDivide)
        smoothAnkleDistance = smooth(ankleDistance,span)
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
        angleArray = CalculateAngle.CalculateAngle(data[:,:,start:fin])
        sz = np.shape(angleArray)
        maxFrame = max(maxFrame,sz[0])
        #storeData implementation
        fileID.close()

    topNIndex = TopNPairIndex.TopNPairIndex()
    length = len(topNIndex)

    fileID = open(Constants.Constants.TrainingSetFolder+'metadata.txt','w')
    fileID.write(str(userCount)+"\n"+str(maxFrame)+"\n")
    for i in range(length):
        fileID.write(str(int(topNIndex[i]))+' ')
    fileID.close()
    


        


            