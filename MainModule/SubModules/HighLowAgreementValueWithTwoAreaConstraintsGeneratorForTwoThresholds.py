from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from ColdspotsUsingBFS import coldspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from AgreementFunction.PolygonAreaCalculation import HotspotAreaInverse
def HighLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_threshold1, cutpoint_threshold1, min_threshold2,
                                                              cutpoint_threshold2, variable1_value_matrix,
                                                              variable2_value_matrix,grid_row_size, grid_column_size,
                                                              grid, total_observation_area_size, steps, hotspot_area_restriction1,hotspot_area_restriction2):
    agreements = []
    threshold1_values = []
    start = 0
    threshold1 = min_threshold1
    initial_coverage = []
    for i in range(0,steps):
        threshold2 = min_threshold2
        agreements_temp = []
        threshold2_values = []


        hotspots = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
        Total_hotspot1_area = 0
        #HotspotAreaInverse(hotspots)
        for polygon in hotspots:
            area = PolygonArea(polygon)
            Total_hotspot1_area += area


        area_coverage1 = Total_hotspot1_area/total_observation_area_size

        if area_coverage1 <= hotspot_area_restriction1 and area_coverage1 >= hotspot_area_restriction2:

            for j in range(0,steps):

                coldspot = coldspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
                if start == 0:
                    initial_coverage.append(HotspotAreaInverse(coldspot))
                Total_hotspot2_area = initial_coverage[j]
                '''
                for polygon in coldspot:
                    area = PolygonArea(polygon)
                    Total_hotspot2_area += area
                '''
                area_coverage2 = (Total_hotspot2_area / total_observation_area_size)#-0.7027330820465472
                #print("(",i,j,"):",area_coverage1,area_coverage2)
                #print("(",i,j,"):",area_coverage1, area_coverage2)
                if area_coverage2 <= hotspot_area_restriction1 and area_coverage2 >= hotspot_area_restriction2:
                    agreement = Agreement(hotspots, coldspot)
                    agreements_temp.append(agreement)
                    threshold2_values.append(threshold2)
                else:
                    agreements_temp.append(-0.01)
                    threshold2_values.append(threshold2)
                threshold2 += cutpoint_threshold2
            start = 1
        else:
            for k in range(0, steps):
                agreements_temp.append(-0.01)
                threshold2_values.append(threshold2)
                threshold2 += cutpoint_threshold2

        agreements.append(agreements_temp)
        threshold1_values.append(threshold1)

        threshold1 += cutpoint_threshold1

    return threshold1_values, threshold2_values, agreements