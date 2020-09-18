import Constants
import CalculateAnkleDistance
import CalculateAngle
import math
import statistics as stat
import numpy as np
import TopNPairIndex
import scipy.signal as ss
from findpeaks import findpeaks
import StoreData

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
    # print("IN METHOD TRAIN")
    maxFrame = 0
    for id in range (userCount):
        locs = []
        userName = str(id+1)
        
        FileLocation = Constants.Constants.DatasetFolder+"joints_s"
        # print("Opening", FileLocation)
        print(FileLocation+str(id+1).zfill(2)+'_e01.txt')
        fileID = open(FileLocation+str(id+1).zfill(2)+'_e01.txt','r')
        frameCount = int(fileID.readline().rstrip())
        # print("File: ", (id * 2) + 1, " Frame: ", frameCount)
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
        fp = findpeaks(method='peakdetect',lookahead=3)
        peakDict=  fp.fit(smoothAnkleDistance)
        peak_indices = []
        valley_indices = []

        index = 0
        for i in peakDict['df']['peak']:
            if(i == True):
                peak_indices.append(index)
            index += 1

        # index = 0
        # for i in peakDict['df']['valley']:
        #     if(i == True):
        #         valley_indices.append(index)
        #     index += 1
        # if(len(peak_indices)>= 3 ):
        #     locs = peak_indices
        # else:
        #     locs = 

            

        start = peak_indices[0]

        if(len(peak_indices)<3):
            fin = len(smoothAnkleDistance)
        else:
            fin = peak_indices[2]
        angleArray = CalculateAngle.CalculateAngle(data[:,:,start:fin])
        sz = np.shape(angleArray)
        maxFrame = max(maxFrame,sz[0])
        print(sz[0])
        # print("Number of frames", sz[0])
        StoreData.StoreData(id+1,id+1,angleArray)
        fileID.close()

    

    fileID = open(Constants.Constants.TrainingSetFolder+'metadata.txt','w')
    fileID.write(str(userCount)+"\n"+str(maxFrame)+"\n")
    fileID.close()
    
    topNIndex = TopNPairIndex.TopNPairIndex(maxFrame)
    length = len(topNIndex)
    fileID = open(Constants.Constants.TrainingSetFolder+'metadata.txt', 'w')
    fileID.write(str(length)+'\n')
    for i in range(length):
        fileID.write(str(int(topNIndex[i]))+' ')
    fileID.close()
    

# Train(20)
        


            