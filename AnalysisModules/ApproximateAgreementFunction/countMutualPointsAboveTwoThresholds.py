def countMutualPointsAboveTwoThresholds(variable1_value_matrix, threshold1, variable2_value_matrix, threshold2):
    count = 0
    for i in range(len(variable1_value_matrix)):
        for j in range(len(variable1_value_matrix[0])):
            if variable1_value_matrix[i][j]>= threshold1 and variable2_value_matrix[i][j]>= threshold2:
                count += 1

    return count