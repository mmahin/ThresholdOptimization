from GradientSearch.GradientCalculation import calculateGradient
def gradientAscentForNpoints(threshold1_set, threshold1_step_size,
                    min_threshold1, max_threshold1, threshold2_set, threshold2_step_size,
                      min_threshold2, max_threshold2,  learning_rate,
                             variable1_value_matrix, variable2_value_matrix, grid_row_size, grid_column_size,
                                                              grid, maximum_iteration):
    # initialize lists to save maximas
    maxima_threshold1_list = []
    maxima_threshold2_list = []
    maxima_agreement_list = []
    # for each point
    for count in range(len(threshold1_set)):
        # set starting points
        threshold1 = threshold1_set[count]
        threshold2 = threshold2_set[count]
        # Iterate till maximum iterations or points get stuck
        for iteration in range(maximum_iteration):

                threshold1_updated, threshold2_updated, agreement = calculateGradient(threshold1, threshold1_step_size,
                    min_threshold1, max_threshold1, threshold2, threshold2_step_size,
                      min_threshold2, max_threshold2, learning_rate, variable1_value_matrix, variable2_value_matrix,
                      grid_row_size, grid_column_size, grid)
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