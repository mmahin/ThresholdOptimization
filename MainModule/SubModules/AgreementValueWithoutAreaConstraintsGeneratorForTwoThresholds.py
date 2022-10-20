from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(min_threshold1, cutpoint_threshold1, min_threshold2,
                                                              cutpoint_threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid, steps):
    agreements = []
    threshold1_values = []


    threshold1 = min_threshold1
    for i in range(0,steps):
        threshold2 = min_threshold2
        threshold2_values = []
        agreements_temp = []

        hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

        for j in range(0,steps):

            hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
            agreement = Agreement(hotspots1, hotspots2)
            agreements_temp.append(agreement)
            threshold2_values.append(threshold2)
            threshold2 += cutpoint_threshold2
        agreements.append(agreements_temp)

        threshold1_values.append(threshold1)
        threshold1 += cutpoint_threshold1

    return threshold1_values, threshold2_values, agreements