from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.PolygonAreaCalculation import PolygonArea

def FindBetaThreshold(sorted_values,point_wise_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,err):
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
        if area_coverage >= beta:
            diff = area_coverage - beta
            if diff < best_diff:
                best_diff = diff
                best_index = mid_index
                best_area_coverage = area_coverage
        if area_coverage < (beta+err):
            high_index = mid_index - 1

        elif area_coverage > beta:
            low_index = mid_index + 1

        else:
            while area_coverage > beta and area_coverage < (beta+err) :
                new_mid = mid_index + 1
                t_m = sorted_values[new_mid]
                hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, point_wise_value_matrix, grid)
                Total_hotspot_area = 0
                for polygon in hotspots:
                    area = PolygonArea(polygon)
                    Total_hotspot_area += area
                area_coverage = Total_hotspot_area / total_area
                if area_coverage >= beta:
                    diff = area_coverage - beta
                    if diff < best_diff:
                        best_diff = diff
                        best_index = mid_index
                        best_area_coverage = area_coverage
                if area_coverage >= beta:
                    mid_index = new_mid
            output_index = mid_index
            output_area_coverage =  area_coverage
            break

    if abs(output_area_coverage-beta) < abs(best_area_coverage-beta):
        return output_index,output_area_coverage
    else:
        return best_index,best_area_coverage


