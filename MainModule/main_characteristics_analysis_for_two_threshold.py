import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeTwoVariableInterestingnessSearchSpace import VisualizeTwoVariableInterestingnessSearchSpace
from SubModules.AgreementValueWithAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithAreaConstraintGeneratorForTwoThresholds

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'population_density_on_land_2010'
variable2_name = 'household_density_on_land_2010'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100


# Agreement Generation Inputs
steps = 100
hotspot_area_restriction = 0.3

# Create thresholds min and gradient
max_variable2 = max(variable2_df['values'])
min_variable2= min(variable2_df['values'])
variable_cutpoint_variable2= (max_variable2 - min_variable2)/steps

max_variable1 = max(variable1_df['values'])
min_variable1 =  min(variable1_df['values'])
variable_cutpoint_variable1 = (max_variable1 - min_variable1)/steps

# Visualization Inputs
X_label = 'Population Density (t)'
Y_label = 'Household Density(t\')'
Z_Label = '$I_{(Population\ Density, t),(Household\ Density, t\'))}$'

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
threshold1_values, threshold2_values, agreements = AgreementValueWithAreaConstraintGeneratorForTwoThresholds(min_variable1,
                                                     variable_cutpoint_variable1, min_variable2,variable_cutpoint_variable2,
                                                     variable1_value_matrix,variable2_value_matrix,grid_row_size,
                                                     grid_column_size, grid, total_area, steps,
                                                     hotspot_area_restriction)


# Visualize the agreement search space
VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values, threshold2_values, agreements, X_label, Y_label, Z_Label)

