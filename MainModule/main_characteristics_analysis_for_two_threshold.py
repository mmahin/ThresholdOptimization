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

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'bachelor_degree_density_2014_2018'
variable2_name = 'medianHouseHoldIncome'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# Agreement Generation Inputs
steps = 100
hotspot_area_restriction1 = 0.5
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
X_label = 'Bachelor Degree Rate (t)'
Y_label = 'Median Income (t\')'
Z_Label = '$I_{(Bachelor\ Degree\ Rate , t),(Median\ Income, t\'))}$'

Output_path = '/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdBachlorIncome.txt'
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
#variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex(grid_matrix, variable1_df, variable2_df,grid_row_size ,grid_column_size)
# Find  valid thresholds and agreement values
threshold1_values, threshold2_values, agreements = AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, total_area, steps,
                                                     hotspot_area_restriction1, hotspot_area_restriction2)

with open(Output_path, 'w') as f:
    for agreement in agreements:
        f.write(f"{agreement}\n")

# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values, threshold2_values, agreements, X_label, Y_label, Z_Label)


