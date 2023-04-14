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

#Set Inputs
#data access inputs
variable1_name = 'bachelor_degree_density_2014_2018'
variable2_name = 'avg_precipitation_for_county'

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
'''
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

alpha = 0.50
beta = 0.01

variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1,variable1_low_threshold_index)
print(variable1_values_sorted[variable1_high_threshold_index], a2,variable1_high_threshold_index)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3,variable2_low_threshold_index)
print(variable2_values_sorted[variable2_high_threshold_index], a4,variable2_high_threshold_index)

hotspots1 = hotspotOfCellsUsingBFS(16, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(40, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(6, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)


variable1_name = 'avg_temp_for_county'
variable2_name = 'population_density_on_land_2010'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)

target_threshold2_cutpoint = int((variable2_high_threshold_index- variable2_low_threshold_index)/steps)
threshold2_set = []
count = variable2_low_threshold_index
while count < variable2_high_threshold_index:
    t = variable2_values_sorted[count]
    threshold2_set.append(t)
    count += target_threshold2_cutpoint
print(threshold2_set)


variable1_name = 'household_density_on_land_2010'
variable2_name = 'UnempRate2018'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)

hotspots1 = hotspotOfCellsUsingBFS(4.1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(186, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(3, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(8, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
target_threshold1_cutpoint = int((variable1_high_threshold_index- variable1_low_threshold_index)/steps)
threshold1_set = []
count = variable1_low_threshold_index
while count < variable1_high_threshold_index:
    t = variable1_values_sorted[count]
    threshold1_set.append(t)
    count += target_threshold1_cutpoint
print(threshold1_set)


variable1_name = 'PctEmpAgriculture'
variable2_name = 'PctEmpMining'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)



variable1_name = 'PctEmpConstruction'
variable2_name = 'PctEmpManufacturing'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)


variable1_name = 'PctEmpTrade'
variable2_name = 'PctEmpTrans'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)


hotspots1 = hotspotOfCellsUsingBFS(12, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(17, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(5, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(10, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)


variable1_name = 'PctEmpInformation'
variable2_name = 'PctEmpFIRE'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)
hotspots1 = hotspotOfCellsUsingBFS(0, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(3, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(3, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(7, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)


variable1_name = 'PctEmpServices'
variable2_name = 'PctEmpGovt'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)
hotspots1 = hotspotOfCellsUsingBFS(38, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(54, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(4, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(11, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)


variable1_name = 'medianHouseHoldIncome'
variable2_name = 'povertyRate'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]
vals=[]
for item in variable1_values_sorted:
    vals.append(item)
print(vals)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)
hotspots1 = hotspotOfCellsUsingBFS(38, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area/total_area)
hotspots1 = hotspotOfCellsUsingBFS(54, grid_row_size, grid_column_size, variable1_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)

hotspots1 = hotspotOfCellsUsingBFS(12, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
hotspots1 = hotspotOfCellsUsingBFS(31, grid_row_size, grid_column_size, variable2_value_matrix, grid)
Total_hotspot1_area = 0
for polygon in hotspots1:
    area = PolygonArea(polygon)
    Total_hotspot1_area += area

print(Total_hotspot1_area / total_area)
target_threshold1_cutpoint = int((variable1_high_threshold_index- variable1_low_threshold_index)/steps)
threshold1_set = []
count = variable1_low_threshold_index
while count < variable1_high_threshold_index:
    t = variable1_values_sorted[count]
    threshold1_set.append(t)
    count += target_threshold1_cutpoint
print(threshold1_set)
'''

variable1_name = 'covid_cases_density'
variable2_name = 'covid_death_density'
variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"
variable2_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
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

alpha = 0.50
beta = 0.01
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]
print(variable1_values_sorted)
print(variable2_values_sorted)
print(len(variable1_values_sorted),len(variable2_values_sorted))
variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
print(variable1_name)
print(variable1_values_sorted[variable1_low_threshold_index], a1)
print(variable1_values_sorted[variable1_high_threshold_index], a2)
print(variable2_name)
print(variable2_values_sorted[variable2_low_threshold_index], a3)
print(variable2_values_sorted[variable2_high_threshold_index], a4)
target_threshold1_cutpoint = int((variable1_high_threshold_index- variable1_low_threshold_index)/steps)
threshold1_set = []
count = variable1_low_threshold_index
while count < variable1_high_threshold_index:
    t = variable1_values_sorted[count]
    threshold1_set.append(t)
    count += target_threshold1_cutpoint
print(threshold1_set)
target_threshold2_cutpoint = int((variable2_high_threshold_index- variable2_low_threshold_index)/steps)
threshold2_set = []
count = variable2_low_threshold_index
while count < variable2_high_threshold_index:
    t = variable2_values_sorted[count]
    threshold2_set.append(t)
    count += target_threshold2_cutpoint
print(threshold2_set)