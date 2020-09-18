def averageFilter(data, span):
    i = 0
    moving = []
    cummSum = [0]
    for i, x in enumerate(data, 1):
        cummSum.append(cummSum[i - 1] + x)
        if i >= span:
            move = (cummSum[i] - cummSum[i - span]) / span
            moving.append(move)
    return moving