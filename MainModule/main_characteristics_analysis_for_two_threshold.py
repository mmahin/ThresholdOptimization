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
avg_precipitation_for_county = []
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
        avg_precipitation_for_county.append(df['bachelor_degree_density_2014_2018'][count])
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
bachelor_degree_density_2014_2018_df = pd.DataFrame()
avg_precipitation_for_county_df = pd.DataFrame()

covid_case_rates_df = pd.DataFrame()
unemployment_rate_2018_df['values'] = unemploymentsForFourStates
unemployment_rate_2018_df['polygons'] = geometries

median_income_2018_df['values'] = medianIncomeForFourStates
median_income_2018_df['polygons'] = geometries

covid_case_rates_df['values'] = covid_case_rates
covid_case_rates_df['polygons'] = geometries

bachelor_degree_density_2014_2018_df['values'] = bachelor_degree_density_2014_2018
bachelor_degree_density_2014_2018_df['polygons'] = geometries

avg_precipitation_for_county_df['values'] = avg_precipitation_for_county
avg_precipitation_for_county_df['polygons'] = geometries

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
#unemployment_value_matrix = []
median_income_value_matrix = []
covid_case_rates_value_matrix = []
bachelor_degree_density_2014_2018_value_matrix = []
avg_precipitation_for_county_value_matrix = []
count = 0
for row in grid_matrix:
    unemployment_row_values = []
    median_income_row_values = []
    covid_case_rates_row_values = []
    bachelor_degree_density_2014_2018_values = []
    avg_precipitation_for_county_value_row_values = []
    for point in row:
        #value_unemployment = PolygonalValueEstimation(point, unemployment_rate_2018_df)
        #value_median_income = PolygonalValueEstimation(point, median_income_2018_df)
        value_covid_case_rates = PolygonalValueEstimation(point, covid_case_rates_df)
        #value_bachelor_degree_density_2014_2018 = PolygonalValueEstimation(point, bachelor_degree_density_2014_2018_df)
        value_avg_precipitation_for_county = PolygonalValueEstimation(point, avg_precipitation_for_county_df)
        #unemployment_row_values.append(value_unemployment)
        #median_income_row_values.append(value_median_income)
        #bachelor_degree_density_2014_2018_values.append(value_bachelor_degree_density_2014_2018)
        covid_case_rates_row_values.append(value_covid_case_rates)
        avg_precipitation_for_county_value_row_values.append(value_avg_precipitation_for_county)

        #print(count ,value_unemployment, value_median_income)
        count += 1
    #unemployment_value_matrix.append(unemployment_row_values)
    #median_income_value_matrix.append(median_income_row_values)
    #bachelor_degree_density_2014_2018_value_matrix.append(bachelor_degree_density_2014_2018_values)
    covid_case_rates_value_matrix.append(covid_case_rates_row_values)
    avg_precipitation_for_county_value_matrix.append(avg_precipitation_for_county_value_row_values)
#print(median_income_value_matrix)
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.agreementFunction import Agreement

steps = 50
#max_MedianIncome2018 = max(medianIncomeForFourStates)
#min_MedianIncome2018 = min(medianIncomeForFourStates)
#variable_cutpoint_MedianIncome2018 = (max_MedianIncome2018 - min_MedianIncome2018)/steps

#max_bachelor_degree_density_2014_2018 = max(bachelor_degree_density_2014_2018)
#min_bachelor_degree_density_2014_2018 = min(bachelor_degree_density_2014_2018)
#variable_cutpoint_bachelor_degree_density_2014_2018 = (max_bachelor_degree_density_2014_2018 - min_bachelor_degree_density_2014_2018)/steps

max_avg_precipitation_for_county = max(avg_precipitation_for_county)
min_avg_precipitation_for_county = min(avg_precipitation_for_county)
variable_cutpoint_avg_precipitation_for_county= (max_avg_precipitation_for_county - min_avg_precipitation_for_county)/steps

max_covid_case_rates = max(covid_case_rates)
min_covid_case_rates = min(covid_case_rates)
variable_cutpoint_covid_case_rates = (max_covid_case_rates - min_covid_case_rates)/steps
threshold1_values = []

threshold1 = min_covid_case_rates

threshold1_df_values = []
threshold2_df_values = []
agreements_df_values = []

agreements = []
count = 0
for i in range(0,steps):
    #threshold2 = min_MedianIncome2018
    #threshold2 = min_bachelor_degree_density_2014_2018
    threshold2 = min_avg_precipitation_for_county
    agreements_temp = []
    threshold2_values = []

    for j in range(0,steps):
        hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row, grid_column, covid_case_rates_value_matrix, grid)
        hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row, grid_column, avg_precipitation_for_county_value_matrix, grid)
        agreement = Agreement(hotspots1, hotspots2)

        agreements_temp.append(agreement)
        '''
        if i % 10 ==0 and count  == j :
            HotspotsVisualiztion(hotspots1, combined_observation_area_polygon)
            HotspotsVisualiztion(hotspots2, combined_observation_area_polygon)
            threshold1_df_values.append(threshold1)
            threshold2_df_values.append(threshold2)
            agreements_df_values.append(agreement)
            break
        '''
        #print(count, threshold1,threshold2, agreement)
        threshold2_values.append(threshold2)
        #threshold2 += variable_cutpoint_bachelor_degree_density_2014_2018
        threshold2 += variable_cutpoint_avg_precipitation_for_county
        count += 1
    agreements.append(agreements_temp)

    threshold1_values.append(threshold1)
    threshold1 += variable_cutpoint_covid_case_rates
'''
interestingness = pd.DataFrame()
interestingness['Covid-19'] = threshold1_df_values
interestingness['Median Income'] = threshold2_df_values
interestingness['Interstingness'] = agreements_df_values
interestingness.to_csv("interestingneess",index=False)
'''
import numpy as np
x = np.linspace(min_covid_case_rates, max_covid_case_rates, steps)
y = np.linspace(min_avg_precipitation_for_county, max_avg_precipitation_for_county, steps)
X, Y = np.meshgrid(x, y)
Z= agreements

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.scatter3D(np.array(threshold1_values), np.array(threshold2_values), np.array(agreements), c=agreements, cmap='Greens');
print(np.shape(X),np.shape(Y),np.shape(np.array(Z)))
surf = ax.plot_surface(X, Y, np.array(Z), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('Covid-19 Infection Rate (t)')
ax.set_ylabel('Average Temperature(t\')')
ax.set_zlabel('$I_{(Covid-19\ Infection\ Rate, t),(Average\ Temperature, t\'))}$')
#ax.set_title('Variables Thresholds vs Agreement Values');
plt.show()

