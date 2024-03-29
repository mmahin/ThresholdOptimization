from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def FindTargetThreshold(sorted_values,point_wise_value_matrix, grid_row_size,grid_column_size,grid, total_area,target_coverage,err):
    low_index = 0
    high_index = len(sorted_values) - 1
    output_index = 0
    output_area_coverage = 0
    best_diff = 1
    best_index = 0
    best_area_coverage = 0
    #mid_index = int((low_index+high_index)/2)
    area_coverage = 1
    while low_index < high_index:
        mid_index = int((low_index + high_index) / 2)
        t_m = sorted_values[mid_index]
        hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, point_wise_value_matrix, grid)
        Total_hotspot_area = 0
        for polygon in hotspots:
            area = PolygonArea(polygon)
            Total_hotspot_area += area
        area_coverage = Total_hotspot_area / total_area
        output_index = mid_index
        output_area_coverage = area_coverage
        if area_coverage <= (target_coverage+err) and area_coverage >= (target_coverage-err) :
            diff = abs(target_coverage - area_coverage)
            if diff < best_diff :
                best_diff = diff
                best_index = mid_index
                best_area_coverage = area_coverage
        if area_coverage < (target_coverage-err):
            high_index = mid_index - 1

        elif area_coverage > (target_coverage+err):
            low_index = mid_index + 1
        else:
            if area_coverage < (target_coverage) and area_coverage > (target_coverage - err):
                while area_coverage < target_coverage and area_coverage > (target_coverage-err) :
                    new_mid = mid_index - 1
                    t_m = sorted_values[new_mid]
                    hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, point_wise_value_matrix, grid)
                    Total_hotspot_area = 0
                    for polygon in hotspots:
                        area = PolygonArea(polygon)
                        Total_hotspot_area += area
                    area_coverage = Total_hotspot_area / total_area
                    if area_coverage <= (target_coverage + err) and area_coverage >= (target_coverage - err):
                        diff = abs(target_coverage - area_coverage)
                        if diff < best_diff:
                            best_diff = diff
                            best_index = mid_index
                            best_area_coverage = area_coverage
                    if area_coverage <= target_coverage:
                        mid_index = new_mid
                output_index = mid_index
                output_area_coverage =  area_coverage
                break
            else:
                while area_coverage > target_coverage and area_coverage < (target_coverage+err) :
                    new_mid = mid_index + 1
                    t_m = sorted_values[new_mid]
                    hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, point_wise_value_matrix, grid)
                    Total_hotspot_area = 0
                    for polygon in hotspots:
                        area = PolygonArea(polygon)
                        Total_hotspot_area += area
                    area_coverage = Total_hotspot_area / total_area
                    if area_coverage <= (target_coverage + err) and area_coverage >= (target_coverage - err):
                        diff = abs(target_coverage - area_coverage)
                        if diff < best_diff:
                            best_diff = diff
                            best_index = mid_index
                            best_area_coverage = area_coverage
                    if area_coverage >= target_coverage:
                        mid_index = new_mid
                output_index = mid_index
                output_area_coverage =  area_coverage
                break

    if abs(target_coverage - output_area_coverage) < abs(target_coverage - best_area_coverage):
        return output_index,output_area_coverage
    else:
        return best_index,best_area_coverage