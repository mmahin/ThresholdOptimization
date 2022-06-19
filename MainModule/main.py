import pandas as pd
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt
import shapely.wkt
import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from numpy import asarray
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
import math
df = pd.read_csv('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv')
#UnempRate2018
#medianHouseHoldIncome
print(df['bachelor_degree_density_2014_2018'].describe())
print(df['avg_precipitation_for_county'].describe())
print(df['avg_temp_for_county'].describe())
print(df['population_density_on_land_2010'].describe())
print(df['household_density_on_land_2010'].describe())
print(df['UnempRate2018'].describe())
print(df['PctEmpAgriculture'].describe())
print(df['PctEmpMining'].describe())
print(df['PctEmpConstruction'].describe())
print(df['PctEmpManufacturing'].describe())
print(df['PctEmpTrade'].describe())
print(df['PctEmpTrans'].describe())
print(df['PctEmpInformation'].describe())
print(df['PctEmpFIRE'].describe())
print(df['PctEmpServices'].describe())
print(df['PctEmpGovt'].describe())
print(df['medianHouseHoldIncome'].describe())
print(df['povertyRate'].describe())
print(df['covid_cases_density'].describe())
print(df['covid_death_density'].describe())



geometries = []
covid_case_rates = []
unemploymentsForFourStates = []
medianIncomeForFourStates = []
#import matplotlib.pyplot as plt
#fig, axs = plt.subplots(2, 1, constrained_layout=False)
for count in range(len(df['FIPS'])):
    stateFIPS = int(df['FIPS'][count]/1000)
    if stateFIPS  == 4:#or stateFIPS == 35 or stateFIPS == 40  or stateFIPS == 48#in range(0,50):#
        #poly = shapely.wkt.loads(df['geometry'][count])
        #gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[poly])
        geometries.append(df['geometry'][count])
        covid_case_rates.append(df['covid_cases_density'][count])
        unemploymentsForFourStates.append(df['UnempRate2018'][count])
        medianIncomeForFourStates.append(df['medianHouseHoldIncome'][count])
        #if not (pd.isna(df['UnempRate2018'][count])):
        #    gdf.plot(linewidth=0.8, ax=axs[0], edgecolor='red', color='r', facecolor="none")
        #else:
        #    gdf.plot(linewidth=0.8, ax=axs[0], edgecolor='black', color='k', facecolor="none")

        #if not (pd.isna(df['medianHouseHoldIncome'][count])):
        #    gdf.plot(linewidth=0.8, ax=axs[1], edgecolor='red', color='r', facecolor="none")
        #else:
        #    gdf.plot(linewidth=0.8, ax=axs[1], edgecolor='black', color='k', facecolor="none")
#plt.show()






unemployment_rate_2018_df = pd.DataFrame()
median_income_2018_df = pd.DataFrame()
covid_case_rates_df = pd.DataFrame()
unemployment_rate_2018_df['values'] = unemploymentsForFourStates
unemployment_rate_2018_df['polygons'] = geometries

median_income_2018_df['values'] = medianIncomeForFourStates
median_income_2018_df['polygons'] = geometries

covid_case_rates_df['values'] = covid_case_rates
covid_case_rates_df['polygons'] = geometries

polygones = []
for polygon in geometries:#df['geometry']:
    polygones.append(shapely.wkt.loads(polygon))

combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))
#fig, ax = plt.subplots(1, 1, figsize=(10, 8))
#combined_observation_area_polygon.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
plt.show()
bounds = combined_observation_area_polygon.bounds
minx = (bounds['minx']).values
miny = (bounds['miny']).values
maxx = (bounds['maxx']).values
maxy = (bounds['maxy']).values


grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, 25, 25)


from PolygonalFunction import PolygonalValueEstimation
unemployment_value_matrix = []
median_income_value_matrix = []
covid_case_rates_value_matrix = []
count = 0
for row in grid_matrix:
    unemployment_row_values = []
    median_income_row_values = []
    covid_case_rates_row_values = []
    for point in row:
        value_unemployment = PolygonalValueEstimation(point, unemployment_rate_2018_df)
        value_median_income = PolygonalValueEstimation(point, median_income_2018_df)
        value_covid_case_rates = PolygonalValueEstimation(point, covid_case_rates_df)
        unemployment_row_values.append(value_unemployment)
        median_income_row_values.append(value_median_income)
        covid_case_rates_row_values.append(value_covid_case_rates)
        #print(count ,value_unemployment, value_median_income)
        count += 1
    unemployment_value_matrix.append(unemployment_row_values)
    median_income_value_matrix.append(median_income_row_values)
    covid_case_rates_value_matrix.append(covid_case_rates_row_values)
#print(median_income_value_matrix)
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement
'''
for count in range(10):
    hotspots2 = hotspotOfCellsUsingBFS(count, 100, 100, unemployment_value_matrix, grid)
    print("Hotspot2:", hotspots2)
    HotspotsVisualiztion(hotspots2,combined_observation_area_polygon)
'''
threshold1 = 0.03
threshold1_agreement = []
count = 0
counts = []
while threshold1 < 1:
    agreements = []
    max_UnempRate2018 = max(unemploymentsForFourStates)
    min_UnempRate2018 = min(unemploymentsForFourStates)
    variable_range = max_UnempRate2018 - min_UnempRate2018

    step_size = variable_range / 10
    best  = min_UnempRate2018 + (rand(variable_range))[0] * (max_UnempRate2018 - min_UnempRate2018)



    hotspots1 = hotspotOfCellsUsingBFS(threshold1, 25, 25, covid_case_rates_value_matrix, grid)
    #print("Hotspot1:",hotspots1)
    #HotspotsVisualiztion(hotspots1,combined_observation_area_polygon)
    hotspots2 = hotspotOfCellsUsingBFS(best,25, 25, unemployment_value_matrix, grid)
    #print("Hotspot2:",hotspots2)
    #HotspotsVisualiztion(hotspots2,combined_observation_area_polygon)
    import numpy as np
    temp =100
    best_eval = Agreement(hotspots1, hotspots2)
    #print(agreement)
    agreements.append(best_eval)
    curr, curr_eval = best, best_eval
    for count in range(100):
        candidate = curr + np.random.normal()   * step_size
        hotspots1 = hotspotOfCellsUsingBFS(threshold1, 25, 25, covid_case_rates_value_matrix, grid)
        #print("Hotspot1:",hotspots1)
        #HotspotsVisualiztion(hotspots1,combined_observation_area_polygon)
        hotspots2 = hotspotOfCellsUsingBFS(candidate,25, 25, unemployment_value_matrix, grid)
        #print("Hotspot2:",hotspots2)
        #HotspotsVisualiztion(hotspots2,combined_observation_area_polygon)


        candidate_eval = Agreement(hotspots1, hotspots2)
        #print(agreement)
        agreements.append(candidate_eval)

        if candidate_eval >= best_eval:
            # store the new point
            best, best_eval = candidate, candidate_eval
            # report progress
        diff = candidate_eval - curr_eval
        t = temp / float(count+ 1)
        metropolis = math.exp(-diff / t)
        if diff < 0 or rand() < metropolis:
            # store the new current point
            curr, curr_eval = candidate, candidate_eval
    threshold1 += 0.05
    threshold1_agreement.append(max(agreements))
    counts.append(threshold1)
    count += 1

import matplotlib.pyplot as plt
plt.plot(counts, threshold1_agreement)
plt.xlabel('Thresholds')
plt.ylabel('Agreement Value')
plt.title('Threshold vs Agreement Value')
plt.show()
#HotspotsVisualiztion(hotspots)
#contourPlot(unemployment_value_mat
#
# rix,grid[0],grid[1])
#contourPlot(median_income_value_matrix,grid[0],grid[1])

#print("HI")
