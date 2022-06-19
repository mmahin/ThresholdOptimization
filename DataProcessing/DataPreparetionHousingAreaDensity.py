import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/housing_area_density_national_2010_census.csv',sep=',')
#for item in df:
#    print(item)

FIPS = []
population_density_on_land_2010 = []
household_density_on_land_2010 = []
for count in range(len(df['Id'])):
    if df['Target Geo Id2'][count] > 1000:
        FIPS.append(int(df['Target Geo Id2'][count]))
        population_density_on_land_2010.append(df['Density per square mile of land area - Population'][count])
        household_density_on_land_2010.append(df['Density per square mile of land area - Housing units'][count])

new_df = pd.DataFrame()
new_df['FIPS'] = FIPS
new_df['population_density_on_land_2010'] = population_density_on_land_2010
new_df['household_density_on_land_2010'] = household_density_on_land_2010
new_df.to_csv('InitialExtractedData/HouseHoldDensity2010.csv', index= False)
