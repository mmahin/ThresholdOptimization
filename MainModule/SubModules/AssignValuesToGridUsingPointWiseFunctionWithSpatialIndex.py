
from shapely.geometry import Point
import geopandas as gpd
def AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex(grid_matrix, variable1_df, variable2_df, grid_row_size, grid_column_size):
    variable1_matrix = [[0 for _ in range(grid_row_size)] for _ in range(grid_column_size)]
    variable2_matrix = [[0 for _ in range(grid_row_size)] for _ in range(grid_column_size)]

    x = []
    y = []
    count = 0
    row_count = 0

    index_dict = {}
    for row in grid_matrix:
        column_count = 0
        for point in row:
            x.append(point.x)
            y.append(point.y)
            index_dict[count] = [row_count,column_count]
            column_count += 1
            count += 1
        row_count += 1

    gdf_nodes = gpd.GeoDataFrame(data={'x': x, 'y': y})

    gdf_nodes.name = 'nodes'
    gdf_nodes['geometry'] = gdf_nodes.apply(lambda row: Point((row['x'], row['y'])), axis=1)
    sindex = gdf_nodes.sindex

    path_shp = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/tl_2016_us_state/tl_2016_us_state.shp"
    my_df_shp = gpd.read_file(path_shp)

    for count in range(len(my_df_shp['geometry'])):
        geometry = my_df_shp['geometry'][count]
        possible_matches_index = list(sindex.intersection(geometry.bounds))
        possible_matches = gdf_nodes.iloc[possible_matches_index]
        precise_matches = possible_matches[possible_matches.intersects(geometry)]
        indexes = precise_matches.index
        for item in indexes:
            matrix_index = index_dict[item]
            variable1_matrix[matrix_index[0]][matrix_index[1]] = variable1_df['values'][count]
            variable2_matrix[matrix_index[0]][matrix_index[1]] = variable2_df['values'][count]


    return variable1_matrix, variable2_matrix
'''
import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# calculate total observation area
polygones = []
for polygon in variable1_df['polygons']:
    polygones.append(polygon)

combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))


# Create the observation grid
bounds = combined_observation_area_polygon.bounds
minx = (bounds['minx']).values
miny = (bounds['miny']).values
maxx = (bounds['maxx']).values
maxy = (bounds['maxy']).values


grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row_size, grid_column_size)

# Assign values to grid points using polygonal function
print(AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex(grid_matrix, variable1_df, variable2_df,grid_row_size ,grid_column_size))
'''