from findpeaks import findpeaks

def peakFind(data, genConst):
    fp = findpeaks(method='peakdetect', lookahead = genConst['LookAhead'])
    peakDict = fp.fit(data)
    peakIndices = []
    
    index = 0
    for i in peakDict['df']['peak']:
        if i:
            peakIndices.append(index)
        index += 1

    if len(peakIndices) > 0:
        start = peakIndices[0]
    else:
        start = 0
    if(len(peakIndices) < 3):
        fin = len(data)
    else:
        fin = peakIndices[2]
    return start, fin
    