import geopandas as gpd
import pandas as pd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
import numpy as np
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeTwoVariableInterestingnessSearchSpace import VisualizeTwoVariableInterestingnessSearchSpace
from SubModules.AgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.HighLowAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import HighLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.LowHighAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import LowHighAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.LowLowAgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import LowLowAgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.AssignValuesToGridUsingPointWiseFunctionWithSpatialIndex import AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from scipy.stats import chi2_contingency
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'bachelor_degree_density_2014_2018'
variable2_name = 'avg_precipitation_for_county'
grid_row_size = 100
grid_column_size = 100

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)


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
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'avg_temp_for_county'
variable2_name = 'population_density_on_land_2010'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'household_density_on_land_2010'
variable2_name = 'UnempRate2018'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'PctEmpAgriculture'
variable2_name = 'PctEmpMining'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'PctEmpConstruction'
variable2_name = 'PctEmpManufacturing'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'PctEmpTrade'
variable2_name = 'PctEmpTrans'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'PctEmpInformation'
variable2_name = 'PctEmpFIRE'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'PctEmpServices'
variable2_name = 'PctEmpGovt'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'medianHouseHoldIncome'
variable2_name = 'povertyRate'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")

# Assign values to grid points using polygonal function
variable1_name = 'covid_cases_density'
variable2_name = 'covid_death_density'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)
Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable1_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable1_value_matrix:
        f.write(f"\"{item}\"\n")

Output_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/"+variable2_name+".csv"

with open(Output_path, 'w') as f:
    f.write(f"List\n")
    for item in variable2_value_matrix:
        f.write(f"\"{item}\"\n")