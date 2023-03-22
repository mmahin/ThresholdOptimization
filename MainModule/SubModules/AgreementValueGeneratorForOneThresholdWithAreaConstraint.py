from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def AgreementValueGeneratorForOneThresholdWithAreaConstrint(threshold1,  min_threshold2, cutpoint_threshold2, variable1_value_matrix,
                                          variable2_value_matrix,grid_row_size, grid_column_size, grid,  steps,
                                        hotspot_area_restriction1, hotspot_area_restriction2, total_observation_area_size):
    agreements = []

    threshold2 = min_threshold2
    threshold2_values = []

    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

    for j in range(0,steps):

        hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
        Total_hotspot_area = 0
        for polygon in hotspots2:
            area = PolygonArea(polygon)
            Total_hotspot_area += area

        area_coverage = Total_hotspot_area / total_observation_area_size


        if area_coverage <= hotspot_area_restriction1 and area_coverage >= hotspot_area_restriction2:
            agreement = Agreement(hotspots1, hotspots2)
            agreements.append(agreement)
            threshold2_values.append(threshold2)
        else:
            agreements.append(-0.001)
            threshold2_values.append(threshold2)
        threshold2 += cutpoint_threshold2

    return threshold2_values, agreements