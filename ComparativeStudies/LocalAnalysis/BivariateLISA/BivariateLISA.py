from scipy.stats import pearsonr
import pandas as pd
import geopandas as gpd
from esda.moran import Moran_BV, Moran_Local_BV
#from splot.esda import plot_moran_bv_simulation, plot_moran_bv
from libpysal.weights.contiguity import Queen
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

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

df = getAllVariableDataframesAndSpatialIndexes(data_path)
gdf = gpd.GeoDataFrame(columns=['feature'], geometry='feature')
gdf['feature'] = df['geometry']
w = Queen.from_dataframe(df)

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

moran_bv1 = Moran_Local_BV(df[variable1], df[variable2], w)
moran_bv2 = Moran_Local_BV(df[variable1], df[variable3], w)
moran_bv3 = Moran_Local_BV(df[variable1], df[variable4], w)
moran_bv4 = Moran_Local_BV(df[variable1], df[variable5], w)
moran_bv5 = Moran_Local_BV(df[variable1], df[variable6], w)
moran_bv6 = Moran_Local_BV(df[variable1], df[variable7], w)
moran_bv7 = Moran_Local_BV(df[variable1], df[variable8], w)
moran_bv8 = Moran_Local_BV(df[variable1], df[variable9], w)
moran_bv9 = Moran_Local_BV(df[variable1], df[variable10], w)
moran_bv10 = Moran_Local_BV(df[variable1], df[variable11], w)
moran_bv11 = Moran_Local_BV(df[variable1], df[variable12], w)
moran_bv12 = Moran_Local_BV(df[variable1], df[variable13], w)
moran_bv13 = Moran_Local_BV(df[variable1], df[variable14], w)
moran_bv14 = Moran_Local_BV(df[variable1], df[variable15], w)
moran_bv15 = Moran_Local_BV(df[variable1], df[variable16], w)
moran_bv16 = Moran_Local_BV(df[variable1], df[variable17], w)
moran_bv17 = Moran_Local_BV(df[variable1], df[variable18], w)
moran_bv18 = Moran_Local_BV(df[variable1], df[variable19], w)
moran_bv19 = Moran_Local_BV(df[variable1], df[variable20], w)

from splot.esda import lisa_cluster
import matplotlib.pyplot as plt
print("Covid-19,bachelor_degree")
lm = lisa_cluster(moran_bv1, gdf, p=1, figsize = (9,9))

print(moran_bv1.q)
plt.show()
print("Covid-19,avg_precipitation")
lisa_cluster(moran_bv2, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,avg_temp")
lisa_cluster(moran_bv3, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,population_density")
lisa_cluster(moran_bv4, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,household_density")
lisa_cluster(moran_bv5, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,UnempRate")
lisa_cluster(moran_bv6, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpAgriculture")
lisa_cluster(moran_bv7, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpMining")
lisa_cluster(moran_bv8, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpConstruction")
lisa_cluster(moran_bv9, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpManufacturing")
lisa_cluster(moran_bv10, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpTrade")
lisa_cluster(moran_bv11, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpTrans")
lisa_cluster(moran_bv12, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpInformation")
lisa_cluster(moran_bv13, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpFIRE")
lisa_cluster(moran_bv14, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpServices")
lisa_cluster(moran_bv15, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,EmpGovt")
lisa_cluster(moran_bv16, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,medianHouseHoldIncome")
lisa_cluster(moran_bv17, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,povertyRate")
lisa_cluster(moran_bv18, gdf, p=0.05, figsize = (9,9))
plt.show()
print("Covid-19,covid_death_density")
lisa_cluster(moran_bv19, gdf, p=0.05, figsize = (9,9))

plt.show()


