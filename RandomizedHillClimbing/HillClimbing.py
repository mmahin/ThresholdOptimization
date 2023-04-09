from RandomizedHillClimbing.FindStep import findStep
def hillClimbingForNpoints(variable1_values_sorted, variable2_values_sorted, threshold1_set, threshold2_set,
                        variable1_value_matrix, variable2_value_matrix, grid_row_size, grid_column_size, grid, maximum_iteration):
    # initialize lists to save maximas
    maxima_threshold1_list = []
    maxima_threshold2_list = []
    maxima_agreement_list = []
    dictAgreement = {}
    # for each point
    for threshold1 in threshold1_set:
        for threshold2 in threshold2_set:
            # Iterate till maximum iterations or points get stuck
            for iteration in range(maximum_iteration):

                    threshold1_updated, threshold2_updated, agreement, dictAgreement = findStep(threshold1, threshold2,variable1_values_sorted, variable2_values_sorted,
                        variable1_value_matrix, variable2_value_matrix, dictAgreement)
                    if (iteration == (maximum_iteration -1)) or (threshold1_updated == threshold1 and threshold2_updated == threshold2):
                        maxima_threshold1_list.append(threshold1_updated)
                        maxima_threshold2_list.append(threshold2_updated)
                        maxima_agreement_list.append(agreement)
                        print(agreement, threshold1_updated, threshold2_updated)
                        break
                    else:
                        threshold1 = threshold1_updated
                        threshold2 = threshold2_updated



    return maxima_agreement_list, maxima_threshold1_list, maxima_threshold2_list