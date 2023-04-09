from RandomizedHillClimbing.AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement import AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement
import numpy as np
def findStep(threshold1, threshold2,variable1_values_sorted, variable2_values_sorted,
                        variable1_value_matrix, variable2_value_matrix, dictAgreement):
    # First derivative of threshold 1
    current_agreement = AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement(threshold1,  threshold2, variable1_value_matrix,
                                                              variable2_value_matrix)

    index1 =  (np.where(variable1_values_sorted == threshold1))[0][0]
    index2 = (np.where(variable2_values_sorted == threshold2))[0][0]
    # Find the eight direction points
    possible_steps = []

    for i in range(-50,51):
        for j in range(-50, 51):
            if i != 0 and j !=0:
                if (index1 + i) >= 0 and (index1 + i) < len(variable1_values_sorted) and\
                    (index2 + j) >= 0 and (index2 + j) < len(variable2_values_sorted):
                    possible_steps.append([variable1_values_sorted[index1 + i], variable2_values_sorted[index2 + j]])
    agreement_update = []
    agreements = []
    for step in possible_steps:
        key = str(step[0])+ str(step[1])
        if key not in dictAgreement.keys():
            dictAgreement[key]= AgreementValueGeneratorForTwoThresholdsWithAlternativeAgreement(step[0], step[1],
                                                                                    variable1_value_matrix,
                                                                                    variable2_value_matrix)
        agreement = dictAgreement[key]
        agreement_update.append((agreement-current_agreement))
        agreements.append(agreement)

    maximum_agreement = max(agreement_update)

    if maximum_agreement >= 0:
        max_index = agreement_update.index(maximum_agreement)
        return possible_steps[max_index][0], possible_steps[max_index][1], agreements[max_index],dictAgreement
    else:
        return threshold1,  threshold2, current_agreement,dictAgreement

