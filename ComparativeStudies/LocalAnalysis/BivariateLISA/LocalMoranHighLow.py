import numpy as np
from scipy.stats import pearsonr
import pandas as pd
import geopandas as gpd
from esda.moran import Moran_BV, Moran_Local_BV
#from splot.esda import plot_moran_bv_simulation, plot_moran_bv
from libpysal.weights.contiguity import Queen
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes
# Calculate local Moran's I using the esda.moran.Moran_Local_BV function


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

local_moran = Moran_Local_BV(df[variable1], df[variable2], w)

# Threshold the standardized local Moran's I values
threshold = 0
high = np.where(local_moran.Is > threshold)[0]
low = np.where(local_moran.Is < -threshold)[0]

# Initialize arrays to store the indices of high-high, high-low, low-high, and low-low spatial clusters
high_high = []
high_low = []
low_high = []
low_low = []

# Loop over each observation
for i in range(local_moran.n):
    neighbors = w.neighbors[i]
    if i in high:
        if all(np.isin(neighbors, high)):
            high_high.append(i)
        else:
            high_low.append(i)
    elif i in low:
        if all(np.isin(neighbors, low)):
            low_low.append(i)
        else:
            low_high.append(i)

# Convert the lists of indices to numpy arrays
high_high = np.array(high_high)
high_low = np.array(high_low)
low_high = np.array(low_high)
low_low = np.array(low_low)

print(high_high)