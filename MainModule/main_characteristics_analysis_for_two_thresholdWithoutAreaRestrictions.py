import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctionWithSpatialIndex import AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex
from SubModules.VisualizeTwoVariableInterestingnessSearchSpaceWithoutRestrictions import VisualizeTwoVariableInterestingnessSearchSpaceWithoutRestriction
from SubModules.AgreementValueWithoutAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 200
grid_column_size = 200


# Agreement Generation Inputs
steps = 200

# Create thresholds min and gradient
max_variable2 = max(variable2_df['values'])
min_variable2= min(variable2_df['values'])
variable_cutpoint_variable2= (max_variable2 - min_variable2)/steps

max_variable1 = max(variable1_df['values'])
min_variable1 =  min(variable1_df['values'])
variable_cutpoint_variable1 = (max_variable1 - min_variable1)/steps
print(max_variable2, min_variable2, max_variable1, min_variable1)
# Visualization Inputs
X_label = 'Covid-19 Infection Rate (t)'
Y_label = 'Median Income(t\')'
Z_Label = '$I_{(Covid-19\ Infection\ Rate , t),(Median\ Income, t\'))}$'

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
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex(grid_matrix, variable1_df, variable2_df,grid_row_size ,grid_column_size)

# Find  valid thresholds and agreement values
threshold1_values, threshold2_values, agreements = AgreementValueWithoutAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, steps)


# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpaceWithoutRestriction(min_variable1,max_variable1, min_variable2, max_variable2, steps, agreements, X_label, Y_label, Z_Label)

