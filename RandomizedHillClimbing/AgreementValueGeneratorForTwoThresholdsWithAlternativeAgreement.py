from ApproximateAgreementFunction.countAboveThreshold import countAboveThreshold
from ApproximateAgreementFunction.countMutualPointsAboveTwoThresholds import countMutualPointsAboveTwoThresholds
from ApproximateAgreementFunction.agreementFunction import Agreement


def AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement(threshold1,  threshold2, variable1_value_matrix,
                                                              variable2_value_matrix):

    countAboveThreshold1 = countAboveThreshold(variable1_value_matrix, threshold1)
    countAboveThreshold2 = countAboveThreshold(variable2_value_matrix, threshold2)
    countMutualPointsAboveThreshold1Threshold2 = countMutualPointsAboveTwoThresholds(variable1_value_matrix, threshold1, variable2_value_matrix, threshold2)
    agreement = Agreement(countMutualPointsAboveThreshold1Threshold2, countAboveThreshold1,countAboveThreshold2 )

    return agreement