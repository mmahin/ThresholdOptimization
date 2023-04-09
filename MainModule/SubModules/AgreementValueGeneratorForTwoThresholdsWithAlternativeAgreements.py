from ApproximateAgreementFunction.countAboveThreshold import countAboveThreshold
from ApproximateAgreementFunction.countMutualPointsAboveTwoThresholds import countMutualPointsAboveTwoThresholds
from ApproximateAgreementFunction.agreementFunction import Agreement


def AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement(min_threshold1, cutpoint_threshold1, min_threshold2,
                                                              cutpoint_threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid, total_observation_area_size, steps, hotspot_area_restriction):
    agreements = []
    threshold1_values = []

    countAboveThreshold2dict = {}
    threshold1 = min_threshold1
    for i in range(0,steps):
        threshold2 = min_threshold2
        threshold2_values = []
        agreements_temp = []
        countAboveThreshold1 = countAboveThreshold(variable1_value_matrix, threshold1)
        for j in range(0,steps):
            if threshold2 not in countAboveThreshold2dict:
                countAboveThreshold2dict[threshold2] = countAboveThreshold(variable2_value_matrix, threshold2)
            count_above_threshold2 = countAboveThreshold2dict[threshold2]
            countMutualPointsAboveThreshold1Threshold2 = countMutualPointsAboveTwoThresholds(variable1_value_matrix, threshold1, variable2_value_matrix, threshold2)
            agreement = Agreement(countMutualPointsAboveThreshold1Threshold2, countAboveThreshold1,count_above_threshold2 )
            agreements_temp.append(agreement)
            threshold2_values.append(threshold2)
            threshold2 += cutpoint_threshold2
        agreements.append(agreements_temp)

        threshold1_values.append(threshold1)
    threshold1 += cutpoint_threshold1

    return threshold1_values, threshold2_values, agreements