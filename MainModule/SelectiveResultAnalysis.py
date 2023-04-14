import geopandas as gpd
import pandas as pd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.PolygonIntersectionVisualization import PolygonIntersectionVisualization
from AgreementFunction.agreementFunction import Agreement
from SubModules.SearchThresholds.FindAlphaThreshold import FindAlphaThreshold
from SubModules.SearchThresholds.FindBetaThreshold import FindBetaThreshold
from SubModules.SearchThresholds.FindCloseThreshold import FindTargetThreshold

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'covid_death_density'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# Agreement Generation Inputs
steps = 100


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
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
# Assign values to grid points using polygonal function
variable1_values = pd.read_csv(variable1_path)
variable2_values =  pd.read_csv(variable2_path)
variable1_value_matrix = []
variable2_value_matrix = []
for i in range(len(variable1_values['List'])):
    strings = ((variable1_values['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    j = 0
    for item in strings:
        values.append(float(item))
        j += 1
    variable1_value_matrix.append(values)

for i in range(len(variable2_values['List'])):
    strings = ((variable2_values['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    j = 0
    for item in strings:
        values.append(float(item))
        j += 1
    variable2_value_matrix.append(values)
# Find  valid thresholds and agreement values
print(variable1_value_matrix)
print(variable2_value_matrix)

threshold1 = 00.18  # += variable_cutpoint_variable2
threshold2 = 0.00185  # += variable_cutpoint_variable1

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
print(threshold1, threshold2,agreement,(Total_hotspot1_area/total_area),(Total_hotspot2_area/total_area), round((Total_hotspot1_area/total_area)*(Total_hotspot2_area/total_area),2))

print("area covered", round((Total_hotspot1_area/total_area)*100,2), round((Total_hotspot2_area/total_area)*100,2),
      round((Total_intersection_area/total_area)*100,2))
