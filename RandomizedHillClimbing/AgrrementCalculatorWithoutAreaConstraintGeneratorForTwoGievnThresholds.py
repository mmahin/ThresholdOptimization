from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement


def AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(threshold1, threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid):
    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

    hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)

    agreement = Agreement(hotspots1, hotspots2)


    return agreement