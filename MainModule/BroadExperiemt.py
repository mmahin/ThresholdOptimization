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
import numpy as np
from SubModules.SearchThresholds.FindAlphaThreshold import FindAlphaThreshold
from SubModules.SearchThresholds.FindBetaThreshold import FindBetaThreshold
from SubModules.SearchThresholds.FindCloseThreshold import FindTargetThreshold

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
thresholds_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/VariableThresholds_.5_.01.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'covid_death_density'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

thresholds_df = pd.read_csv(thresholds_path)
variable1_thresholds = thresholds_df['Thresholds'][thresholds_df['Name'] == variable1_name].values[0]
variable2_thresholds = thresholds_df['Thresholds'][thresholds_df['Name'] == variable2_name].values[0]
variable1_thresholds_strings = variable1_thresholds.split(",")
variable2_thresholds_strings = variable2_thresholds.split(",")
threshold1_set = []
threshold2_set = []
for item in variable1_thresholds_strings:
    threshold1_set.append(float(item))

for item in variable2_thresholds_strings:
    threshold2_set.append(float(item))

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


threshold1s = []
threshold2s = []
threshold1_areas = []
threshold2_areas = []
agreements = []
daviations = []
hotspots_threshold2_dict = {}
count = 0
for threshold1 in threshold1_set:
    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Total_hotspot1_area = 0
    for polygon in hotspots1:
        area = PolygonArea(polygon)
        Total_hotspot1_area += area
    for threshold2 in threshold2_set:
        if str(threshold2) not in hotspots_threshold2_dict.keys():
            hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
            Total_hotspot2_area = 0
            for polygon in hotspots2:
                area = PolygonArea(polygon)
                Total_hotspot2_area += area
            hotspots_threshold2_dict[str(threshold2)] = {}
            hotspots_threshold2_dict[str(threshold2)]['H'] = hotspots2
            hotspots_threshold2_dict[str(threshold2)]['A'] = Total_hotspot2_area
        hotspots2 = hotspots_threshold2_dict[str(threshold2)]['H']
        Total_hotspot2_area = hotspots_threshold2_dict[str(threshold2)]['A']
        threshold1_areas.append(Total_hotspot1_area / total_area)
        threshold2_areas.append(Total_hotspot2_area / total_area)
        expected = (Total_hotspot1_area/total_area) * (Total_hotspot2_area / total_area)
        agreement = Agreement(hotspots1, hotspots2)
        threshold1s.append(threshold1)
        threshold2s.append(threshold2)
        agreements.append(agreement)
        daviations.append(agreement-expected)
        print(count,agreement,expected)
        count+=1

max_index = agreements.index(max(agreements))
print("Pattern", variable1_name,variable2_name)
print("Max Threshold1", threshold1s[max_index])
print("Max Threshold2", threshold2s[max_index])
print("Max Agreement", agreements[max_index])
print("Expected Agreement", threshold1_areas[max_index]*threshold2_areas[max_index])

max_deviation_index = daviations.index(max(daviations))
print("Max Deviation Threshold1", threshold1s[max_deviation_index])
print("Max Deviation Threshold2", threshold2s[max_deviation_index])
print("Max Deviation Agreement", agreements[max_deviation_index])
print("Expected Deviation Agreement", threshold1_areas[max_deviation_index]*threshold2_areas[max_deviation_index])

min_deviation_index = daviations.index(min(daviations))
print("Min Deviation Threshold1", threshold1s[min_deviation_index])
print("Min Deviation Threshold2", threshold2s[min_deviation_index])
print("Min Deviation Agreement", agreements[min_deviation_index])
print("Expected Deviation Agreement", threshold1_areas[min_deviation_index]*threshold2_areas[min_deviation_index])

