
def Agreement(countMutualPointsAboveThreshold1Threshold2, countAboveThreshold1,count_above_threshold2):

    union = countAboveThreshold1 + count_above_threshold2 - countMutualPointsAboveThreshold1Threshold2
    if union <= 0:
        return 0

    agreement = countMutualPointsAboveThreshold1Threshold2/union

    return agreement