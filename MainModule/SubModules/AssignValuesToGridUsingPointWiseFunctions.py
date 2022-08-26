from PolygonalFunctionWithR_TreeAndDictionary import  PolygonalValueEstimationUsingR_TreeAndDictionary
def AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict):
    variable1_matrix = []
    variable2_matrix = []

    count = 0
    for row in grid_matrix:
        variable1_row_values = []
        variable2_row_values = []
        for point in row:
            value_variable1 = PolygonalValueEstimationUsingR_TreeAndDictionary(point, variable1_df, StateFIPSDict)
            value_variable2 = PolygonalValueEstimationUsingR_TreeAndDictionary(point, variable2_df, StateFIPSDict)
            variable1_row_values.append(value_variable1)
            variable2_row_values.append(value_variable2)
            count += 1
        variable1_matrix.append(variable1_row_values)
        variable2_matrix.append(variable2_row_values)

    return variable1_matrix, variable2_matrix