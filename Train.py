import Constants
import CalculateAnkleDistance
import CalculateAngle
import math
import statistics as stat
import numpy as np
import TopNPairIndex
from scipy.signal import find_peaks

def smooth(iterable, size):
    i = 0
    moving_average = []
    while (i< len(iterable) - (size+1)):
        current = iterable[i: i+size]
        window_average = sum(current) / size
        moving_average.append(window_average)
        i = i+1
    return moving_average

def Train(userCount):
    maxFrame = 0
    for id in range (0,userCount+1):
        userName = str(id+1)
        FileLocation = Constants.Constants.DataSetFolder+"UPCV\\action_"
        fileID = open(FileLocation+str((id*2)+1)+'.txt','r')
        frameCount = float(fileID.readline().rstrip())
        data = np.zeros(Constants.Constants.TotalJoints, Constants.Constants.Coordinates , frameCount)

        for i in range(0,frameCount+1):
            arr = fileID.readline().rstrip()
            x = [float(x) for x in arr.split()]
            for j in range(0,Constants.Constants.TotalJoints+1):
                data[j, 0, i] = x[3*j - 2, 1]
                data[j, 1, i] = x[3*j - 1, 1]
                data[j, 2, i] = x[3*j , 1]
        ankleDistance = CalculateAnkleDistance.CalculateAnkleDistance(data)
        span = math.floor(len(ankleDistance)/Constants.Constants.SpanDivide)
        smoothAnkleDistance = smooth(ankleDistance,span)
        [_,locs] =  find_peaks(smoothAnkleDistance,,np.mean(smoothAnkleDistance),5)
        start = locs[1,1]
        if(len(locs)<3):
            fin = len(smoothAnkleDistance)
        else:
            fin = locs[3,1]
        angleArray = CalculateAngle.CalculateAngle(data[:,:,start:fin])
        sz = np.shape(angleArray)
        maxFrame = max(maxFrame,sz[0][0])
        #storeData implementation
        fileID.close()

    topNIndex = TopNPairIndex.TopNPairIndex()
    length = len(topNIndex)

    fileID = open(Constants.Constants.TrainingSetFolder+'metadata.txt','w')
    fileID.write('{userCount}\n{maxFrame}\n')
    for i in range(0,len+1):
        fileID.write('{topNIndex[i]}')
    fileID.close()
    


        


            