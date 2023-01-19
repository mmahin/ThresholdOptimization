from scipy.stats import pearsonr
import pandas as pd
import geopandas as gpd
from esda.moran import Moran_BV, Moran_Local_BV
#from splot.esda import plot_moran_bv_simulation, plot_moran_bv
from libpysal.weights.contiguity import Queen
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes

import numpy as np
import matplotlib.pyplot as plt

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = getAllVariableDataframesAndSpatialIndexes(data_path)
gdf = gpd.GeoDataFrame(columns=['feature'], geometry='feature')
gdf['feature'] = df['geometry']
w = Queen.from_dataframe(df)

variables = ['covid_cases_density', 'bachelor_degree_density_2014_2018', 'avg_precipitation_for_county', 'avg_temp_for_county',
             'population_density_on_land_2010', 'household_density_on_land_2010', 'UnempRate2018', 'PctEmpAgriculture',
             'PctEmpMining', 'PctEmpConstruction', 'PctEmpManufacturing', 'PctEmpTrade', 'PctEmpTrans', 'PctEmpInformation',
             'PctEmpFIRE', 'PctEmpServices', 'PctEmpGovt', 'medianHouseHoldIncome', 'povertyRate', 'covid_death_density']
labels = ['Covid-19 Infection Rate', 'Bachelor Degree Rate', 'Average Precipitation', 'Average Temperature',
             'Population Density', 'Household Density', 'Unemployment Rate', 'Agriculture Employee Rate',
             'Mining Employee Rate', 'Construction Employee Rate', 'Manufacturing Employee Rate', 'Trade  Employee Rate',
             'Tranportation Employee Rate', 'Information  Employee Rate', 'FIRE Service  Employee Rate',
              'Services  Employee Rate', 'Goverment  Employee Rate', 'Median HouseHold Income', 'Poverty Rate', 'Covid-19 Death Rate']
correlation_mat = np.empty([len(variables),len(variables)])

for count1 in range(len(variables)):
      df[variables[count1]].fillna(int(df[variables[count1]].mean()), inplace=True)
      for count2 in range(len(variables)):
            df[variables[count2]].fillna(int(df[variables[count2]].mean()), inplace=True)
            moran_bv1 = Moran_BV(df[variables[count1]], df[variables[count2]], w)
            correlation_mat[count1][count2] = round(moran_bv1.I,2)

fig, ax = plt.subplots()
ax.matshow(correlation_mat, cmap='hot')
for (i, j), z in np.ndenumerate(correlation_mat):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')
#plt.colorbar()
xaxis = np.arange(len(labels))
ax.set_xticks(xaxis,rotation=90)
ax.set_yticks(xaxis,rotation=90)
ax.set_xticklabels(labels,rotation=90)
ax.set_yticklabels(labels)
plt.show()

#Set Inputs
#data access inputs
variable1 = 'covid_cases_density'
variable2 = 'bachelor_degree_density_2014_2018'
variable3 = 'avg_precipitation_for_county'
variable4 = 'avg_temp_for_county'
variable5 = 'population_density_on_land_2010'
variable6 = 'household_density_on_land_2010'
variable7 = 'UnempRate2018'
variable8 = 'PctEmpAgriculture'
variable9 = 'PctEmpMining'
variable10 = 'PctEmpConstruction'
variable11 = 'PctEmpManufacturing'
variable12 = 'PctEmpTrade'
variable13 = 'PctEmpTrans'
variable14 = 'PctEmpInformation'
variable15 = 'PctEmpFIRE'
variable16 = 'PctEmpServices'
variable17 = 'PctEmpGovt'
variable18 = 'medianHouseHoldIncome'
variable19 = 'povertyRate'
variable20 = 'covid_death_density'



df[variable1].fillna(int(df[variable1].mean()), inplace=True)
df[variable2].fillna(int(df[variable2].mean()), inplace=True)
df[variable3].fillna(int(df[variable2].mean()), inplace=True)
df[variable4].fillna(int(df[variable2].mean()), inplace=True)
df[variable5].fillna(int(df[variable2].mean()), inplace=True)
df[variable6].fillna(int(df[variable2].mean()), inplace=True)
df[variable7].fillna(int(df[variable2].mean()), inplace=True)
df[variable8].fillna(int(df[variable2].mean()), inplace=True)
df[variable9].fillna(int(df[variable2].mean()), inplace=True)
df[variable10].fillna(int(df[variable2].mean()), inplace=True)
df[variable11].fillna(int(df[variable2].mean()), inplace=True)
df[variable12].fillna(int(df[variable2].mean()), inplace=True)
df[variable13].fillna(int(df[variable2].mean()), inplace=True)
df[variable14].fillna(int(df[variable2].mean()), inplace=True)
df[variable15].fillna(int(df[variable2].mean()), inplace=True)
df[variable16].fillna(int(df[variable2].mean()), inplace=True)
df[variable17].fillna(int(df[variable2].mean()), inplace=True)
df[variable18].fillna(int(df[variable2].mean()), inplace=True)
df[variable19].fillna(int(df[variable2].mean()), inplace=True)
df[variable20].fillna(int(df[variable2].mean()), inplace=True)

moran_bv1 = Moran_BV(df[variable1], df[variable2], w)
moran_bv2 = Moran_BV(df[variable1], df[variable3], w)
moran_bv3 = Moran_BV(df[variable1], df[variable4], w)
moran_bv4 = Moran_BV(df[variable1], df[variable5], w)
moran_bv5 = Moran_BV(df[variable1], df[variable6], w)
moran_bv6 = Moran_BV(df[variable1], df[variable7], w)
moran_bv7 = Moran_BV(df[variable1], df[variable8], w)
moran_bv8 = Moran_BV(df[variable1], df[variable9], w)
moran_bv9 = Moran_BV(df[variable1], df[variable10], w)
moran_bv10 = Moran_BV(df[variable1], df[variable11], w)
moran_bv11 = Moran_BV(df[variable1], df[variable12], w)
moran_bv12 = Moran_BV(df[variable1], df[variable13], w)
moran_bv13 = Moran_BV(df[variable1], df[variable14], w)
moran_bv14 = Moran_BV(df[variable1], df[variable15], w)
moran_bv15 = Moran_BV(df[variable1], df[variable16], w)
moran_bv16 = Moran_BV(df[variable1], df[variable17], w)
moran_bv17 = Moran_BV(df[variable1], df[variable18], w)
moran_bv18 = Moran_BV(df[variable1], df[variable19], w)
moran_bv19 = Moran_BV(df[variable1], df[variable20], w)
print(round(moran_bv1.I,2), round(moran_bv2.I,2), round(moran_bv3.I,2), round(moran_bv4.I,2), round(moran_bv5.I,2),
      round(moran_bv6.I,2), round(moran_bv7.I,2), round(moran_bv8.I,2), round(moran_bv9.I,2), round(moran_bv10.I,2),
      round(moran_bv11.I,2), round(moran_bv12.I,2), round(moran_bv13.I,2), round(moran_bv14.I,2), round(moran_bv15.I,2),
      round(moran_bv16.I,2), round(moran_bv17.I,2), round(moran_bv18.I,2), round(moran_bv19.I,2))
print(round(moran_bv1.p_sim,2), round(moran_bv2.p_sim,2), round(moran_bv3.p_sim,2), round(moran_bv4.p_sim,2), round(moran_bv5.p_sim,2),
      round(moran_bv6.p_sim,2), round(moran_bv7.p_sim,2), round(moran_bv8.p_sim,2), round(moran_bv9.p_sim,2), round(moran_bv10.p_sim,2),
      round(moran_bv11.p_sim,2), round(moran_bv12.p_sim,2), round(moran_bv13.p_sim,2), round(moran_bv14.p_sim,2), round(moran_bv15.p_sim,2),
      round(moran_bv16.p_sim,2), round(moran_bv17.p_sim,2), round(moran_bv18.p_sim,2), round(moran_bv19.I,2))

