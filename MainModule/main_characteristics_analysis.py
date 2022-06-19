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




geometries = []
covid_case_rates = []
unemploymentsForFourStates = []
medianIncomeForFourStates = []
#import matplotlib.pyplot as plt
#fig, axs = plt.subplots(2, 1, constrained_layout=False)
for count in range(len(df['FIPS'])):
    stateFIPS = int(df['FIPS'][count]/1000)
    if stateFIPS in range(0,50):#== 4 or stateFIPS == 35 or stateFIPS == 40  or stateFIPS == 48:##
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

grid_row = 25
grid_column = 25
grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row, grid_column)


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
steps = 100
max_UnempRate2018 = max(unemploymentsForFourStates)
min_UnempRate2018 = min(unemploymentsForFourStates)
variable_cutpoint_UnempRate2018 = (max_UnempRate2018 - min_UnempRate2018)/steps

max_covid_case_rates = max(covid_case_rates)
min_covid_case_rates = min(covid_case_rates)
variable_cutpoint_covid_case_rates = (max_covid_case_rates - min_covid_case_rates)/steps
threshold1_values = []

threshold1 = min_covid_case_rates



agreements = []
for i in range(0,steps):
    threshold2 = min_UnempRate2018
    agreements_temp = []
    threshold2_values = []
    for j in range(0,steps):
        hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row, grid_column, covid_case_rates_value_matrix, grid)
        hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row, grid_column, unemployment_value_matrix, grid)
        agreement = Agreement(hotspots1, hotspots2)
        agreements_temp.append(agreement)
        threshold2_values.append(threshold2)
        threshold2 += variable_cutpoint_UnempRate2018
    agreements.append(agreements_temp)

    threshold1_values.append(threshold1)
    threshold1 += variable_cutpoint_covid_case_rates

import numpy as np
x = np.linspace(min_covid_case_rates, max_covid_case_rates, steps)
y = np.linspace(min_UnempRate2018, max_UnempRate2018, steps)
X, Y = np.meshgrid(x, y)
Z= agreements

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.scatter3D(np.array(threshold1_values), np.array(threshold2_values), np.array(agreements), c=agreements, cmap='Greens');
print(np.shape(X),np.shape(Y),np.shape(np.array(Z)))
surf = ax.plot_surface(X, Y, np.array(Z), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('Covid-19 Infection Rate')
ax.set_ylabel('Unemployment Rate')
ax.set_zlabel('Agreement Values')
ax.set_title('Variables Thresholds vs Agreement Values');
plt.show()

#plt.plot(counts, threshold1_agreement)
#plt.xlabel('Thresholds')
#plt.ylabel('Agreement Value')
#plt.title('Threshold vs Agreement Value')
#plt.show()
#HotspotsVisualiztion(hotspots)
#contourPlot(unemployment_value_mat
#
# rix,grid[0],grid[1])
#contourPlot(median_income_value_matrix,grid[0],grid[1])

#print("HI")
