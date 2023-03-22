import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.PolygonIntersectionVisualization import PolygonIntersectionVisualization
from AgreementFunction.agreementFunction import Agreement
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'bachelor_degree_density_2014_2018'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# Agreement Generation Inputs
steps = 100

# Create thresholds min and gradient
'''
max_variable2 = 60#max(variable2_df['values'])
min_variable2= 40#min(variable2_df['values'])
variable_cutpoint_variable2= (max_variable2 - min_variable2)/steps

max_variable1 = 0.45 #max(variable1_df['values'])
min_variable1 = 0.35 #min(variable1_df['values'])
variable_cutpoint_variable1 = (max_variable1 - min_variable1)/steps
'''

# calculate total observation area
polygones = []
for polygon in variable1_df['polygons']:
    polygones.append(polygon)

combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))

total_area = 0
for polygon in combined_observation_area_polygon:
    area = PolygonArea(polygon)
    total_area += area

# Create the observation grid
bounds = combined_observation_area_polygon.bounds
minx = (bounds['minx']).values
miny = (bounds['miny']).values
maxx = (bounds['maxx']).values
maxy = (bounds['maxy']).values


grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row_size, grid_column_size)

# Assign values to grid points using polygonal function
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)

# Find  valid thresholds and agreement values

covid = [0.04, 0.14, 0.25, 0.34, 0.37, 0.43]
bachelor = [1,10,20,27,44,56]

#threshold1 = min_variable1
#threshold2 = min_variable2
for i in range(len(covid)):
    threshold2 = bachelor[i]  # += variable_cutpoint_variable2
    threshold1 = covid[i]  # += variable_cutpoint_variable1

    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Total_hotspot1_area = 0
    for polygon in hotspots1:
        area = PolygonArea(polygon)
        Total_hotspot1_area += area

    hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
    Total_hotspot2_area = 0
    for polygon in hotspots2:
        area = PolygonArea(polygon)
        Total_hotspot2_area += area

    intersection_hotspots = PolygonIntersectionVisualization(hotspots1,hotspots2)
    Total_intersection_area = 0
    for polygon in intersection_hotspots:
        area = PolygonArea(polygon)
        Total_intersection_area += area

    agreement = Agreement(hotspots1, hotspots2)
    print(threshold1, threshold2,agreement)
    print("area covered", round((Total_hotspot1_area/total_area)*100,2), round((Total_hotspot2_area/total_area)*100,2), round((Total_intersection_area/total_area)*100,2))
    HotspotsVisualiztion(hotspots1, combined_observation_area_polygon)
    HotspotsVisualiztion(hotspots2, combined_observation_area_polygon)
    HotspotsVisualiztion(intersection_hotspots, combined_observation_area_polygon)
