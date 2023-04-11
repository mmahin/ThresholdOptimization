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
from SubModules.SearchThresholds.FindAlphaThreshold import FindAlphaThreshold
from SubModules.SearchThresholds.FindBetaThreshold import FindBetaThreshold
from SubModules.SearchThresholds.FindCloseThreshold import FindTargetThreshold
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

alpha = 0.50
beta = 0.03
variable1_values_sorted = np.sort(pd.unique(variable1_df['values']))
variable2_values_sorted = np.sort(pd.unique(variable2_df['values']))

null_indices = np.isnan(variable1_values_sorted)
variable1_values_sorted = variable1_values_sorted[~null_indices]
null_indices = np.isnan(variable2_values_sorted)
variable2_values_sorted = variable2_values_sorted[~null_indices]

variable1_low_threshold_index, a1 = FindAlphaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable1_high_threshold_index, a2 = FindBetaThreshold(variable1_values_sorted,variable1_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)
variable2_low_threshold_index, a3 = FindAlphaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,alpha,0.01)
variable2_high_threshold_index, a4 = FindBetaThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,beta,0.01)

print(variable1_low_threshold_index, a1 , variable1_high_threshold_index, a2, variable2_low_threshold_index, a3 , variable2_high_threshold_index, a4 )
target_threshold1_cutpoint = int((variable1_high_threshold_index- variable1_low_threshold_index)/50)

threshold1_set = []
threshold1_area_coverage = []
threshold2_set = []
threshold2_area_coverage = []
Variable1_hotspots = []
agreements = []
expected = []
count = variable1_low_threshold_index
while count < variable1_high_threshold_index:
    t = variable1_values_sorted[count]
    hotspots = hotspotOfCellsUsingBFS(t, grid_row_size, grid_column_size, variable1_value_matrix, grid)
    Variable1_hotspots.append(hotspots)
    Total_hotspot_area = 0
    for polygon in hotspots:
        area = PolygonArea(polygon)
        Total_hotspot_area += area
    area_coverage = Total_hotspot_area / total_area
    threshold1_area_coverage.append(round(area_coverage,2))
    threshold1_set.append(t)
    count += target_threshold1_cutpoint

for count in range(len(threshold1_area_coverage)):
    found = -1
    for i in range(len(threshold2_area_coverage)):
        if abs(threshold1_area_coverage[count]-threshold2_area_coverage[i]) <= 0.005:
            found = i
            threshold2 = threshold2_set[i]
            c = threshold1_area_coverage[i]
            break

    if found == -1:
        t,c = FindTargetThreshold(variable2_values_sorted,variable2_value_matrix, grid_row_size,grid_column_size,grid, total_area,threshold1_area_coverage[count],0.05)
        threshold2= variable2_values_sorted[t]
    print(round(threshold1_set[count],2),round(threshold1_area_coverage[count],2),round(threshold2,2),round(c,2))
    if abs(threshold1_area_coverage[count]-c)<0.05:

        hotspots = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)

        agreement = Agreement(Variable1_hotspots[count], hotspots)
        agreements.append(agreement)
        expected.append(threshold1_area_coverage[count] * c)
        threshold2_set.append(threshold2)
        threshold2_area_coverage.append(round(c,2))

print("Thresholds 1",threshold1_set)
print("Thresholds 2",threshold2_set)
print("Area Coverage 1",threshold1_area_coverage)
print("Area Coverage 2",threshold2_area_coverage)
print("Agreements:", agreements,len(agreements))
print("Expected:", expected,len(expected))
print("Sum Agreements:", sum(agreements))
print("Sum Expected:",sum(expected))
print("AUC:",sum(agreements)/len(agreements))
from scipy.stats import chisquare
chi2, p = chisquare(agreements, expected)
print(chi2, p)
chi2, p = chisquare(expected, agreements)
print(chi2, p)

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