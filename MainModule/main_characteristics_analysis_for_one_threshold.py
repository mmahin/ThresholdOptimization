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

'''
FIPS
geometry
bachelor_degree_density_2014_2018
avg_precipitation_for_county
avg_temp_for_county
covid_cases
covid_deaths
population_density_on_land_2010
household_density_on_land_2010
UnempRate2018
PctEmpAgriculture
PctEmpMining
PctEmpConstruction
PctEmpManufacturing
PctEmpTrade
PctEmpTrans
PctEmpInformation
PctEmpFIRE
PctEmpServices
PctEmpGovt
medianHouseHoldIncome
povertyRate
covid_cases_density
covid_death_density
'''


geometries = []
covid_case_rates = []
unemploymentsForFourStates = []
medianIncomeForFourStates = []
bachelor_degree_density_2014_2018 = []
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
        bachelor_degree_density_2014_2018.append(df['bachelor_degree_density_2014_2018'][count])
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
bachelor_degree_density_2014_2018_df = pd.DataFrame()
unemployment_rate_2018_df['values'] = unemploymentsForFourStates
unemployment_rate_2018_df['polygons'] = geometries

median_income_2018_df['values'] = medianIncomeForFourStates
median_income_2018_df['polygons'] = geometries

bachelor_degree_density_2014_2018_df['values'] = bachelor_degree_density_2014_2018
bachelor_degree_density_2014_2018_df['polygons'] = geometries

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

grid_row = 100
grid_column = 100
grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row, grid_column)


from PolygonalFunction import PolygonalValueEstimation
unemployment_value_matrix = []
median_income_value_matrix = []
bachelor_degree_density_2014_2018_value_matrix = []
covid_case_rates_value_matrix = []
count = 0
for row in grid_matrix:
    #unemployment_row_values = []
    #median_income_row_values = []
    bachelor_degree_density_2014_2018_row_values = []
    covid_case_rates_row_values = []
    for point in row:
        #value_unemployment = PolygonalValueEstimation(point, unemployment_rate_2018_df)
        #value_median_income = PolygonalValueEstimation(point, median_income_2018_df)
        value_bachelor_degree_density_2014_2018 = PolygonalValueEstimation(point, bachelor_degree_density_2014_2018_df)
        value_covid_case_rates = PolygonalValueEstimation(point, covid_case_rates_df)
        #unemployment_row_values.append(value_unemployment)
        #median_income_row_values.append(value_median_income)
        bachelor_degree_density_2014_2018_row_values.append(value_bachelor_degree_density_2014_2018)
        covid_case_rates_row_values.append(value_covid_case_rates)
        #print(count ,value_unemployment, value_median_income)
        count += 1
    bachelor_degree_density_2014_2018_value_matrix.append(bachelor_degree_density_2014_2018_row_values)
    #unemployment_value_matrix.append(unemployment_row_values)
    #median_income_value_matrix.append(median_income_row_values)
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
'''
max_MedianIncome2018 = max(medianIncomeForFourStates)
min_MedianIncome2018 = min(medianIncomeForFourStates)
variable_cutpoint_MedianIncome2018 = (max_MedianIncome2018 - min_MedianIncome2018)/steps


max_unemployment  = max(unemploymentsForFourStates)
min_unemployment  = min(unemploymentsForFourStates)
variable_cutpoint_unemployment  = (max_unemployment  - min_unemployment)/steps

'''

max_bachelor_degree_density_2014_2018  = max(bachelor_degree_density_2014_2018)
min_bachelor_degree_density_2014_2018  = min(bachelor_degree_density_2014_2018)
variable_cutpoint_bachelor_degree_density_2014_2018  = (max_bachelor_degree_density_2014_2018  - min_bachelor_degree_density_2014_2018)/steps

max_covid_case_rates = max(covid_case_rates)
min_covid_case_rates = min(covid_case_rates)
variable_cutpoint_covid_case_rates = (max_covid_case_rates - min_covid_case_rates)/steps
threshold1_values = []

threshold1 = 0.25



agreements = []
threshold2 = min_bachelor_degree_density_2014_2018
counts = []
threshold2_values = []
hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row, grid_column, covid_case_rates_value_matrix, grid)
for j in range(0,steps):
    hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row, grid_column, bachelor_degree_density_2014_2018_value_matrix, grid)
    agreement = Agreement(hotspots1, hotspots2)
    #HotspotsVisualiztion(hotspots1, combined_observation_area_polygon)
    #HotspotsVisualiztion(hotspots2, combined_observation_area_polygon)
    #print(threshold1, threshold2, agreement)
    agreements.append(agreement)
    threshold2_values.append(threshold2)
    counts.append(j)
    threshold2 += variable_cutpoint_bachelor_degree_density_2014_2018
    #print(threshold1,threshold2)


import matplotlib.pyplot as plt
plt.plot(threshold2_values, agreements)
plt.xlabel('Unemployment Rate')
plt.ylabel('$I_{(Covid-19\ Infection\ Rate, 0.25),(Unemployment\ Rate, t\'))}$')
#plt.title('Threshold vs Agreement Value')
plt.show()
