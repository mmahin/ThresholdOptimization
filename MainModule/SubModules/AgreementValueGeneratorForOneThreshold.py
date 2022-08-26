from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def AgreementValueGeneratorForOneThreshold(threshold1,  min_threshold2, cutpoint_threshold2, variable1_value_matrix,
                                          variable2_value_matrix,grid_row_size, grid_column_size, grid,  steps):
    agreements = []

    threshold2 = min_threshold2
    threshold2_values = []

    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

    for j in range(0,steps):

        hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
        agreement = Agreement(hotspots1, hotspots2)
        agreements.append(agreement)
        threshold2_values.append(threshold2)
        threshold2 += cutpoint_threshold2

    return threshold2_values, agreements