from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def AgreementValueWithAreaConstraintGeneratorForTwoThresholds(threshold1, threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid, total_observation_area_size, hotspot_area_restriction):
    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Total_hotspot_area = 0
    for polygon in hotspots1:
        area = PolygonArea(polygon)
        Total_hotspot_area += area

    area_coverage = Total_hotspot_area/total_observation_area_size

    if area_coverage <= hotspot_area_restriction:
        hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
        Total_hotspot2_area = 0
        for polygon in hotspots2:
            area = PolygonArea(polygon)
            Total_hotspot2_area += area

        area_coverage2 = Total_hotspot2_area / total_observation_area_size

        if area_coverage2 <= hotspot_area_restriction:
            agreement = Agreement(hotspots1, hotspots2)


    return agreement