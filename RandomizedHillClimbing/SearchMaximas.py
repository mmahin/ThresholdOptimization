import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeTwoVariableInterestingnessSearchSpace import VisualizeTwoVariableInterestingnessSearchSpace
from SubModules.AgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.AssignValuesToGridUsingPointWiseFunctionWithSpatialIndex import AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex
import pandas as pd
import numpy as np

from RandomizedHillClimbing.HillClimbing import hillClimbingForNpoints
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'
X_label = 'Covid-19 Infection Rate\n Thresholds(t)'
Y_label = 'Median Income\n Thresholds(t\')'
Z_Label = 'I({(Covid-19 Infection Rate , t),\n(Median Income, t\'))})'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)


variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]


# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100

maximum_iteration = 2000
# Agreement Generation Inputs
step1 = 100
step2 = 100
target_threshold1 = 4
target_threshold2 = 5
hotspot_area_restriction = 0.5

target_threshold1_cutpoint = int((len(variable1_values_sorted))/target_threshold1)


target_threshold2_cutpoint = int((len(variable2_values_sorted) )/target_threshold2)
threshold1_set = []
threshold2_set = []

point_x = []
point_y = []
values = []

count = 0
while count < len(variable1_values_sorted):
    threshold1_set.append(variable1_values_sorted[count])
    count += target_threshold1_cutpoint

count = 0
while count < len(variable2_values_sorted):
    threshold2_set.append(variable2_values_sorted[count])
    count += target_threshold2_cutpoint

for threshold1 in threshold1_set:
    for threshold2 in threshold2_set:
        point_x.append(threshold1)
        point_y.append(threshold2)
        values.append(0)

print(threshold1_set)
print(threshold2_set)
from PointAndValueVisualizer import PointAndValueVisualizer
PointAndValueVisualizer(point_x,point_y,values,threshold1_set,threshold2_set, X_label,Y_label,Z_Label)

# Create thresholds min and gradient
max_variable2 = max(variable2_df['values'])#60#100000#
min_variable2= min(variable2_df['values'])#15#40000#
threshold2_step_size= (max_variable2 - min_variable2)/step2

max_variable1 = max(variable1_df['values'])#0.45#
min_variable1 =  min(variable1_df['values'])#0.15#
threshold1_step_size = (max_variable1 - min_variable1)/step1

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
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)

maxima_agreement_list, maxima_threshold1_list, maxima_threshold2_list = hillClimbingForNpoints(variable1_values_sorted, variable2_values_sorted, threshold1_set, threshold2_set,
                                                                                            variable1_value_matrix, variable2_value_matrix, grid_row_size, grid_column_size, grid, maximum_iteration)
print(maxima_agreement_list, maxima_threshold1_list, maxima_threshold2_list)
PointAndValueVisualizer(maxima_threshold1_list,maxima_threshold2_list,maxima_agreement_list,threshold1_set,threshold2_set, X_label,Y_label,Z_Label)
import pandas as pd
df = pd.DataFrame()
df['Interestingness'] = maxima_agreement_list
df['Thresholds1'] = maxima_threshold1_list
df['Thresholds2'] = maxima_threshold2_list

df.to_csv("Covid-19_Median_Income_maximas2.csv", index= False)


