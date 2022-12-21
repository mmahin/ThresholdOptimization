from GradientSearch.AgrrementCalculatorWithoutAreaConstraintGeneratorForTwoGievnThresholds import AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds
def calculateGradient(threshold1, threshold1_step_size, min_threshold1, max_threshold1, threshold2, threshold2_step_size,
                      min_threshold2, max_threshold2, learning_rate, variable1_value_matrix, variable2_value_matrix,
                      grid_row_size, grid_column_size, grid):
    # First derivative of threshold 1
    current_agreement = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(threshold1, threshold2, variable1_value_matrix,
                                                              variable2_value_matrix, grid_row_size, grid_column_size,
                                                              grid)
    gradients = [
        [threshold1_step_size, 0 ],
        [-1* threshold1_step_size, 0],
        [0, threshold2_step_size],
        [0, -1*threshold2_step_size],
        [threshold1_step_size, threshold2_step_size],
        [threshold1_step_size, -1*threshold2_step_size],
        [-1*threshold1_step_size, threshold2_step_size],
        [-1*threshold1_step_size, -1*threshold2_step_size]
    ]
    # Find the eight direction points
    direction1 = [threshold1 + gradients[0][0], threshold2 + gradients[0][1]]
    direction2 = [threshold1 + gradients[1][0], threshold2 + gradients[1][1]]
    direction3 = [threshold1 + gradients[2][0], threshold2 + gradients[2][1]]
    direction4 = [threshold1 + gradients[3][0], threshold2 + gradients[3][1]]
    direction5 = [threshold1 + gradients[4][0], threshold2 + gradients[4][1]]
    direction6 = [threshold1 + gradients[5][0], threshold2 + gradients[5][1]]
    direction7 = [threshold1 + gradients[6][0], threshold2 + gradients[6][1]]
    direction8 = [threshold1 + gradients[7][0], threshold2 + gradients[7][1]]

    agreement = [0] * 8
    # Find if given directions are valid and their agreements
    if direction1[0] >= min_threshold1 and direction1[0] <= max_threshold1 and direction1[1] >= min_threshold2 and direction1[1] <= max_threshold2:
        agreement[0] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction1[0], direction1[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[0] = 0

    if direction2[0] >= min_threshold1 and direction2[0] <= max_threshold1 and direction2[1] >= min_threshold2 and direction2[1] <= max_threshold2:
        agreement[1] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction2[0], direction2[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[1] = 0

    if direction3[0] >= min_threshold1 and direction3[0] <= max_threshold1 and direction3[1] >= min_threshold2 and direction3[1] <= max_threshold2:
        agreement[2] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction3[0], direction3[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[2] = 0

    if direction4[0] >= min_threshold1 and direction4[0] <= max_threshold1 and direction4[1] >= min_threshold2 and direction4[1] <= max_threshold2:
        agreement[3] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction4[0], direction4[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[3] = 0

    if direction5[0] >= min_threshold1 and direction5[0] <= max_threshold1 and direction5[1] >= min_threshold2 and \
            direction5[1] <= max_threshold2:
        agreement[4] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction5[0], direction5[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[4] = 0

    if direction6[0] >= min_threshold1 and direction6[0] <= max_threshold1 and direction6[1] >= min_threshold2 and \
            direction6[1] <= max_threshold2:
        agreement[5] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction6[0], direction6[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[5] = 0

    if direction7[0] >= min_threshold1 and direction7[0] <= max_threshold1 and direction7[1] >= min_threshold2 and \
            direction7[1] <= max_threshold2:
        agreement[6] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction7[0], direction7[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[6] = 0

    if direction8[0] >= min_threshold1 and direction8[0] <= max_threshold1 and direction8[1] >= min_threshold2 and \
            direction8[1] <= max_threshold2:
        agreement[7] = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(direction8[0], direction8[1],
                                                                                  variable1_value_matrix,
                                                                                  variable2_value_matrix, grid_row_size,
                                                                                  grid_column_size,
                                                                                  grid)
    else:
        agreement[7] = 0



    agreement_change_list = [agreement[0] - current_agreement ,agreement[1] - current_agreement ,agreement[2] - current_agreement ,
                             agreement[3]- current_agreement ,agreement[4] - current_agreement ,agreement[5] - current_agreement ,
                             agreement[6]- current_agreement ,agreement[7]- current_agreement ]

    maximum_agreement = max(agreement_change_list)
    if maximum_agreement > 0:
        maximum_agreement_index = agreement_change_list.index(maximum_agreement)
        return threshold1 + (learning_rate * gradients[maximum_agreement_index][0]), \
               threshold2 + (learning_rate * gradients[maximum_agreement_index][1]), agreement[maximum_agreement_index]
    else:
        return threshold1, threshold2, current_agreement
