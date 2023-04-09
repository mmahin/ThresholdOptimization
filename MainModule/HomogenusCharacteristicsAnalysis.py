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
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'
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

alpha = 50
beta = 3

variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]


low_index = 0
high_index = len(variable1_values_sorted) - 1
output_index = 0
output_area_coverage = 0
best_diff = 1
best_index = 0
best_area_coverage = 0
#mid_index = int((low_index+high_index)/2)
area_coverage = 1
while low_index < high_index:
    mid_index = int((low_index + high_index) / 2)
    t_m = variable1_values_sorted[mid_index]
    hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Total_hotspot_area = 0
    for polygon in hotspots:
        area = PolygonArea(polygon)
        Total_hotspot_area += area
    area_coverage = Total_hotspot_area / total_area
    output_index = mid_index
    output_area_coverage = area_coverage
    if area_coverage < 0.5:
        diff = 0.5 - area_coverage
        if diff < best_diff :
            best_diff = diff
            best_index = mid_index
            best_area_coverage = area_coverage
    if area_coverage < 0.49:
        high_index = mid_index - 1

    elif area_coverage >= 0.50:
        low_index = mid_index + 1
    else:
        while area_coverage < 0.5 and area_coverage > 0.49 :
            new_mid = mid_index - 1
            t_m = variable1_values_sorted[new_mid]
            hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, variable1_value_matrix, grid)
            Total_hotspot_area = 0
            for polygon in hotspots:
                area = PolygonArea(polygon)
                Total_hotspot_area += area
            area_coverage = Total_hotspot_area / total_area
            if area_coverage < 0.5:
                diff = 0.5 - area_coverage
                if diff < best_diff:
                    best_diff = diff
                    best_index = mid_index
                    best_area_coverage = area_coverage
            if area_coverage <= 0.5:
                mid_index = new_mid
        output_index = mid_index
        output_area_coverage =  area_coverage
        break

print(output_index, output_area_coverage)
print(best_index,best_area_coverage)

low_index = 0
high_index = len(variable1_values_sorted) - 1
output_index2 = 0
output_area_coverage2 = 0
best_diff = 1
best_index = 0
best_area_coverage = 0
#mid_index = int((low_index+high_index)/2)
area_coverage = 1
while low_index < high_index:
    mid_index = int((low_index + high_index) / 2)
    t_m = variable1_values_sorted[mid_index]
    hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Total_hotspot_area = 0
    for polygon in hotspots:
        area = PolygonArea(polygon)
        Total_hotspot_area += area
    area_coverage = Total_hotspot_area / total_area
    output_index2 = mid_index
    output_area_coverage2 = area_coverage
    if area_coverage > 0.04:
        diff = area_coverage - 0.04
        if diff < best_diff :
            best_diff = diff
            best_index = mid_index
            best_area_coverage = area_coverage
    if area_coverage < 0.05:
        high_index = mid_index - 1

    elif area_coverage >= 0.04:
        low_index = mid_index + 1
    else:
        while area_coverage < 0.05 and area_coverage > 0.04:
            new_mid = mid_index - 1
            t_m = variable1_values_sorted[new_mid]
            hotspots = hotspotOfCellsUsingBFS(t_m, grid_row_size, grid_column_size, variable1_value_matrix, grid)
            Total_hotspot_area = 0
            for polygon in hotspots:
                area = PolygonArea(polygon)
                Total_hotspot_area += area
            area_coverage = Total_hotspot_area / total_area
            if area_coverage > 0.04:
                diff = area_coverage - 0.04
                if diff < best_diff:
                    best_diff = diff
                    best_index = mid_index
                    best_area_coverage = area_coverage
            if area_coverage >= 0.04:
                mid_index = new_mid
            print(mid_index, area_coverage)
        output_index2 = mid_index
        output_area_coverage2 = area_coverage

        break
    print(output_index2, output_area_coverage2)
print(output_index2, output_area_coverage2)
print(best_index,best_area_coverage)

target_threshold1_cutpoint = int((output_index2- output_index)/100)

threshold1_set = []
threshold2_set = []

count = output_index
while count < output_index2:
    threshold1_set.append(variable1_values_sorted[count])
    count += target_threshold1_cutpoint
'''
variable1_thresholds = []
variable1_thresholds_area = []
variable2_thresholds = []
variable2_thresholds_area = []
agreements = []
expected = []
for i in range(101):
    if i >= alpha and i<= (100-beta):
        t1 = np.percentile(variable1_df['values'].dropna().astype(float), i)
        variable1_thresholds.append(t1)
        hotspots1 = hotspotOfCellsUsingBFS(t1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

        Total_hotspot_area = 0
        for polygon in hotspots1:
            area1 = PolygonArea(polygon)
            Total_hotspot_area += area1
        area_coverage1 = Total_hotspot_area / total_area
        variable1_thresholds_area.append(area_coverage1)
        t2 = np.percentile(variable2_df['values'].dropna().astype(float), i)
        variable2_thresholds.append(t2)
        hotspots2 = hotspotOfCellsUsingBFS(t2, grid_row_size, grid_column_size, variable2_value_matrix, grid)
        Total_hotspot_area = 0
        for polygon in hotspots2:
            area2 = PolygonArea(polygon)
            Total_hotspot_area += area2
        area_coverage2 = Total_hotspot_area / total_area
        variable2_thresholds_area.append(area_coverage2)
        agreement = Agreement(hotspots1, hotspots2)
        agreements.append(agreement)
        expected.append(area_coverage1*area_coverage2)
        print(t1,area_coverage1,t2,area_coverage2)

print(variable1_thresholds)
print(variable1_thresholds_area)
print(variable2_thresholds)
print(variable2_thresholds_area)
print(agreements)
print(expected)
print(sum(agreements))
print(sum(expected))

from scipy.stats import chisquare
chi2, p = chisquare(agreements, expected)
print(chi2, p)
chi2, p = chisquare(expected, agreements)
print(chi2, p)
#print(len(pd.unique(variable1_df['values'])),len(pd.unique(variable2_df['values'])))
'''