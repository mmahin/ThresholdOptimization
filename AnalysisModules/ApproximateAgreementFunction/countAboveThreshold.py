def countAboveThreshold(variable_value_matrix, threshold):
    count = 0
    for row in variable_value_matrix:
        for value in row:
            if value >= threshold:
                count += 1

    return count