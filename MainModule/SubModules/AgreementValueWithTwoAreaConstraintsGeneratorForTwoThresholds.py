from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_threshold1, cutpoint_threshold1, min_threshold2,
                                                              cutpoint_threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid, total_observation_area_size, steps, hotspot_area_restriction):
    agreements = []
    threshold1_values = []


    threshold1 = min_threshold1
    for i in range(0,steps):
        threshold2 = min_threshold2
        threshold2_values = []
        agreements_temp = []

        hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
        Total_hotspot1_area = 0
        for polygon in hotspots1:
            area = PolygonArea(polygon)
            Total_hotspot1_area += area

        area_coverage1 = Total_hotspot1_area/total_observation_area_size

        if area_coverage1 <= hotspot_area_restriction:

            for j in range(0,steps):

                hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
                Total_hotspot2_area = 0
                for polygon in hotspots2:
                    area = PolygonArea(polygon)
                    Total_hotspot2_area += area

                area_coverage2 = Total_hotspot2_area / total_observation_area_size

                if area_coverage2 <= hotspot_area_restriction:
                    agreement = Agreement(hotspots1, hotspots2)
                    agreements_temp.append(agreement)
                    threshold2_values.append(threshold2)
                threshold2 += cutpoint_threshold2
            agreements.append(agreements_temp)

            threshold1_values.append(threshold1)
        threshold1 += cutpoint_threshold1

    return threshold1_values, threshold2_values, agreements