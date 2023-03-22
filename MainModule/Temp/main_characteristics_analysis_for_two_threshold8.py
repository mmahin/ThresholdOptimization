import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeTwoVariableInterestingnessSearchSpace import VisualizeTwoVariableInterestingnessSearchSpace
from SubModules.AgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.HighLowAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import HighLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.LowHighAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import LowHighAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.LowLowAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import LowLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.AssignValuesToGridUsingPointWiseFunctionWithSpatialIndex import AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'bachelor_degree_density_2014_2018'
variable2_name = 'povertyRate'


variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# Agreement Generation Inputs
steps = 100
hotspot_area_restriction1 = 0.75
hotspot_area_restriction2 = 0.1
# Create thresholds min and gradient
max_variable2 = max(variable2_df['values'])#60#100000#
min_variable2= min(variable2_df['values'])#15#40000#
variable_cutpoint_variable2= (max_variable2 - min_variable2)/steps

max_variable1 = max(variable1_df['values'])#0.45#
min_variable1 =  min(variable1_df['values'])#0.15#
variable_cutpoint_variable1 = (max_variable1 - min_variable1)/steps
print(max_variable2, min_variable2, max_variable1, min_variable1)
# Visualization Inputs
X_label = 'Bachelor Degree Rate(t)'
Y_label = 'Poverty Rate(t\')'
Z_Label = '$I_{(Bachelor\ Degree\ Rate, t),(Poverty\ Rate, t\'))}$'

Output_path1 = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementNoAreaRestrictedWithTwoThresholdBachelorPoverty0.75to0.1.txt'
Output_path2 = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementTwoAreaRestrictedWithTwoThresholdBachelorPoverty0.75to0.1.txt'
#Output_path3 = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/LowLow/agreementTwoAreaRestrictedWithTwoThresholdLowLowBachelorService.txt'

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
'''
variable2_value_matrix_inverse = variable2_value_matrix
for i in range(grid_row_size):
    for j in range(grid_column_size):
            variable2_value_matrix_inverse[i][j] = 1/(variable2_value_matrix_inverse[i][j]+1)

max_variable2_inverse = 1/(min(variable2_df['values'])+1)
min_variable2_inverse = 1/(max(variable2_df['values'])+1)
variable_cutpoint_variable2_inverse = (max_variable2_inverse - min_variable2_inverse)/steps
'''
#variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex(grid_matrix, variable1_df, variable2_df,grid_row_size ,grid_column_size)
# Find  valid thresholds and agreement values
threshold1_values1, threshold2_values1, agreements1 = AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, total_area, steps,
                                                     hotspot_area_restriction1, hotspot_area_restriction2)

with open(Output_path1, 'w') as f:
    for agreement in agreements1:
        f.write(f"{agreement}\n")
'''
for i in range(len(threshold2_values)):
    threshold2_values[i] = (1/threshold2_values[i])-1
'''

'''
variable1_value_matrix_inverse = variable1_value_matrix
for i in range(grid_row_size):
    for j in range(grid_column_size):
        variable1_value_matrix_inverse[i][j] = 1 / (variable1_value_matrix_inverse[i][j] + 1)


max_variable1_inverse = 1 / (min(variable1_df['values']) + 1)
min_variable1_inverse = 1 / (max(variable1_df['values']) + 1)
variable_cutpoint_variable1_inverse = (max_variable1_inverse - min_variable1_inverse) / steps

hotspot_area_restriction1 = 0.5
hotspot_area_restriction2 = 0.1
threshold1_values2, threshold2_values2, agreements2 = AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, total_area, steps,
                                                     hotspot_area_restriction1, hotspot_area_restriction2)


with open(Output_path2, 'w') as f:
    for agreement in agreements2:
        f.write(f"{agreement}\n")
# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values1, threshold2_values1, agreements1, X_label, Y_label, Z_Label)
# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values2, threshold2_values2, agreements2, X_label, Y_label, Z_Label)

for i in range(len(threshold1_values)):
    threshold1_values[i] = (1/threshold1_values[i])-1
'''

'''
threshold1_values3, threshold2_values3, agreements3 = LowLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, total_area, steps,
                                                     hotspot_area_restriction1, hotspot_area_restriction2)

with open(Output_path3, 'w') as f:
    for agreement in agreements3:
        f.write(f"{agreement}\n")
'''
'''
for i in range(len(threshold2_values)):
    threshold2_values[i] = (1/threshold2_values[i])-1

for i in range(len(threshold1_values)):
    threshold1_values[i] = (1/threshold1_values[i])-1
'''

# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values1, threshold2_values1, agreements1, X_label, Y_label, Z_Label)
# Visualize the agreement search space
#VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values2, threshold2_values2, agreements2, X_label, Y_label, Z_Label)
# Visualize the agreement search space
#VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values3, threshold2_values3, agreements3, X_label, Y_label, Z_Label)
