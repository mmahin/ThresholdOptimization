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
from GradientSearch.GradientAscent import gradientAscentForNpoints
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'
X_label = 'Covid-19 Infection Rate (t)'
Y_label = 'Median Income(t\')'
Z_Label = '$I_{(Covid-19\ Infection\ Rate , t),(Median\ Income, t\'))}$'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100

learning_rate = .1
maximum_iteration = 2000
# Agreement Generation Inputs
step1 = 100
step2 = 100
target_threshold1 = 10
target_threshold2 = 20
hotspot_area_restriction = 0.5

target_threshold1_start = 0.21
target_threshold1_end = 0.45
target_threshold1_cutpoint = (target_threshold1_end - target_threshold1_start )/target_threshold1

target_threshold2_start = 40000
target_threshold2_end = 90000
target_threshold2_cutpoint = (target_threshold2_end - target_threshold2_start )/target_threshold2
threshold1_set = []
threshold2_set = []

point_x = []
point_y = []
values = []

t1 = target_threshold1_start
while t1 <= target_threshold1_end:

    t2 = target_threshold2_start
    while t2 <= target_threshold2_end :
        threshold1_set.append(t1)
        threshold2_set.append(t2)

        t2 += target_threshold2_cutpoint
        point_x.append(t1)
        point_y.append(t2)
        values.append(0)
    t1 += target_threshold1_cutpoint
from PointAndValueVisualizer import PointAndValueVisualizer
PointAndValueVisualizer(point_x,point_y,values, X_label,Y_label,Z_Label)

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

maxima_agreement_list, maxima_threshold1_list, maxima_threshold2_list = gradientAscentForNpoints(threshold1_set, threshold1_step_size, target_threshold1_start, target_threshold1_end,
                                                                                                 threshold2_set,  threshold2_step_size, target_threshold2_start, target_threshold2_end, learning_rate,
                             variable1_value_matrix, variable2_value_matrix, grid_row_size, grid_column_size,
                                                              grid, maximum_iteration)
print(maxima_agreement_list, maxima_threshold1_list, maxima_threshold2_list)

import pandas as pd
df = pd.Dataframe()
df['Interestingness'] = maxima_agreement_list
df['Thresholds1'] = maxima_threshold1_list
df['Thresholds2'] = maxima_threshold2_list

df.to_csv("Covid-19_Median_Income_maximas.csv", index= False)
PointAndValueVisualizer(maxima_threshold1_list,maxima_threshold2_list,maxima_agreement_list, X_label,Y_label,Z_Label)

